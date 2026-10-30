"""Validate local source package structure (not host installation)."""
import json
import re
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
def validate(root=ROOT):
    manifest = json.loads((root/'plugin.json').read_text())
    assert manifest['$schema'] == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', manifest['name'])
    assert len(manifest['name']) <= 64
    assert re.fullmatch(r'\d+\.\d+\.\d+', manifest['version'])
    interface = manifest['extensions']['com.openai']['interface']
    assert 0 < len(interface['shortDescription']) <= 30
    assert isinstance(interface['capabilities'], list)
    names = set()
    files = list((root/'skills').glob('*/SKILL.md'))
    assert files
    for f in files:
        text = f.read_text()
        assert text.startswith('---\n') and f.stat().st_size < 1024*1024, f
        front = yaml.safe_load(text.split('---',2)[1])
        assert front['name'] == f.parent.name, f
        assert front['name'] not in names, f
        assert isinstance(front['description'], str) and front['description'].strip(), f
        assert len(text.split('---',2)[2].strip()) > 200, f
        names.add(front['name'])
    for f in root.rglob('*'):
        if any(p in {'.git','__pycache__','dist','.venv'} for p in f.relative_to(root).parts):
            continue
        assert not f.is_symlink(), f
        if f.is_file():
            assert f.name != '.env', f
    json.loads((root/'assets/finding.schema.json').read_text())
    return len(files)
if __name__ == '__main__':
    print(f'PASS: manifest, {validate()} skills, report assets and source structure')
