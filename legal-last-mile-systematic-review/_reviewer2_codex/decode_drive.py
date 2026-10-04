"""Decode Drive download_file_content tool-result payloads (saved by Claude Code when a file
exceeds the MCP tool's inline token limit) into real PDFs. The source directory is session- and
machine-specific (Claude Code's own scratch tool-results folder for one conversation), so it is
never hardcoded: pass it as the first argument, or set DRIVE_TOOL_RESULTS_DIR."""
import json,base64,glob,os,sys
src=sys.argv[1] if len(sys.argv)>1 else os.environ.get("DRIVE_TOOL_RESULTS_DIR")
if not src or not os.path.isdir(src):
    sys.exit("usage: python decode_drive.py <tool-results-dir>  (or set DRIVE_TOOL_RESULTS_DIR)\n"
             "the directory must hold Claude Code's own *download_file_content*.txt tool-result files")
dst=os.path.join(os.path.dirname(os.path.abspath(__file__)),"pdfs")
for f in glob.glob(os.path.join(glob.escape(src),"*download_file_content*.txt")):
    d=json.load(open(f,encoding="utf-8"))
    title=os.path.basename(d["title"])
    if not title or title in (".",".."):
        print("SKIP unsafe title:",repr(d["title"])); continue
    out=os.path.join(dst,title)
    if os.path.exists(out): continue
    data=base64.b64decode(d["content"])
    if data[:4]!=b"%PDF":
        print("SKIP non-PDF:",d["title"],data[:15]); continue
    open(out,"wb").write(data); print("wrote",d["title"],len(data))
print("total pdfs:",len(os.listdir(dst)))
