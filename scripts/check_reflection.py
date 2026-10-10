"""Local deterministic aid; never a factual or model behavior certificate."""
def analyze(p):
 if p.get('subject')!='本人' or p.get('consent') is not True:raise ValueError('voluntary self reflection required')
 if any(k in p for k in ('rank','level','境界等级')):raise ValueError('no personality or realm grading')
 if not all(isinstance(p.get(k),str) and p[k].strip() for k in ('action','commitment')):raise ValueError('concrete action and commitment required')
 if not p.get('motives') or any(not isinstance(x,str) or not x.strip() for x in p['motives']):raise ValueError('self-described motives required')
 for e in p['effects']:
  if not all(isinstance(e.get(k),str) and e[k].strip() for k in ('affected','observation','next_check')):raise ValueError('effect observation and follow-up required')
 return {'self_described_motives':p['motives'],'effects_to_recheck':len(p['effects']),'note':'No inference about virtue, actual inner states or psychological status.'}

if __name__=='__main__':
 import json,sys
 print(json.dumps(analyze(json.loads(open(sys.argv[1],encoding='utf-8').read())),ensure_ascii=False,indent=2))
