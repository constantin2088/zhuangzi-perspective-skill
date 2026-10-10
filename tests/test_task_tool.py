import json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from check_reflection import analyze
class TaskToolTests(unittest.TestCase):
 def sample(self):return json.loads((ROOT/'examples/tool-input.json').read_text(encoding='utf-8'))
 def test_multiple_motives_coexist(self):self.assertEqual(len(analyze(self.sample())['self_described_motives']),2)
 def test_other_person_motive_not_inferred(self):
  p=self.sample();p['subject']='员工'
  with self.assertRaises(ValueError):analyze(p)
 def test_no_coerced_reflection(self):
  p=self.sample();p['consent']=False
  with self.assertRaises(ValueError):analyze(p)
 def test_no_realm_grading(self):
  p=self.sample();p['level']=4
  with self.assertRaises(ValueError):analyze(p)
 def test_effect_without_followup_stops(self):
  p=self.sample();p['effects'][0]['next_check']=''
  with self.assertRaises(ValueError):analyze(p)

if __name__=='__main__':unittest.main()
