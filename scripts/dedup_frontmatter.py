"""Remove duplicate top-level front-matter keys from publication pages.

The `academic` Bibtex importer appends a `links:` block to each generated
page, which duplicates any `links:` block already present (e.g. manually
added Shiny-app links). Hugo >= 0.145 errors on duplicate mapping keys,
failing the build. This keeps the FIRST occurrence of each top-level key
and drops subsequent ones. Idempotent: a no-op on already-clean files.
"""
import glob
import re

KEY = re.compile(r"^[A-Za-z0-9_]+:")
changed = 0

for f in glob.glob("content/publication/*/index.md"):
    t = open(f).read()
    if not t.startswith("---"):
        continue
    parts = t.split("---", 2)
    if len(parts) < 3:
        continue
    lines = parts[1].strip("\n").split("\n")
    starts = [(i, ln.split(":", 1)[0]) for i, ln in enumerate(lines) if KEY.match(ln)]
    seen, drop = set(), set()
    for idx, (i, k) in enumerate(starts):
        end = starts[idx + 1][0] if idx + 1 < len(starts) else len(lines)
        if k in seen:
            drop.update(range(i, end))
        seen.add(k)
    if not drop:
        continue
    kept = [ln for i, ln in enumerate(lines) if i not in drop]
    open(f, "w").write("---\n" + "\n".join(kept) + "\n---" + parts[2])
    changed += 1
    print(f"deduped {f}")

print(f"total changed: {changed}")
