import json,base64,glob,os,sys
src="C:/Users/junio/.claude/projects/C--Users-junio--claude/bd0496f7-9d55-4751-ad1e-04410e79b921/tool-results"
dst=os.path.join(os.path.dirname(os.path.abspath(__file__)),"pdfs")
for f in glob.glob(os.path.join(src,"*download_file_content*.txt")):
    d=json.load(open(f,encoding="utf-8"))
    out=os.path.join(dst,d["title"])
    if os.path.exists(out): continue
    data=base64.b64decode(d["content"])
    if data[:4]!=b"%PDF":
        print("SKIP non-PDF:",d["title"],data[:15]); continue
    open(out,"wb").write(data); print("wrote",d["title"],len(data))
print("total pdfs:",len(os.listdir(dst)))
