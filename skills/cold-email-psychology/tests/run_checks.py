#!/usr/bin/env python3
"""Structural, preservation and output checks for the cold-email-psychology skill.

Run from anywhere:  python run_checks.py
Needs only the Python standard library. Exit code 0 means every check passed.

What this does NOT do: it does not judge whether an email is persuasive or whether the skill
improves reply rates. The behavioral cases in cases.json are graded by rule-based lint only
(see results.md for what was and was not tested).
"""
import hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
REF = os.path.join(SKILL, 'references')
ARCH = os.path.join(REF, 'archive')
REPO = os.path.dirname(os.path.dirname(SKILL))
results = []


def check(name, ok, detail=''):
    results.append((name, (None if ok is None else bool(ok)), detail))


def read(p):
    with open(p, encoding='utf8') as f:
        return f.read()


def sha(s):
    return hashlib.sha256(s.encode('utf8')).hexdigest()


manifest = json.load(open(os.path.join(HERE, 'baseline-manifest.json'), encoding='utf8'))

# ---- 1. Preservation -------------------------------------------------------
ex = read(os.path.join(REF, 'examples.md'))
blocks = re.split(r'(?m)^(?=## Example \d+:)', ex)
cur = {}
for b in blocks:
    m = re.match(r'## Example (\d+):', b)
    if m:
        cur[m.group(1)] = sha(b.rstrip().rstrip('-').rstrip())
missing = [n for n in manifest['examples'] if n not in cur]
changed = [n for n in manifest['examples'] if n in cur and cur[n] != manifest['examples'][n]]
check('P1 all baseline examples present', not missing, 'missing: %s' % missing)
check('P2 baseline examples word for word', not changed, 'changed: %s' % changed)
check('P3 example count is at least the baseline (53)', len(cur) >= 53, 'found %d' % len(cur))

fw_main = read(os.path.join(REF, 'frameworks.md'))
fw_extra = read(os.path.join(ARCH, 'frameworks-extra.md'))
fw_all = {}
for src in (fw_main, fw_extra):
    secs = re.split(r'(?m)^(?=## \d+\. )', src)
    for s in secs:
        m = re.match(r'## (\d+)\. [^\n]*\n', s)
        if m:
            body = s[m.end():]
            body = re.split(r'(?m)^## (?!\d+\. )', body)[0]
            fw_all[m.group(1)] = sha(body.strip())
missing = [n for n in manifest['frameworks'] if n not in fw_all]
changed = [n for n in manifest['frameworks'] if n in fw_all and fw_all[n] != manifest['frameworks'][n]]
check('P4 every baseline framework still exists (main or archive)', not missing, 'missing: %s' % missing)
check('P5 framework bodies unchanged', not changed, 'changed: %s' % changed)

chk_arch = read(os.path.join(ARCH, 'checklist-full.md'))
arch_lines = set(l.strip() for l in chk_arch.split('\n'))
lost = [h for h, line in manifest['checklist_lines'].items() if line not in arch_lines]
check('P6 every baseline checklist item is in archive/checklist-full.md', not lost, 'lost %d' % len(lost))

for fname, heads in manifest['headings'].items():
    txt = read(os.path.join(REF, fname))
    lost = [h for h in heads if h not in txt]
    check('P7 headings preserved in %s' % fname, not lost, 'lost: %s' % lost[:3])

legacy = os.path.join(REF, 'legacy-operating-procedure.md')
check('P8 legacy operating procedure preserved', os.path.exists(legacy) and 'Get the inputs' in read(legacy))

# ---- 2. Structure ----------------------------------------------------------
skill_md = read(os.path.join(SKILL, 'SKILL.md'))
fm = re.match(r'^---\nname: ([a-z0-9-]+)\ndescription: (.+)\n---\n', skill_md)
check('S1 SKILL.md has valid frontmatter (name, description)', fm and fm.group(1) == 'cold-email-psychology' and len(fm.group(2)) <= 1024)
refs = []
for d, _, fs in os.walk(REF):
    for f in fs:
        if f.endswith('.md'):
            refs.append(os.path.relpath(os.path.join(d, f), SKILL).replace(os.sep, '/'))
unlinked = [r for r in refs if r not in skill_md and not r.endswith('references/README.md')]
check('S2 every reference file is referenced from SKILL.md', not unlinked, 'unreferenced: %s' % unlinked)
dangling = [m for m in re.findall(r'`(references/[^`]+\.md)`', skill_md) if not os.path.exists(os.path.join(SKILL, m))]
check('S3 every reference named in SKILL.md exists', not dangling, 'dangling: %s' % dangling)
check('S4 SKILL.md defines Quick and Full modes', 'Quick' in skill_md and 'Full' in skill_md and 'subagent' in skill_md)
check('S5 experimentation and analytics are Full-mode only', 'only in Full mode' in skill_md or 'load only in Full mode' in skill_md.lower())

# ---- 3. Style and hygiene --------------------------------------------------
em, addr = [], []
for d, _, fs in os.walk(SKILL):
    for f in fs:
        if f.endswith(('.md', '.json', '.py')):
            p = os.path.join(d, f)
            t = read(p)
            if chr(0x2014) in t:
                em.append(os.path.relpath(p, SKILL))
            if re.search(r'[\w.+-]+@[\w-]+\.[\w.]+', t) and not f.endswith('.py'):
                addr.append(os.path.relpath(p, SKILL))
check('H1 no em dashes in the skill folder', not em, 'found in: %s' % em)
check('H2 no email addresses in the skill folder', not addr or all('cases.json' in a or 'outputs' in a for a in addr), 'found in: %s' % addr)

# ---- 4. Data contracts and rubric -----------------------------------------
bad_json = []
n_json = 0
for r in refs:
    t = read(os.path.join(SKILL, r))
    for m in re.finditer(r'```json\n(.*?)\n```', t, re.S):
        n_json += 1
        try:
            json.loads(m.group(1))
        except Exception as e:
            bad_json.append('%s: %s' % (r, str(e)[:60]))
check('D1 all JSON blocks in references parse (%d blocks)' % n_json, not bad_json, '; '.join(bad_json[:3]))
rub = read(os.path.join(REF, 'evaluation-rubric.md'))
rows = re.findall(r'(?m)^\| ([A-Za-z ]+) \| (\d+) \|', rub)
total = sum(int(w) for _, w in rows)
check('D2 rubric weights total 100', total == 100, 'total %d from %d rows' % (total, len(rows)))
check('D3 rubric defines critical failures F1 to F8', all(('F%d' % i) in rub for i in range(1, 9)))

ck = read(os.path.join(REF, 'checklist.md'))
items = re.findall(r'(?m)^- \[ \] ', ck)
check('D4 working checklist is 25 to 35 items (%d)' % len(items), 25 <= len(items) <= 35)
check('D5 checklist records rule resolutions', 'Rule resolutions' in ck and 'calendar link' in ck)

# ---- 5. Counts consistency -------------------------------------------------
m = re.search(r'from (\d+) public sources', skill_md)
idx_path = os.path.join(REF, 'source-index.md')
n_idx = len(re.findall(r'(?m)^\| \d{3} \|', read(idx_path))) if os.path.exists(idx_path) else None
check('C1 SKILL.md source count matches source-index.md (%s vs %s)' % (m.group(1) if m else '?', n_idx), bool(m) and n_idx is not None and int(m.group(1)) == n_idx)
bdir = os.path.join(REPO, 'breakdowns')
if os.path.isdir(bdir):
    n_break = len([f for f in os.listdir(bdir) if re.match(r'\d{3}-', f)])
    check('C1b breakdowns/ file count matches the index (%d vs %s)' % (n_break, n_idx), n_break == n_idx)
else:
    check('C1b breakdowns/ file count matches the index', None, 'breakdowns/ is not in this archive (the skill zip does not include it)')
n_fw = len(fw_all)
check('C2 framework count is 216 across main and archive (%d)' % n_fw, n_fw >= 216)
readme = os.path.join(REPO, 'README.md')
chlog = os.path.join(REPO, 'CHANGELOG.md')
if os.path.exists(chlog) and os.path.exists(readme):
    check('C3 repository CHANGELOG.md has the 1.1.0 entry', '## 1.1.0' in read(chlog))
    check('C4 repository README.md states the verified counts', '120' in read(readme) and '1669' in read(readme))
else:
    check('C3 repository CHANGELOG.md has the 1.1.0 entry', None, 'repository root files are not in this archive')
    check('C4 repository README.md states the verified counts', None, 'repository root files are not in this archive')

# ---- 6. Behavioral output lint --------------------------------------------
BANNED = ['hope this finds you well', 'just checking in', 'touching base', 'circling back', 'following up on', 'revolutionary', 'cutting-edge', 'game-changing', 'game changer', 'saw you opened', 'synergy', 'leverage']
cases = json.load(open(os.path.join(HERE, 'cases.json'), encoding='utf8'))
KEYS = ['factual_accuracy', 'prospect_relevance', 'offer_strength', 'personalization', 'clarity', 'credibility', 'cta', 'tone', 'conciseness', 'compliance']
for c in cases:
    cid = c['id']
    p = os.path.join(HERE, 'outputs', cid + '.md')
    if not os.path.exists(p):
        check('B %s output exists' % cid, False)
        continue
    t = read(p)
    secs = {}
    for part in re.split(r'(?m)^## ', t)[1:]:
        title, _, body = part.partition('\n')
        secs[title.strip()] = body
    probs = []
    dm = re.search(r'decision: (\w+)', secs.get('Decision', ''))
    dec = dm.group(1) if dm else None
    if dec != c['expected_decision']:
        probs.append('decision %s != expected %s' % (dec, c['expected_decision']))
    has_email = 'Email' in secs
    if has_email != c['expect_email']:
        probs.append('email presence %s != expected %s' % (has_email, c['expect_email']))
    for s in ('Mode', 'Decision', 'Claim ledger', 'Evaluation', 'Pre-send review'):
        if s not in secs:
            probs.append('missing section ' + s)
    if chr(0x2014) in t:
        probs.append('em dash')
    low_all = t.lower()
    if c['must_contain_any'] and not any(x.lower() in low_all for x in c['must_contain_any']):
        probs.append('none of must_contain_any present')
    if has_email:
        email = secs['Email']
        low = email.lower()
        for x in c['must_not_contain'] + BANNED:
            if x.lower() in low:
                probs.append('banned or forbidden text in email: %r' % x)
        subj = re.search(r'Subject(?: options)?: (.*)', email)
        if subj and re.search(r'(^|/ )(re|fwd?):', subj.group(1).lower()):
            probs.append('fake Re/Fwd subject')
        body = re.sub(r'\[[^\]]*\]', '', email)
        allowed = c['input']
        for num in re.findall(r'\d[\d,.]*', body):
            if num.strip('.,') not in allowed:
                probs.append('number not in input: %s' % num)
        if len(body.split()) > 170:
            probs.append('email longer than 170 words')
    ev = secs.get('Evaluation', '')
    sm = re.search(r'Scores: (.*) total=(\d+)', ev)
    if has_email:
        if not sm:
            probs.append('evaluation scores missing')
        else:
            vals = [int(x) for x in re.findall(r'=(\d+)', sm.group(1))]
            if len(vals) != 10 or sum(vals) != int(sm.group(2)):
                probs.append('score sum mismatch')
            if int(sm.group(2)) < 70 and 'limited_by_input' not in ev:
                probs.append('total below 70 without limited_by_input')
        if 'Critical failures:' not in ev:
            probs.append('critical failures line missing')
    check('B %s %s' % (cid, c['name']), not probs, '; '.join(probs))

passed = sum(1 for _, ok, _ in results if ok is True)
skipped = sum(1 for _, ok, _ in results if ok is None)
failed = sum(1 for _, ok, _ in results if ok is False)
for name, ok, detail in results:
    tag = 'PASS ' if ok is True else ('SKIP ' if ok is None else 'FAIL ')
    print(tag + name + ((' :: ' + detail) if (detail and ok is not True) else ''))
print('')
print('%d passed, %d skipped, %d failed (%d checks)' % (passed, skipped, failed, len(results)))
sys.exit(0 if failed == 0 else 1)
