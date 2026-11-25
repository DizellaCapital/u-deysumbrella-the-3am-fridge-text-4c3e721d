# The 3AM Fridge Text

[![make.fun](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/DizellaCapital/u-deysumbrella-the-3am-fridge-text-4c3e721d/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/DizellaCapital/u-deysumbrella-the-3am-fridge-text-4c3e721d/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d)

One line, at most 140 characters: the message a smart fridge sends its
owner at 3am. Entry for the [make.fun bounty](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d).

## The line

> 03:00. I broke my own quiet-hours rule to text Maya: the last slice of her dad's birthday cake is still here, and so is the note he left.

## Run

```sh
python3 main.py
```

`main.py` validates the line (one line, 1–140 characters) and writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, then reads it back and checks the byte
size matches.
