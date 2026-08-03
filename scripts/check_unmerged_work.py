#!/usr/bin/env python3
"""
Fail loudly if work is stranded outside main.

WHY THIS EXISTS
---------------
On 2026-08-03 we found that this repository had been forked in two since
2026-07-22: `main` and `claude/project-status-briefing-0528tx` had each
accumulated ~25 commits, invisible to one another, duplicating the same bug
fixes while each missed the other's real work. Nobody noticed for 12 days,
because nothing was watching.

The user's instruction after that: branches for testing are fine, but work
must never again sit unmerged and unnoticed. They don't write the code, so
they can't be the one to catch it. This script is that check.

It is deliberately noisy about uncommitted work too, since the other half of
the same failure is a sweep that produces files and never commits them.

Exit codes:
    0  clean - everything is on main and pushed
    1  something is stranded (details printed)

Run it at the end of every sweep, and any time you finish a piece of work.
"""

import subprocess
import sys

# Branches that are allowed to exist without being merged.
IGNORED = {"main", "master", "HEAD"}
# A branch younger than this is presumably still being worked on.
STALE_DAYS = 2


def git(*args):
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, check=False
    ).stdout.strip()


def main():
    problems = []

    # 1. Uncommitted changes in the working tree.
    dirty = git("status", "--porcelain")
    if dirty:
        n = len(dirty.splitlines())
        problems.append(
            f"{n} uncommitted change(s) in the working tree.\n"
            f"    Fix: git add -A && git commit && git push"
        )

    # 2. Commits on main that were never pushed.
    ahead = git("rev-list", "--count", "@{upstream}..HEAD") or "0"
    if ahead.isdigit() and int(ahead) > 0:
        problems.append(
            f"{ahead} commit(s) on the current branch are not pushed.\n"
            f"    Fix: git push -u origin HEAD"
        )

    # 3. Any other branch, local or remote, holding commits main doesn't have.
    branches = git("for-each-ref", "--format=%(refname:short)|%(committerdate:relative)",
                   "refs/heads", "refs/remotes/origin").splitlines()
    for entry in branches:
        if "|" not in entry:
            continue
        name, when = entry.split("|", 1)
        short = name.replace("origin/", "")
        if short in IGNORED or not short:
            continue
        unmerged = git("rev-list", "--count", f"main..{name}")
        if unmerged.isdigit() and int(unmerged) > 0:
            problems.append(
                f"branch '{name}' has {unmerged} commit(s) not in main "
                f"(last commit {when}).\n"
                f"    This is exactly the 2026-08-03 failure. Either merge it:\n"
                f"      git merge {name}\n"
                f"    or delete it if the work is genuinely dead."
            )

    if problems:
        print("UNMERGED OR UNCOMMITTED WORK FOUND\n")
        for i, p in enumerate(problems, 1):
            print(f"  {i}. {p}\n")
        print("Nothing here is lost yet - but it is invisible to the next")
        print("session, which is how the last fork went unnoticed for 12 days.")
        return 1

    print("Clean: no stranded branches, nothing uncommitted, nothing unpushed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
