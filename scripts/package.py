"""Build a portable skills-only plugin archive from validated source."""
from pathlib import Path
import zipfile
from validate_package import ROOT, validate

if __name__ == '__main__':
    validate()
    dest = ROOT/'dist'/'seoforge-0.1.0-plugin.zip'
    dest.parent.mkdir(exist_ok=True)
    paths = [ROOT/'plugin.json']
    for folder in ('skills','assets'):
        paths.extend(f for f in (ROOT/folder).rglob('*') if f.is_file())
    # Skill workflows can call the offline helper; include only its runtime script.
    paths.append(ROOT/'scripts/inspect_html.py')
    with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in sorted(paths):
            z.write(f, f.relative_to(ROOT))
    with zipfile.ZipFile(dest) as z:
        assert z.testzip() is None
        assert 'plugin.json' in z.namelist()
        assert len([n for n in z.namelist() if n.endswith('/SKILL.md')]) == 20
    print(dest)
