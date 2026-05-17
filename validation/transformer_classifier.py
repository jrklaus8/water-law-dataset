"""
Transformer-Based Residual Classifier (Route A)
================================================
Fine-tunes a multilingual transformer (XLM-RoBERTa) on the regex engine's
classified decisions, then applies it to the other_water residual.

This is the Route A methodology documented in FUTURE_WORK.md and in the
manuscript's §4.8 validation protocol.

Workflow:
  1. python validation/transformer_classifier.py prepare   -- builds train/val splits
  2. python validation/transformer_classifier.py train     -- fine-tunes the model
  3. python validation/transformer_classifier.py classify  -- labels the residual
  4. python validation/transformer_classifier.py compare   -- vs second-coder labels

Requirements:
  pip install transformers datasets torch scikit-learn pandas

GPU recommended for training; CPU is feasible for small datasets (<5k examples)
but will take several hours. For a GPU in Google Colab (free T4):
  runtime: ~15-25 minutes for 5,000 training examples, 3 epochs.

Model choice: xlm-roberta-base (559M params, 100 languages including
Portuguese, Dutch, English, French). Alternatives:
  - bert-base-multilingual-cased (smaller, faster, slightly lower accuracy)
  - neuralmind/bert-base-portuguese-cased (Portuguese-only; better for BR subset)
  - GroNLP/bert-base-dutch-cased (Dutch-only; better for NL subset)
"""
import argparse, json, sys, os, random
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

DATA_PATH = Path(os.getenv('CODED_CSV',
    Path(__file__).parent.parent / 'data' / 'water_law_global_coded.csv'))
MODEL_DIR = Path(__file__).parent / 'transformer_model'
RESIDUAL_OUT = Path(__file__).parent / 'residual_classified_by_transformer.csv'

# Categories to model (exclude residual and false-positive classes)
MODELLED_CATS = [
    'tariff_dispute', 'connection_refusal', 'water_quality', 'informal_settlement',
    'groundwater', 'sanitation_sewage', 'flooding', 'riparian_waterway',
    'environmental_protection', 'spatial_planning_water', 'waterboard_governance',
    'pipe_leak_damage', 'water_theft_fraud', 'regulatory_permit', 'hydroelectric_dam',
    'irrigation_agricultural', 'fisheries_water', 'water_infrastructure_contract',
    'flood_protection', 'not_water_related',
]


def load_data():
    try:
        import pandas as pd
    except ImportError:
        sys.exit('pip install pandas')
    if not DATA_PATH.exists():
        sys.exit(f'Coded CSV not found: {DATA_PATH}\nSet CODED_CSV env var.')
    df = pd.read_csv(DATA_PATH, low_memory=False, encoding='utf-8-sig')
    text_cols = [c for c in ['title', 'summary', 'ementa', 'snippet'] if c in df.columns]
    df['_text'] = df[text_cols].fillna('').apply(
        lambda r: ' '.join(str(v) for v in r)[:512], axis=1
    )
    return df


def prepare(args):
    """Step 1: Build training and validation splits from classified decisions."""
    import pandas as pd

    df = load_data()
    labelled = df[df['governance_cat'].isin(MODELLED_CATS)].copy()
    residual = df[df['governance_cat'] == 'other_water'].copy()

    print(f'Labelled examples available: {len(labelled):,}')
    print(f'Residual to classify later:  {len(residual):,}')
    print(f'\nCategory distribution:')
    for cat, n in labelled['governance_cat'].value_counts().items():
        print(f'  {cat:<35} {n:>6,}')

    # Train/val split (80/20 stratified by category)
    from sklearn.model_selection import train_test_split
    train, val = train_test_split(
        labelled, test_size=0.2, stratify=labelled['governance_cat'], random_state=42
    )

    out_dir = Path(__file__).parent / 'transformer_data'
    out_dir.mkdir(exist_ok=True)
    train[['_text', 'governance_cat']].to_csv(out_dir / 'train.csv', index=False)
    val[['_text', 'governance_cat']].to_csv(out_dir / 'val.csv', index=False)
    residual[['_text']].to_csv(out_dir / 'residual.csv', index=False)

    # Save label mapping
    label2id = {cat: i for i, cat in enumerate(sorted(MODELLED_CATS))}
    with open(out_dir / 'label2id.json', 'w') as f:
        json.dump(label2id, f, indent=2)

    print(f'\nSaved to {out_dir}:')
    print(f'  train.csv:   {len(train):,} examples')
    print(f'  val.csv:     {len(val):,} examples')
    print(f'  residual.csv:{len(residual):,} examples to classify')


def train(args):
    """Step 2: Fine-tune XLM-RoBERTa on the training split."""
    try:
        from transformers import (AutoTokenizer, AutoModelForSequenceClassification,
                                   TrainingArguments, Trainer)
        from datasets import Dataset
        import torch
        import numpy as np
    except ImportError:
        sys.exit('pip install transformers datasets torch')

    import pandas as pd

    data_dir = Path(__file__).parent / 'transformer_data'
    if not (data_dir / 'train.csv').exists():
        sys.exit('Run "prepare" step first: python transformer_classifier.py prepare')

    with open(data_dir / 'label2id.json') as f:
        label2id = json.load(f)
    id2label = {v: k for k, v in label2id.items()}
    n_labels = len(label2id)

    train_df = pd.read_csv(data_dir / 'train.csv')
    val_df   = pd.read_csv(data_dir / 'val.csv')

    train_df['label'] = train_df['governance_cat'].map(label2id)
    val_df['label']   = val_df['governance_cat'].map(label2id)

    # Drop any unmapped labels (shouldn't happen, but defensive)
    train_df = train_df.dropna(subset=['label'])
    val_df   = val_df.dropna(subset=['label'])

    MODEL_NAME = args.model if hasattr(args, 'model') and args.model else 'xlm-roberta-base'
    print(f'Loading tokenizer: {MODEL_NAME}')
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    def tokenize(batch):
        return tokenizer(batch['_text'], truncation=True, padding='max_length',
                         max_length=256)

    train_ds = Dataset.from_pandas(train_df[['_text', 'label']]).map(tokenize, batched=True)
    val_ds   = Dataset.from_pandas(val_df[['_text', 'label']]).map(tokenize, batched=True)
    train_ds = train_ds.rename_column('label', 'labels')
    val_ds   = val_ds.rename_column('label', 'labels')

    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME, num_labels=n_labels,
        id2label=id2label, label2id=label2id
    )

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    training_args = TrainingArguments(
        output_dir=str(MODEL_DIR),
        eval_strategy='epoch',
        save_strategy='epoch',
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=32,
        num_train_epochs=3,
        weight_decay=0.01,
        load_best_model_at_end=True,
        metric_for_best_model='eval_loss',
        logging_dir=str(MODEL_DIR / 'logs'),
        report_to='none',
    )

    def compute_metrics(eval_pred):
        from sklearn.metrics import accuracy_score, f1_score
        logits, labels = eval_pred
        preds = np.argmax(logits, axis=-1)
        return {
            'accuracy': accuracy_score(labels, preds),
            'f1_macro': f1_score(labels, preds, average='macro', zero_division=0),
        }

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        compute_metrics=compute_metrics,
    )

    print('Training...')
    trainer.train()
    trainer.save_model(str(MODEL_DIR / 'best'))
    tokenizer.save_pretrained(str(MODEL_DIR / 'best'))
    print(f'\nModel saved to: {MODEL_DIR / "best"}')

    # Evaluate on validation set
    results = trainer.evaluate()
    print(f'\nValidation results:')
    for k, v in results.items():
        print(f'  {k}: {v:.4f}')


def classify(args):
    """Step 3: Apply the fine-tuned model to the other_water residual."""
    try:
        from transformers import pipeline
        import pandas as pd
    except ImportError:
        sys.exit('pip install transformers pandas')

    model_path = str(MODEL_DIR / 'best')
    if not Path(model_path).exists():
        sys.exit('Run "train" step first: python transformer_classifier.py train')

    data_dir = Path(__file__).parent / 'transformer_data'
    residual_df = pd.read_csv(data_dir / 'residual.csv')

    print(f'Classifying {len(residual_df):,} residual decisions...')
    classifier = pipeline('text-classification', model=model_path,
                          device=0 if _has_gpu() else -1, truncation=True,
                          max_length=256, batch_size=32)

    predictions = classifier(residual_df['_text'].tolist())
    residual_df['transformer_label'] = [p['label'] for p in predictions]
    residual_df['transformer_score'] = [round(p['score'], 4) for p in predictions]

    residual_df.to_csv(RESIDUAL_OUT, index=False)
    print(f'\nClassified residual saved to: {RESIDUAL_OUT}')

    print('\nTransformer classification distribution:')
    for cat, n in residual_df['transformer_label'].value_counts().items():
        print(f'  {cat:<35} {n:>5,} ({n/len(residual_df)*100:.1f}%)')

    # Key finding: how many connection_refusal and informal_settlement in residual?
    for cat in ['connection_refusal', 'informal_settlement']:
        n = (residual_df['transformer_label'] == cat).sum()
        print(f'\n*** {cat} found in residual by transformer: {n} ***')


def compare(args):
    """Step 4: Compare transformer predictions with second-coder labels."""
    import pandas as pd

    if not RESIDUAL_OUT.exists():
        sys.exit('Run "classify" step first.')
    coder2_path = Path(__file__).parent / 'coder2_labels.csv'
    if not coder2_path.exists():
        sys.exit(f'Second-coder labels not found: {coder2_path}')

    transformer_df = pd.read_csv(RESIDUAL_OUT)
    coder2_df = pd.read_csv(coder2_path)

    # Merge on available ID
    merged = transformer_df.merge(coder2_df, left_index=True, right_on='case_id',
                                   how='inner')
    if len(merged) == 0:
        sys.exit('No matching records. Ensure case_id column in coder2_labels.csv '
                 'matches the row index of the residual.')

    # Agreement rate
    agree = (merged['transformer_label'] == merged['label']).mean()
    print(f'Transformer vs second-coder agreement: {agree:.3f} ({agree*100:.1f}%)')
    print('\nThis is not kappa — use kappa_calculator.py for the formal statistic.')


def _has_gpu() -> bool:
    try:
        import torch
        return torch.cuda.is_available()
    except ImportError:
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Transformer-based residual classifier.')
    sub = parser.add_subparsers(dest='command')
    sub.add_parser('prepare', help='Build train/val/residual splits')
    train_p = sub.add_parser('train', help='Fine-tune XLM-RoBERTa')
    train_p.add_argument('--model', default='xlm-roberta-base',
                         help='HuggingFace model name')
    sub.add_parser('classify', help='Apply model to other_water residual')
    sub.add_parser('compare', help='Compare transformer vs second-coder labels')

    args = parser.parse_args()
    if args.command == 'prepare':
        prepare(args)
    elif args.command == 'train':
        train(args)
    elif args.command == 'classify':
        classify(args)
    elif args.command == 'compare':
        compare(args)
    else:
        parser.print_help()
