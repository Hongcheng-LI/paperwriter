"""Run with Python: test_project_tools.py. All fixtures use temporary directories."""
import json
from pathlib import Path
import tempfile
import unittest
import project_tools as p


class ProjectToolsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve() / 'project'

    def test_idempotent_preserves_user_files(self):
        first = p.initialize(self.root)
        self.assertEqual(first['stage'], 'awaiting_journal_materials')
        self.assertEqual(first['next_message'], '期刊材料已放好')
        self.assertEqual(
            first['input_map']['target_journal_articles'],
            '01_inputs/01_target_journal/reference_articles'
        )
        project = json.loads((self.root / '00_project/project.json').read_text(encoding='utf-8'))
        self.assertEqual(
            project['canonical_manuscript'],
            '05_drafts/merged_manuscript/manuscript.docx'
        )
        state = self.root / '00_project/status.json'
        state.write_text('{"author_decision":"keep"}', encoding='utf-8')
        raw = self.root / '01_inputs/02_research_materials/raw_data_and_results/test.txt'
        raw.write_bytes(b'original')
        result = p.initialize(self.root)
        self.assertEqual(result['created_files'], [])
        self.assertEqual(json.loads(state.read_text())['author_decision'], 'keep')
        self.assertEqual(raw.read_bytes(), b'original')

    def test_collision_preflight(self):
        self.root.mkdir()
        (self.root / '01_inputs').write_text('keep')
        with self.assertRaises(ValueError):
            p.initialize(self.root)
        self.assertFalse((self.root / '00_project').exists())

    def test_path_escape(self):
        with self.assertRaises(ValueError):
            p.safe(self.root, '../outside')

    def test_redirect(self):
        self.root.mkdir()
        outside = Path(self.temp.name) / 'outside'
        outside.mkdir()
        try:
            (self.root / '01_inputs').symlink_to(outside, target_is_directory=True)
        except OSError as exc:
            self.skipTest('Symlink creation unavailable: ' + str(exc))
        with self.assertRaises(ValueError):
            p.initialize(self.root)
        self.assertEqual(list(outside.iterdir()), [])

    def test_inventory_revision_and_scope(self):
        p.initialize(self.root)
        data = self.root / '01_inputs/02_research_materials/raw_data_and_results/a.txt'
        data.write_text('v1')
        def snapshot(scope='research'):
            return json.loads(Path(p.inventory(self.root, scope)['snapshot']).read_text(encoding='utf-8'))
        first = snapshot()['sources'][0]
        self.assertEqual(snapshot('journal')['sources'], [])
        data.write_text('v2')
        revised = snapshot()['sources'][0]
        self.assertEqual(first['source_id'], revised['source_id'])
        self.assertEqual(revised['change'], 'changed')
        data.unlink()
        self.assertEqual(snapshot()['sources'][0]['change'], 'removed')
        data.write_text('v3')
        restored = snapshot()['sources'][0]
        self.assertEqual(first['source_id'], restored['source_id'])
        self.assertEqual(restored['change'], 'restored')

    def test_placeholders(self):
        p.initialize(self.root)
        relative = '05_drafts/merged_manuscript/manuscript.md'
        draft = self.root / relative
        draft.write_text('[PENDING:ISSUE-0001]\nSee Fig. X and [ref].', encoding='utf-8')
        self.assertEqual(len(p.placeholders(self.root, relative)['hits']), 3)
        draft.write_text('A bounded observation.', encoding='utf-8')
        self.assertEqual(p.placeholders(self.root, relative)['hits'], [])
        with self.assertRaises(ValueError):
            p.placeholders(self.root, 'example.docx')


if __name__ == '__main__':
    unittest.main(verbosity=2)
