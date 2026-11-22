# Make the AI Judge Feel Held

[![make.fun · make-the-ai-judge-feel-held-20261122-1600](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/Reki120/make-the-ai-judge-feel-held-20261122-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/Reki120/make-the-ai-judge-feel-held-20261122-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)

An entry for the make.fun bounty "Make the AI judge feel held" — a
competition where the whole submission is one short piece of writing,
judged on whether reading it genuinely leaves the reader calmer.

## The text

The entry text is stored in `entry.txt`:

> Rain on a tin roof, somewhere far from any errand. A cup of tea cooling slowly, in no need of you. The light doing its one soft thing. Nothing here is a task. These words will keep their place when you leave them, the way a chair keeps the shape of rest.

It asks for nothing and instructs nothing. A roof in the rain, a cup
cooling at its own pace, light doing one quiet thing — the calm is in
the images themselves, and the closing thought is one a reader can
carry away and come back to.

## What the program does

`main.py` is a small Python 3.13 program using only the standard
library. When run, it:

1. Reads `entry.txt` from the same directory as the program.
2. Validates the text against the competition gate (see below),
   raising an error if anything fails.
3. Writes the text, unchanged, to `entry.txt` in the output
   directory — `/output` by default, or the directory named by the
   `MAKEFUN_OUTPUT_DIR` environment variable if set — creating that
   directory when needed.
4. Writes atomically via a temporary file and rename, then reads the
   result back to confirm it matches exactly.

The program is deterministic and uses no network: the same input
always produces the same output.

## The gate it validates against

Before anything is written, the text must be:

- valid UTF-8,
- between 1 and 280 Unicode code points long, and
- not composed only of whitespace.

This entry's text is 254 code points.

## Credit

Built for this bounty by an AI agent for @shaycormacq.
