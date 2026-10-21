import copy,json,sys,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R))
from catalog import validate,markdown
class CatalogTests(unittest.TestCase):
 def sample(self):return json.loads((R/'projects.json').read_text())
 def test_canonical_catalog(self):self.assertEqual(len(validate(self.sample())),5)
 def test_duplicate_slug_rejected(self):
  p=self.sample();p.append(copy.deepcopy(p[0]))
  with self.assertRaises(ValueError):validate(p)
 def test_offsite_source_rejected(self):
  p=self.sample();p[0]['source']='https://example.com/phishing'
  with self.assertRaises(ValueError):validate(p)
 def test_slug_and_destination_agree(self):
  p=self.sample();p[0]['live']='https://m-qazi99.github.io/not-this-project/'
  with self.assertRaises(ValueError):validate(p)
 def test_markdown_has_all_live_products(self):
  p=self.sample();text=markdown(validate(p))
  for item in p:self.assertIn(item['live'],text)
if __name__=='__main__':unittest.main()
