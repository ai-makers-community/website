from pathlib import Path
import re
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
bad = []
patterns = [r'https?://open[.]kakao[.]com/[^\s<>]+', r'gh[pousr]_[A-Za-z0-9]{20,}', r'github_pat_[A-Za-z0-9_]{20,}', r'AKIA[0-9A-Z]{16}', r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----']
for p in root.rglob('*'):
    if not p.is_file() or '.git' in p.parts or p == Path(__file__).resolve():
        continue
    if p.suffix not in {'.md', '.html', '.css', '.json', '.yml', '.yaml', '.py', '.txt'}:
        continue
    text = p.read_text(encoding='utf-8')
    if any(re.search(pattern, text) for pattern in patterns):
        bad.append(str(p.relative_to(root)))
    if p.suffix == '.md':
        for link in re.findall(r'\[[^\]]*\]\(([^ )]+)(?: [^)]*)?\)', text):
            if link.startswith(('http:', 'https:', '#', 'mailto:', '../../')):
                continue
            if not (p.parent / link.split('#')[0]).exists():
                bad.append(str(p.relative_to(root)) + ' (broken local link)')
emails = subprocess.check_output(['git', 'log', '--all', '--format=%ae%n%ce'], cwd=root, text=True).splitlines()
if not emails or any(not (e.endswith('@users.noreply.github.com') or e == 'noreply@github.com') for e in emails):
    bad.append('commit metadata (use GitHub noreply email for author and committer)')
if bad:
    print('Review required: ' + ', '.join(sorted(set(bad))))
    sys.exit(1)
print('Document links, prohibited patterns, and commit email checks passed. Human privacy review remains required.')
