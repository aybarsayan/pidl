# MATEMATİKSEL KANITLAR VE TÜREVLER

## THEOREM 1: Dual-Mode Optimality

**İddia:** Dual-mode sistemi, her kullanıcı profili için en az bir optimal persona garanti eder.

**Kanıt:**

Verilsin:
- \( U = \{u_1, u_2, ..., u_n\} \): Kullanıcı uzayı
- \( P = \{p_1, p_2, ..., p_m\} \): Persona kümesi
- \( P = P_{tech} \cup P_{edu} \), \( P_{tech} \cap P_{edu} = \emptyset \)

Her \( u \in U \) için:

**Case 1:** \( s_T(u) > s_E(u) \) (Technical dominant)

Similarity mode:
\[
p^*_{sim} = \arg\max_{p \in P_{tech}} R_{sim}(u,p)
\]

Complementary mode:
\[
p^*_{comp} = \arg\max_{p \in P_{edu}} R_{comp}(u,p)
\]

**Case 2:** \( s_E(u) > s_T(u) \) (Educational dominant)

Similarity mode:
\[
p^*_{sim} = \arg\max_{p \in P_{edu}} R_{sim}(u,p)
\]

Complementary mode:
\[
p^*_{comp} = \arg\max_{p \in P_{tech}} R_{comp}(u,p)
\]

Her iki durumda da:
- Similarity: Aynı kategoriden optimal
- Complementary: Karşı kategoriden optimal

\( \therefore \) En az 2 optimal persona garanti edilir.

\( \square \)

---

## LEMMA 1: Similarity Monotonicity

**İddia:** Similarity skoru, kullanıcı-persona vektör yakınlığı ile monoton artar.

\[
d(\vec{u}, \vec{p}_1) < d(\vec{u}, \vec{p}_2) \implies S(u, p_1) > S(u, p_2)
\]

**Kanıt:**

\[
S(u,p) = w_1 \cos(\vec{u}, \vec{p}) + w_2(1 - \frac{d_{euc}}{d_{max}})
\]

Hem cosine hem Euclidean uzaklıkla monoton. \( \square \)

---

## PROPOSITION 1: Complementarity Bounds

\[
0 \leq D(u,p) \leq 1
\]

**Kanıt:** Max fonksiyonu ve normalizasyon. \( \square \)

---

## COROLLARY 1: Adaptive Mode Continuity

Adaptive mode, \( g \) (learning goal) parametresinde süreklidir:

\[
\lim_{g \to 0.7^-} R_{adaptive} = \lim_{g \to 0.7^+} R_{adaptive}
\]

**Kanıt:** Linear interpolation. \( \square \)

