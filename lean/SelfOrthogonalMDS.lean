import Mathlib

/-!
# A self-orthogonal [18,3] MDS code over F_16

`F16` is `F_2[a]/(a^4 + a + 1)`.  An element is a 4-bit number whose bit `i` is the coefficient
of `a^i`.  Addition is XOR; multiplication is carry-less multiplication reduced modulo the bit
pattern `0b10011` (= `a^4 + a + 1`).
-/

namespace SelfOrthogonalMDS

/-- Carry-less product of two 4-bit numbers (a polynomial of degree at most 6 over F_2). -/
def clmul (a b : Nat) : Nat :=
  (if b.testBit 0 then a else 0) ^^^ (if b.testBit 1 then a <<< 1 else 0) ^^^
  (if b.testBit 2 then a <<< 2 else 0) ^^^ (if b.testBit 3 then a <<< 3 else 0)

/-- Reduction modulo `a^4 + a + 1 = 0b10011`, clearing bits 6, 5, 4 in turn. -/
def reduce (p : Nat) : Nat :=
  let p := if p.testBit 6 then p ^^^ (0b10011 <<< 2) else p
  let p := if p.testBit 5 then p ^^^ (0b10011 <<< 1) else p
  if p.testBit 4 then p ^^^ 0b10011 else p

/-- Multiplication on encodings. -/
def mulN (a b : Nat) : Nat := reduce (clmul a b)

/-- The field with 16 elements, encoded as numbers `0..15`. -/
structure F16 where
  val : Fin 16
  deriving DecidableEq

namespace F16

def equivFin : F16 ≃ Fin 16 where
  toFun := F16.val
  invFun := F16.mk
  left_inv _ := rfl
  right_inv _ := rfl

instance : Fintype F16 := Fintype.ofEquiv (Fin 16) equivFin.symm

instance : Zero F16 := ⟨⟨0⟩⟩
instance : One F16 := ⟨⟨1⟩⟩
instance : Add F16 := ⟨fun a b => ⟨Fin.ofNat 16 (a.val.val ^^^ b.val.val)⟩⟩
instance : Mul F16 := ⟨fun a b => ⟨Fin.ofNat 16 (mulN a.val.val b.val.val)⟩⟩
instance : Neg F16 := ⟨id⟩
instance : Sub F16 := ⟨fun a b => a + b⟩

/-- Inverse is `x ^ 14` (since `x ^ 15 = 1` for `x ≠ 0`); `0⁻¹ = 0`. -/
instance : Inv F16 :=
  ⟨fun x =>
    let x2 := x * x
    let x4 := x2 * x2
    let x8 := x4 * x4
    x8 * x4 * x2⟩

theorem add_assoc' : ∀ a b c : F16, a + b + c = a + (b + c) := by decide +kernel
theorem add_comm' : ∀ a b : F16, a + b = b + a := by decide +kernel
theorem zero_add' : ∀ a : F16, 0 + a = a := by decide +kernel
theorem neg_add' : ∀ a : F16, -a + a = 0 := by decide +kernel
theorem mul_assoc' : ∀ a b c : F16, a * b * c = a * (b * c) := by decide +kernel
theorem mul_comm' : ∀ a b : F16, a * b = b * a := by decide +kernel
theorem one_mul' : ∀ a : F16, 1 * a = a := by decide +kernel
theorem left_distrib' : ∀ a b c : F16, a * (b + c) = a * b + a * c := by decide +kernel
theorem mul_inv' : ∀ a : F16, a ≠ 0 → a * a⁻¹ = 1 := by decide +kernel

instance : CommRing F16 where
  add_assoc := add_assoc'
  zero_add := zero_add'
  add_zero a := by rw [add_comm', zero_add']
  add_comm := add_comm'
  neg_add_cancel := neg_add'
  nsmul := nsmulRec
  zsmul := zsmulRec
  mul_assoc := mul_assoc'
  one_mul := one_mul'
  mul_one a := by rw [mul_comm', one_mul']
  mul_comm := mul_comm'
  left_distrib := left_distrib'
  right_distrib a b c := by rw [mul_comm', left_distrib', mul_comm' c, mul_comm' c]
  zero_mul := by decide +kernel
  mul_zero := by decide +kernel
  sub_eq_add_neg _ _ := rfl

instance : Field F16 where
  exists_pair_ne := ⟨0, 1, by decide +kernel⟩
  mul_inv_cancel := mul_inv'
  inv_zero := by decide +kernel
  nnqsmul := _
  nnqsmul_def := fun _ _ => rfl
  qsmul := _
  qsmul_def := fun _ _ => rfl

theorem card_F16 : Fintype.card F16 = 16 := by
  rw [Fintype.card_congr equivFin]; simp

end F16

open F16

/-- Helper to write an element from its encoding. -/
def e (n : Nat) : F16 := ⟨Fin.ofNat 16 n⟩

/-- The generator matrix, entries in the encoding described above. -/
def Gdata : List (List Nat) :=
  [[14, 12,  3, 12, 10,  1, 11,  2,  2,  7,  1, 11,  5,  5, 11, 11,  0,  0],
   [ 0, 12,  6,  7, 14,  5, 15, 14,  3, 10, 10,  9,  9, 12,  8,  3,  3,  0],
   [ 0, 12, 15,  5,  9,  7,  5,  6,  5,  3, 12,  6, 11, 14,  3,  8,  0,  9]]

def G : Matrix (Fin 3) (Fin 18) F16 :=
  Matrix.of fun i j => e ((Gdata.getD i []).getD j 0)

theorem G_mul_transpose : G * G.transpose = 0 := by decide +kernel

theorem minors_ne_zero : ∀ i j k : Fin 18, i ≠ j → i ≠ k → j ≠ k →
    G 0 i * (G 1 j * G 2 k - G 1 k * G 2 j) - G 0 j * (G 1 i * G 2 k - G 1 k * G 2 i) +
      G 0 k * (G 1 i * G 2 j - G 1 j * G 2 i) ≠ 0 := by
  decide +kernel

theorem selfOrthogonal_MDS_18_3 :
    G * G.transpose = 0 ∧
    ∀ s : Fin 3 → Fin 18, Function.Injective s → (G.submatrix id s).det ≠ 0 := by
  refine ⟨G_mul_transpose, fun s hs => ?_⟩
  rw [Matrix.det_fin_three]
  have h01 : s 0 ≠ s 1 := fun h => by simpa using hs h
  have h02 : s 0 ≠ s 2 := fun h => by simpa using hs h
  have h12 : s 1 ≠ s 2 := fun h => by simpa using hs h
  have := minors_ne_zero (s 0) (s 1) (s 2) h01 h02 h12
  intro h
  apply this
  simp only [Matrix.submatrix_apply, id] at h
  rw [← h]
  ring

end SelfOrthogonalMDS

#print axioms SelfOrthogonalMDS.selfOrthogonal_MDS_18_3
