#!/usr/bin/env python3
"""检查资产层文件、Markdown 元数据、相对链接、JSON、图片、重复哈希与路径长度。"""
from pathlib import Path
import argparse, collections, hashlib, json, re, os

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('root',nargs='?',default='.')
    ap.add_argument('--windows-prefix',default='')
    ap.add_argument('--output',default='资产健康检查结果.json')
    args=ap.parse_args(); root=Path(args.root).resolve()
    files=[p for p in root.rglob('*') if p.is_file()]
    mds=[p for p in files if p.suffix.lower()=='.md']
    missing=[]; relative_broken=[]; json_errors=[]
    required=['title','status','maturity','tags','created','updated','summary']
    for p in mds:
        t=p.read_text('utf-8',errors='replace')
        fm={}
        if t.startswith('---\n') and '\n---\n' in t[4:]:
            head=t[4:t.find('\n---\n',4)]
            for line in head.splitlines():
                if ':' in line and not line.startswith(' '): fm[line.split(':',1)[0].strip()]=line.split(':',1)[1].strip()
        for k in required:
            if not fm.get(k): missing.append({'path':str(p.relative_to(root)),'field':k})
        for target in re.findall(r'!?(?:\[[^\]]*\])\((?:<)?([^)>]+)(?:>)?\)',t):
            if '://' in target or target.startswith('#'): continue
            target=target.split('#',1)[0]
            if target and not (p.parent/target).resolve().exists(): relative_broken.append({'path':str(p.relative_to(root)),'target':target})
    for p in files:
        if p.suffix.lower()=='.json':
            try: json.loads(p.read_text('utf-8'))
            except Exception as e: json_errors.append({'path':str(p.relative_to(root)),'error':str(e)})
    h=collections.defaultdict(list)
    for p in files: h[hashlib.sha256(p.read_bytes()).hexdigest()].append(str(p.relative_to(root)))
    dups=[v for v in h.values() if len(v)>1]
    longest=max(((len(args.windows_prefix+str(p.relative_to(root)).replace('/','\\')),str(p.relative_to(root))) for p in files),default=(0,''))
    result={'root':str(root),'files':len(files),'markdown':len(mds),'missing_metadata':missing,'relative_broken_links':relative_broken,'json_errors':json_errors,'duplicate_groups':dups,'longest_windows_path':{'length':longest[0],'path':longest[1]}}
    Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:(len(v) if isinstance(v,list) else v) for k,v in result.items() if k!='root'},ensure_ascii=False,indent=2))
    return 1 if missing or relative_broken or json_errors else 0
if __name__=='__main__': raise SystemExit(main())
