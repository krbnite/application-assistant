import json
import sys
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import generate_resume_docx as g
from docx import Document

class GroupedCVBTests(unittest.TestCase):
    def setUp(self):
        self.bank=g.parse_bullet_bank(ROOT/'RESUME_BULLET_BANK.md')
        self.profiles=g.parse_profile_bank(ROOT/'PROFILE_BANK.md')
        self.plan=json.loads((ROOT/'TAILORED_RESUME_PLAN_TEMPLATE.json').read_text())
        self.plan['experience']={'cvb_director':['CVB-04'],'cvb_senior_ds':['CVB-09']}

    def render(self):
        g.validate_plan(self.plan,self.bank,self.profiles)
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'layout.docx'
            g.build_docx(self.plan,self.bank,self.profiles,out)
            return [p.text for p in Document(out).paragraphs]

    def grouped(self):
        self.plan.update(group_cvb_roles_before_bullets=True,cvb_layout_rationale='Spanning projects form a clearer company-wide technical narrative.')

    def test_separate_mode_preserves_chronology(self):
        text=self.render()
        director=next(i for i,t in enumerate(text) if t.startswith('Director of'))
        sleep=next(i for i,t in enumerate(text) if t.startswith('Sleep sensor validation:'))
        senior=next(i for i,t in enumerate(text) if t.startswith('Senior Data Scientist, Early'))
        self.assertLess(director,sleep)
        self.assertLess(sleep,senior)
        self.assertFalse(any(t.startswith('Associate Director') for t in text))

    def test_grouped_legacy_buckets_all_titles_before_bullets(self):
        self.grouped()
        text=self.render()
        titles=[next(i for i,t in enumerate(text) if t.startswith(r.title)) for r in g.ROLE_ORDER if r.key.startswith('cvb_')]
        first=next(i for i,t in enumerate(text) if t.startswith('Sleep sensor validation:'))
        self.assertEqual(titles,sorted(titles))
        self.assertLess(max(titles),first)
        self.assertEqual(sum(t=='Cohen Veterans Bioscience' for t in text),1)

    def test_grouped_company_list_functional_heading_and_wwe(self):
        self.grouped()
        self.plan.update(cvb_functional_description='Research Scientist - Wearable ML & Signal Processing',cvb_group_summary='Wearable modeling and validation.',group_wwe_roles_before_bullets=True)
        self.plan['experience']={'cvb_grouped':['CVB-21','CVB-09'],'wwe_senior_ds':['WWE-03']}
        text=self.render()
        functional=text.index(self.plan['cvb_functional_description'])
        titles=[next(i for i,t in enumerate(text) if t.startswith('Official title: '+r.title)) for r in g.ROLE_ORDER if r.key.startswith('cvb_')]
        self.assertLess(functional,min(titles))
        self.assertLess(max(titles),text.index(self.plan['cvb_group_summary']))
        self.assertEqual(sum(t.startswith('SensorNet reusable') for t in text),1)
        self.assertEqual(sum(t.startswith('Data Scientist | Stamford') for t in text),1)
        for role in [r for r in g.ROLE_ORDER if r.key.startswith('cvb_')]:
            self.assertTrue(any(role.dates in t and role.title in t for t in text))

    def test_invalid_grouped_plans_rejected(self):
        self.grouped()
        cases=[({'cvb_grouped':['CVB-09'],'cvb_director':['CVB-04']},{}),
               ({'cvb_grouped':['WWE-03']},{}),
               ({'cvb_grouped':['CVB-09','CVB-09']},{}),
               ({'cvb_grouped':['CVB-09']},{'group_cvb_roles_before_bullets':False}),
               ({'cvb_grouped':['CVB-09']},{'cvb_layout_rationale':''}),
               ({'cvb_grouped':['CVB-09']},{'role_summaries':{'cvb_director':'Hidden summary'}}),
               ({'cvb_director':['CVB-09']},{})]
        for experience,updates in cases:
            with self.subTest(experience=experience,updates=updates):
                plan=dict(self.plan,experience=experience,**updates)
                with self.assertRaises(ValueError):
                    g.validate_plan(plan,self.bank,self.profiles)

if __name__=='__main__':
    unittest.main()
