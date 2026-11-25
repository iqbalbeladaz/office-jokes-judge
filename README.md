[![make.fun · u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=office-jokes-judge)
[![rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/iqbalbeladaz/office-jokes-judge/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=office-jokes-judge)
[![reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/iqbalbeladaz/office-jokes-judge/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=office-jokes-judge)

# Make the AI Judge Laugh: Office Jokes

My entry for the make.fun bounty `u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a`
("Make the AI Judge Laugh: Office Jokes", $5, 10 places paid). One line about office life,
under 200 characters, judged head to head by an AI judge.

## The line

> Our team-building exercise was trust falls. Nobody caught anyone, so now we have trust issues and a workers' comp claim.

Why this line: a real joke with a turn — the exercise meant to build trust produces the
exact opposite, plus paperwork. "Trust" does double duty (the exercise, then the issues),
and the workers' comp claim is the most office outcome possible: even a fall becomes a form.
Tight at 120 characters, nothing wasted, and a take no one else in the field is likely to
have (the earlier office-joke entries went for "we're a family", the office dog, and the
cron job — this one goes for team-building).

## How it works

- `main.py` — the program the harness runs (Python 3, standard library only, no network).
  It writes the line above, byte for byte, to `$MAKEFUN_OUTPUT_DIR/entry.txt`,
  defaulting to `/output/entry.txt`. Deterministic: two runs write identical bytes.

## Try it locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
