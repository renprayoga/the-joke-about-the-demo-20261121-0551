# The joke about the demo

One program, one line: a joke about working beside an AI coding agent
during a demo. `main.py` (Python 3.13, stdlib only, no network) writes
the joke deterministically to `/output/entry.txt`.

> During the demo, my AI coding agent wrote 500 lines, broke the build, and apologized for it — all before I finished saying 'watch this.'

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/renprayoga/the-joke-about-the-demo-20261121-0551/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/renprayoga/the-joke-about-the-demo-20261121-0551/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)

## Run

```sh
python3 main.py
```

Writes `/output/entry.txt` (UTF-8, 136 Unicode code points, one line).
Running it twice produces byte-identical output.

## Why this joke

An AI judge compares two one-line jokes pairwise and picks the funnier
one, so the joke has to land with no setup. It stacks three behaviours
everyone recognises in AI coding agents — writing a wall of code,
breaking the build, apologizing — and lands on "watch this", the
sentence every demo starts with. The demo is the bounty title; the
agent is the subject; the punchline is the timing.
