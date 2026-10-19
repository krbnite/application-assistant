import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import generate_resume_docx as g
from docx import Document


class ResumeBankFieldsTests(unittest.TestCase):
    def test_plain_entry_and_wrapped_lines(self):
        self.assertEqual(g.parse_entry_body('POD-01', 'Built a model\nwith Python.'),
                         ('Built a model with Python.', {}))

    def test_notes_never_become_resume_text(self):
        text, variants = g.parse_entry_body('POD-01', '''#### Resume text

Built a model.

#### Evidence

Private context.

More private context.

#### Boundaries

Do not claim cloud ownership.

#### Selection

Use for sensor roles.

#### Variant: implementation

Implemented the model in C.
''')
        self.assertEqual(text, 'Built a model.')
        self.assertEqual(variants, {'implementation': 'Implemented the model in C.'})

    def test_rejects_ambiguous_or_malformed_content(self):
        for body in ['Built a model.\n\nInternal context.',
                     '#### Evidence\n\nOnly notes.',
                     '#### Resume text\n\nBuilt it.\n\nUnmarked notes.',
                     '#### Resume text\n\nBuilt it.\n\n#### Evidnce\n\nTypo.',
                     '#### Resume text\n\nBuilt it.\n\n#### Resume text\n\nDuplicate.',
                     '#### Resume text\n\nBuilt it.\n\n#### Variant: detailed\n\n']:
            with self.subTest(body=body), self.assertRaisesRegex(ValueError, 'POD-01'):
                g.parse_entry_body('POD-01', body)

    def test_variant_selection_and_existing_overrides(self):
        bank = g.parse_bullet_bank(ROOT / 'RESUME_BULLET_BANK.md')
        self.assertEqual(g.resolve_entry('POD-06', bank).text, bank['POD-06'].text)
        selected = g.resolve_entry({'id': 'POD-06', 'variant': 'implementation'}, bank)
        self.assertTrue(selected.text.startswith('Adapted the production thermal pipeline'))
        self.assertEqual(g.resolve_entry({'id': 'POD-06', 'text': 'Edited wording.'}, bank).text,
                         'Edited wording.')
        for spec in [{'id': 'POD-06', 'variant': 'missing'},
                     {'id': 'POD-06', 'variant': []},
                     {'id': 'POD-06', 'variant': 'implementation', 'text': 'Conflict'},
                     {'label': 'Custom', 'text': 'Words', 'variant': 'detailed'}]:
            with self.subTest(spec=spec), self.assertRaises(ValueError):
                g.resolve_entry(spec, bank)

    def test_real_bank_and_generated_document(self):
        bank = g.parse_bullet_bank(ROOT / 'RESUME_BULLET_BANK.md')
        self.assertEqual(len(bank), 92)
        self.assertEqual({key for key, value in bank.items() if value.variants}, {'POD-06', 'WWE-02'})
        profiles = g.parse_profile_bank(ROOT / 'PROFILE_BANK.md')
        plan = json.loads((ROOT / 'TAILORED_RESUME_PLAN_TEMPLATE.json').read_text())
        plan['experience'] = {}
        plan['project_ids'] = list(bank)
        plan['project_ids'][plan['project_ids'].index('POD-06')] = {'id': 'POD-06', 'variant': 'implementation'}
        plan['project_ids'][plan['project_ids'].index('WWE-02')] = {'id': 'WWE-02', 'variant': 'detailed'}
        g.validate_plan(plan, bank, profiles)
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / 'structural-test.docx'
            g.build_docx(plan, bank, profiles, out)
            text = '\n'.join(p.text for p in Document(out).paragraphs)
        self.assertIn('Adapted the production thermal pipeline', text)
        self.assertIn('delegating Twitter collection to a direct report', text)
        for marker in ['Evidence /', 'Selection guidance:', 'Interview context',
                       'Implementation-focused variant:', 'Attribution /', '####']:
            self.assertNotIn(marker, text)


if __name__ == '__main__':
    unittest.main()
