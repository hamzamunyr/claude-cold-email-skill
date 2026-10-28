#!/usr/bin/env python3
"""Builds baseline-manifest.json from the pre-upgrade git tag. Needs git and the repository history.
The generated manifest is committed so run_checks.py works without git."""
import hashlib, json, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
TAG = 'pre-upgrade-baseline'
P = 'skills/cold-email-psychology/references/'


def git_show(path):
    return subprocess.run(['git', '-C', REPO, 'show', '%s:%s' % (TAG, path)], capture_output=True, text=True, encoding='utf8', check=True).stdout


def sha(s):
    return hashlib.sha256(s.encode('utf8')).hexdigest()


out = {'baseline_tag': TAG, 'examples': {}, 'frameworks': {}, 'checklist_lines': {}, 'headings': {}}
ex = git_show(P + 'examples.md')
for b in re.split(r'(?m)^(?=## Example \d+:)', ex):
    m = re.match(r'## Example (\d+):', b)
    if m:
        out['examples'][m.group(1)] = sha(b.rstrip().rstrip('-').rstrip())
fw = git_show(P + 'frameworks.md')
for s in re.split(r'(?m)^(?=## \d+\. )', fw):
    m = re.match(r'## (\d+)\. [^\n]*\n', s)
    if m:
        body = re.split(r'(?m)^## (?!\d+\. )', s[m.end():])[0]
        out['frameworks'][m.group(1)] = sha(body.strip())
ck = git_show(P + 'checklist.md')
for line in ck.split('\n'):
    if line.startswith('- [ ] '):
        out['checklist_lines'][sha(line.strip())[:12]] = line.strip()
for f in ['hooks.md', 'ctas.md', 'followups.md', 'practices.md', 'principles.md']:
    t = git_show(P + f)
    out['headings'][f] = [l.strip() for l in t.split('\n') if l.startswith('# ') or l.startswith('## ')]
json.dump(out, open(os.path.join(HERE, 'baseline-manifest.json'), 'w', encoding='utf8'), indent=1)
print({k: len(v) if isinstance(v, (dict, list)) else v for k, v in out.items()})
