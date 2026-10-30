"""Offline HTML inventory. No network access or JavaScript execution."""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path

class Inventory(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.result = {'titles': [], 'headings': [], 'meta': [], 'canonicals': [], 'links': [], 'images': [], 'json_ld': []}
        self.capture = None
        self.buffer = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'title' or tag in {'h1','h2','h3','h4','h5','h6'}:
            self.capture, self.buffer = tag, []
        if tag == 'script' and a.get('type','').lower().split(';')[0].strip() == 'application/ld+json':
            self.capture, self.buffer = 'json_ld', []
        if tag == 'meta':
            self.result['meta'].append(a)
        if tag == 'link' and 'canonical' in a.get('rel','').lower().split():
            self.result['canonicals'].append(a.get('href'))
        if tag == 'a' and 'href' in a:
            self.result['links'].append(a['href'])
        if tag == 'img':
            self.result['images'].append(a)

    def handle_data(self, data):
        if self.capture:
            self.buffer.append(data)

    def handle_endtag(self, tag):
        if not self.capture or not (tag == self.capture or (tag == 'script' and self.capture == 'json_ld')):
            return
        value = ''.join(self.buffer)
        if self.capture == 'json_ld':
            try:
                parsed = json.loads(value)
                item = {'syntax_valid': True, 'value': parsed}
            except (ValueError, RecursionError) as exc:
                item = {'syntax_valid': False, 'error': str(exc)}
            self.result['json_ld'].append(item)
        elif tag == 'title':
            self.result['titles'].append(' '.join(value.split()))
        else:
            self.result['headings'].append({'level': tag, 'text': ' '.join(value.split())})
        self.capture, self.buffer = None, []

def inspect_html(text):
    parser = Inventory()
    parser.feed(text)
    parser.close()
    return {'evidence_type': 'offline_html_snapshot', 'limitations': ['No HTTP status or response headers', 'No JavaScript rendering', 'JSON-LD syntax only; no vocabulary or rich-result validation'], **parser.result}

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('file', type=Path)
    args = ap.parse_args()
    print(json.dumps(inspect_html(args.file.read_text(encoding='utf-8-sig')), indent=2, ensure_ascii=False))
