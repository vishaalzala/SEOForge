import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from inspect_html import inspect_html

class OfflineEvidence(unittest.TestCase):
    def test_metadata_and_nested_heading(self):
        d = inspect_html('<title>A &amp; B</title><h1>Repair <em>guide</em></h1><link rel="CANONICAL alternate" href="https://example.com/a"><meta name="robots" content="noindex"><img src="a.webp" alt=""><a href="/next">Next</a>')
        self.assertEqual(d['titles'], ['A & B'])
        self.assertEqual(d['headings'], [{'level':'h1','text':'Repair guide'}])
        self.assertEqual(d['canonicals'], ['https://example.com/a'])
        self.assertEqual(d['meta'][0]['content'], 'noindex')
        self.assertEqual(d['links'], ['/next'])
        self.assertEqual(d['images'][0]['alt'], '')
    def test_json_syntax_and_limits(self):
        d = inspect_html('<script type="application/ld+json">{"@type":"Product"}</script><script type="application/ld+json">{bad}</script>')
        self.assertTrue(d['json_ld'][0]['syntax_valid'])
        self.assertFalse(d['json_ld'][1]['syntax_valid'])
        self.assertEqual(d['evidence_type'], 'offline_html_snapshot')
        self.assertTrue(d['limitations'])
    def test_missing_data_is_empty(self):
        d = inspect_html('<p>No metadata</p>')
        self.assertEqual(d['titles'], [])
        self.assertEqual(d['canonicals'], [])
if __name__ == '__main__':
    unittest.main()
