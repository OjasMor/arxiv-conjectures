import Mathlib

/-!
# The close-skew set-pair bound follows from the skew set-pair bound

Conjecture 5.9 of S. Selvaraja, "Collapsibility of Vietoris–Rips complexes of hypercube graphs in
codimension two" (arXiv:2611.20820), follows from the skew Hamming set-pair theorem of Gao and Zhao
(arXiv:2607.17261), which is taken here as the hypothesis `SkewBound`.

Points of the hypercube are functions `Fin n → Bool` and the distance is `hammingDist`.
-/

namespace CloseSkew

/-- The Gao–Zhao bound (Hypothesis `(S_r)` of arXiv:2611.20820): pairs `(a i, b i)` with
`d (a i) (b i) ≥ r + 1` and `d (a i) (b j) ≤ r` for `i < j` number at most `2 ^ (r + 1)`. -/
def SkewBound (n r : ℕ) : Prop :=
  ∀ (m : ℕ) (a b : Fin m → (Fin n → Bool)),
    (∀ i, r + 1 ≤ hammingDist (a i) (b i)) →
    (∀ i j, i < j → hammingDist (a i) (b j) ≤ r) →
    m ≤ 2 ^ (r + 1)

/-- Conjecture 5.9 of arXiv:2611.20820, assuming the Gao–Zhao bound: if the `v i` are pairwise within
distance `r`, each `w i` is at distance at least `r + 1` from `v i` and within distance `r` of every
earlier `v j`, then there are at most `2 ^ r` of them. -/
theorem closeSkew_of_skew {n r : ℕ} (hS : SkewBound n r)
    (k : ℕ) (v w : Fin k → (Fin n → Bool))
    (hvv : ∀ i j, hammingDist (v i) (v j) ≤ r)
    (hwv : ∀ i, r + 1 ≤ hammingDist (w i) (v i))
    (hlt : ∀ i j, j < i → hammingDist (w i) (v j) ≤ r) :
    k ≤ 2 ^ r := by
  -- the doubled list (v_1,w_1),…,(v_k,w_k),(w_k,v_k),…,(w_1,v_1)
  let a : Fin (k + k) → (Fin n → Bool) := fun t =>
    if h : t.val < k then v ⟨t.val, h⟩ else w ⟨k + k - 1 - t.val, by have := t.isLt; omega⟩
  let b : Fin (k + k) → (Fin n → Bool) := fun t =>
    if h : t.val < k then w ⟨t.val, h⟩ else v ⟨k + k - 1 - t.val, by have := t.isLt; omega⟩
  have key : k + k ≤ 2 ^ (r + 1) := by
    apply hS (k + k) a b
    · intro i
      by_cases h : i.val < k
      · simp only [a, b, h, ↓reduceDIte]
        rw [hammingDist_comm]
        exact hwv _
      · simp only [a, b, h, ↓reduceDIte]
        exact hwv _
    · intro i j hij
      have hij' : i.val < j.val := hij
      by_cases hi : i.val < k
      · by_cases hj : j.val < k
        · simp only [a, b, hi, hj, ↓reduceDIte]
          rw [hammingDist_comm]
          exact hlt _ _ (Fin.mk_lt_mk.mpr hij')
        · simp only [a, b, hi, hj, ↓reduceDIte]
          exact hvv _ _
      · have hj : ¬ j.val < k := by omega
        simp only [a, b, hi, hj, ↓reduceDIte]
        refine hlt _ _ (Fin.mk_lt_mk.mpr ?_)
        have := j.isLt
        omega
  have : k + k ≤ 2 * 2 ^ r := by simpa [pow_succ, mul_comm] using key
  omega

end CloseSkew
