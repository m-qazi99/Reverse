"""Validate and render the first-party project catalog; Python 3.11+, no network."""
import argparse,json,re,sys
from pathlib import Path
from urllib.parse import urlparse

def validate(items):
 if not isinstance(items,list) or not items:raise ValueError('Catalog must be a nonempty array.')
 slugs=set()
 for p in items:
  if not isinstance(p,dict):raise ValueError('Each project must be an object.')
  for key in ['slug','name','purpose','version','keywords','live','source','guide']:
   if key not in p:raise ValueError('Missing field: '+key)
  slug=p['slug']
  if not isinstance(slug,str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',slug) or slug in slugs:raise ValueError('Slugs must be unique lowercase hyphenated names.')
  slugs.add(slug)
  if not re.fullmatch(r'\d+\.\d+\.\d+',p['version']):raise ValueError('Use a three-part version.')
  if not isinstance(p['keywords'],list) or not p['keywords'] or not all(isinstance(x,str) and x.strip() for x in p['keywords']):raise ValueError('Supply descriptive keywords.')
  for field in ['live','source','guide']:
   url=urlparse(p[field])
   if url.scheme!='https' or url.username or url.password or url.hostname not in {'github.com','m-qazi99.github.io'}:raise ValueError('Use canonical public HTTPS links.')
  if p['source']!='https://github.com/m-qazi99/'+slug:raise ValueError('Source URL must match the project slug.')
  if p['live']!='https://m-qazi99.github.io/'+slug+'/':raise ValueError('Live URL must match the project slug.')
 return items

def markdown(items):
 return '| Project | Purpose | Version | Explore |\n|---|---|---|---|\n'+''.join('| '+p['name']+' | '+p['purpose']+' | '+p['version']+' | [Live]('+p['live']+') · [Source]('+p['source']+') · [Guide]('+p['guide']+') |\n' for p in items)

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');parser.add_argument('--format',choices=['json','markdown'],default='markdown');parser.add_argument('--path',type=Path,default=Path(__file__).with_name('projects.json'));args=parser.parse_args()
 try:
  items=validate(json.loads(args.path.read_text()))
  print('PASS: '+str(len(items))+' canonical project records' if args.check else json.dumps(items,indent=2) if args.format=='json' else markdown(items))
 except (OSError,ValueError,TypeError) as e:print('Catalog error: '+str(e),file=sys.stderr);sys.exit(1)
