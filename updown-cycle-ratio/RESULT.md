# Question 7.1 of arXiv:2611.20344: no, a cycle can have 2^l > 3^(a+1)

Status as of 2026-11-25: an explicit cycle of length 149, found by GPT-6.2 Astra in one attempt ($1.19) and
re-checked with our own code. A finite object anyone can verify in a second. Not reviewed by a human.

## Source

Oleg Vasilyev, "Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph",
arXiv:2611.20344 (cs.DM, 16 Nov 2026). T_S sends x to ⌈3x/2⌉ if x is in S and to ⌈x/2⌉ otherwise. A cycle with
l steps, a of them up, always has 2^l > 3^a.

> Question 7.1. Does every cycle satisfy 2^l < 3^(a+1), that is, a = ⌊l log_3 2⌋? This holds for cycles with a
> single run of steps up, for all cycles of length l ≤ 30, and for all 1,133,265,572 cycles whose elements are
> all at most 160; among the latter, the largest ratio 2^l/3^a is 2.398, for l = 71.

## Answer: no

Start at 2 and take runs of steps up, down, up, down, ... of lengths

    12,1,2,1,2,1,2,1,1,1,2,3,1,3,9,1,2,1,1,2,4,4,6,1,2,2,1,1,4,2,3,2,2,2,1,2,2,1,6,1,1,5,6,1,3,2,6,2,3,2,
    1,1,2,1,1,1,4,1,1,7

This visits 149 distinct integers (the smallest is 2, the largest 458) and returns to 2, so it is a cycle of
T_S for S = the 93 numbers where it steps up. It has l = 149, a = 93, and

    2^149 = 713623846352979940529142984724747568191373312  >  706965049015104706497203195837614914543357369 = 3^94.

The ratio 2^l/3^a is about 3.028.

## Verification

- `verify.py` (our code, exact integers): rebuilds the cycle, checks the 149 vertices are distinct, that it
  closes, replays it as the map T_S, and compares 2^l with 3^(a+1).
- `ASTRA_ATTEMPT.md`: the model output, which also reproduces the paper's cycle counts for l = 2, 5, 8, 10.
- The paper's second part of the question (what is the supremum of the ratio?) is not answered here.

## Prior work (checked 2026-11-25)

GitHub repository search, the collection repositories we know of, and X by arXiv id: nothing found. The author
has not been asked.
