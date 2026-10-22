# Security Policy

These rooms are archives you download and unpack on your own machine, so
their safety matters.

## Reporting a vulnerability

Please report security problems privately through GitHub:
**[Report a vulnerability](https://github.com/rk-secops/ctf-challenges/security/advisories/new)**.
Don't open a public issue for these.

In scope:

- A room archive that could harm a player's machine (files written outside
  the room folder, anything that runs on its own, malicious content)
- A problem in `tools/build_room.py`
- Anything in the repository that looks tampered with

Not security issues: an unsolvable step, a typo in a clue, or a rating that
feels off. Those are welcome as regular
[issues](https://github.com/rk-secops/ctf-challenges/issues/new/choose),
spoiler-free.

I'll acknowledge a report within a few days. This is a personal project, so
there's no bug bounty, but credit is gladly given.

## How the rooms are kept safe

- Rooms contain only plain text files, folders and ordinary archives.
  Nothing in them needs to be run.
- Archives are built by `tools/build_room.py`, which only packages plain
  files and folders, with relative paths inside the room folder.
- Room archives are only ever built by the maintainer; pull requests that
  change a `.tar.gz` file aren't merged.
- Every commit to `main` is signed.
