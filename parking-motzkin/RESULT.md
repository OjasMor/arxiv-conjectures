# Question 5.2 of arXiv:2611.29890: yes, with an explicit Motzkin-number formula

Status as of 2026-11-25: a formula and a written proof, found by GPT-6.2 Astra in one attempt ($0.88). The
formula matches exhaustive enumeration in all 55 cases with n ≤ 10 (separate code). The proof has been read by
Claude and by an AI referee, not by a human mathematician.

## Source

Alexander Clifton, Pamela E. Harris, Maryam Khaqan, "Parking Functions inspired by board games",
arXiv:2611.29890 (math.CO, 23 Nov 2026). In the backgammon parking rule a car takes its preferred spot; if the
spot is occupied, the parked car is bumped back to the start of the street and takes the first free spot.
Out_B(α) is the resulting permutation (car in each spot). The paper proves that the number of preference lists
with outcome n (n−1) ... 1 is the Motzkin number M_n, and gives formulas for k = 1, 2 below. It asks:

> Question 5.2. For fixed k, can |Out_B^(−1)(1 2 ... k n (n−1) ... (k+1))| for n > k be expressed as a sum
> involving Motzkin numbers whose indices depend on n?

## Answer: yes

Let C_j be the Catalan numbers and define polynomials P_0(z) = 1,

    P_(k+1)(z) = z² P_k(z) − z · (C_0 P_k(z) + C_1 P_(k−1)(z) + ... + C_k P_0(z)).

Then for all k ≥ 0 and n > k,

    |Out_B^(−1)(1 2 ... k n (n−1) ... (k+1))|  =  Σ_h [z^h] P_k(z) · M_(n−k+h).

k = 1 and k = 2 give the paper's M_(n+1) − M_n and M_(n+2) − 2M_(n+1) + M_n − M_(n−1). The first new case is

    k = 3:   M_(n+3) − 3M_(n+2) + 3M_(n+1) − 3M_n + 2M_(n−1) − 2M_(n−2).

The proof (in `ASTRA_ATTEMPT.md`) inserts a car that ends in spot 1, tracks the length of the initial run of
distinct preferences, and derives A_(k+1)(m) = A_k(m+2) − Σ_j C_j A_(k−j)(m+1), where A_k(m) is the count with
a decreasing block of length m.

## Verification

- `brute.py` simulates the rule from the paper's definition and counts all outcomes. It reproduces the paper's
  examples (Out_B(1,4,4,3,2,2) = 164325, Out_B(1,3,3,1) = 4231), its table of minimum counts for n ≤ 9, and
  its formulas for k = 0, 1, 2.
- `formula.py` evaluates the formula above. All 55 cases 0 ≤ k < n ≤ 10 match (`log.txt`). For n = 8, 9, 10
  the enumeration merges identical street states, checked against the plain loop for n ≤ 7.
- These scripts were written by a separate agent given the paper's definitions.
- A fresh-context AI referee pass was still running when this was committed.

## Prior work (checked 2026-11-25)

Paper is 2 days old. Nothing in the teen's repository or on GitHub. The authors have not been asked.

Checked on GitHub by repository search (name, description, README) for the arXiv id and keywords, and inside the collection repositories we know of (1337isnot1337/solved-conjectures, s66lem/conjectures, the-omega-institute/trureturing, AmirMakir/broken-conjectures and others); on X by arXiv id; and by web search. Nothing found. This is a search, not a guarantee: several people are working through the same papers this week.
