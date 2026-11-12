# Exact heralded return and the one-mode optimum

Exact return is possible on a success branch even though the failure branch may destroy the catalyst. Infinite Fock support and finite mean energy play different roles.

This page proves the exact construction and the sharp initial-energy budget for one oscillator per party. The [mode-threshold account](mode_threshold.md) treats the existence threshold at any fixed mode count.

## 1. Exact conversion with finite mean energy

Fix $`d\ge2`$ and $`0<s<1`$. Use the decreasing probability sequence

```math
p_1=\frac{1-s}{1-s/d},
\qquad
p_j=\frac{s}{d}p_{\lceil j/d\rceil},
\quad j\ge2,
\tag{1}
```

whose normalization and block formula are proved in [construction](construction.md). Let $`|f_j\rangle`$ denote the ordered $`m`$-mode Fock basis, with photon numbers $`e_j`$, and set

```math
|C_s\rangle
=
\sum_{j\ge1}\sqrt{p_j}\,
|f_j\rangle_A|f_j\rangle_B.
\tag{2}
```

Define the target product spectrum

```math
q_j=\frac1d p_{\lceil j/d\rceil}.
\tag{3}
```

The probability vectors obey

```math
p=(1-s)\delta_1+s q.
\tag{4}
```

Equation (4) is a relation between Schmidt probabilities. The catalyst (2) is a pure state, not a classical mixture.

Alice uses the bounded local filter

```math
K
=
\sqrt{\frac{s}{d}}\,
|f_1\rangle\langle f_1|
+
\sum_{j\ge2}|f_j\rangle\langle f_j|.
\tag{5}
```

Equations (1)–(4) imply $`p_jK_j^2=sq_j`$ for every index. Therefore the filter succeeds with probability exactly $`s`$, and its normalized success state is

```math
|\psi_{\rm suc}\rangle
=
\sum_{j\ge1}\sqrt{q_j}\,
|f_j\rangle_A|f_j\rangle_B.
\tag{6}
```

Both parties apply the local isometry

```math
V|f_j\rangle
=
|f_{\lceil j/d\rceil}\rangle
|(j-1)\bmod d\rangle_T.
\tag{7}
```

Because the quotient and remainder enumerate each pair of indices exactly once,

```math
(V_A\otimes V_B)|\psi_{\rm suc}\rangle
=
|C_s\rangle\otimes|\Phi_d\rangle.
\tag{8}
```

The original catalyst is returned exactly and is decoupled from the target on success. On failure, the state is the product Fock vacuum.

### Local dilation

The map (7) is an isometry from one separable local Hilbert space to its tensor product with the target. One must not assume that it automatically extends to a unitary on catalyst and target alone with a fixed initial target state: its range already fills that output space.

A further local flag supplies a valid unitary dilation. Map the occupied input subspace with target and flag initialized to $`|0,0\rangle`$ onto the range of (7) with flag $`|1\rangle`$. The orthogonal input and output complements are both countably infinite-dimensional, so complete orthonormal bases define a unitary extension. The flag is local and initially unentangled; its state need not be returned in the [model](model.md).

Thus (5)–(8) define an allowed finite-round LOCC protocol on the infinite-dimensional modes. They are not a finite-gate or bounded-work implementation claim.

## 2. When the exact catalyst has finite energy

In Schmidt block $`\ell`$, the total probability is proportional to $`s^\ell`$ and the Fock energies are of order $`d^{\ell/m}`$. Hence

```math
E(C_s)
=
2\sum_{j\ge1}e_jp_j
<\infty
\quad\Longleftrightarrow\quad
s d^{1/m}<1.
\tag{9}
```

The exact construction is therefore finite-energy below $`s_c=d^{-1/m}`$. It has infinite Schmidt rank. Finite truncations give the [finite-support positive-error construction](construction.md).

The converse in [mode threshold](mode_threshold.md) shows that no other pure catalyst or allowed LOCC protocol has exact finite-energy return at or above this success threshold.

## 3. A sharp one-mode bound for every energy budget

For a decreasing Schmidt probability sequence $`p`$, define its index moment

```math
\mu(p)=\sum_{j\ge1}(j-1)p_j
=\sum_{k\ge1}P_k,
\qquad
P_k=\sum_{j>k}p_j.
\tag{10}
```

For one oscillator per party, the initial photon inventory in arbitrary physical Schmidt bases satisfies

```math
E(C)\ge2\mu(p).
\tag{11}
```

Equality holds in matched passive number bases. This is a rearrangement bound; it does not assert that physical energy is monotone under local operations.

For the product spectrum (3), direct summation gives the exact identity

```math
\begin{aligned}
\mu(q)
&=
\frac1d
\sum_{i\ge1}p_i
\sum_{r=1}^{d}\bigl(d(i-1)+r-1\bigr)\\
&=
d\mu(p)+\frac{d-1}{2}.
\end{aligned}
\tag{12}
```

Suppose an arbitrary allowed protocol returns the catalyst and $`|\Phi_d\rangle`$ exactly with success probability at least $`s`$. Average monotonicity of the Schmidt-tail entanglement monotones gives

```math
P_k\ge sQ_k
\quad\text{for every }k.
\tag{13}
```

The same inequality holds with discarded local environments: the exact pure retained target factors from each complete successful branch, and any additional environment entanglement can only enlarge the corresponding Schmidt tails. [The converse](converse.md) supplies this reduction.

Summing the nonnegative inequalities (13) and using (12),

```math
\mu(p)
\ge
s\left[d\mu(p)+\frac{d-1}{2}\right].
\tag{14}
```

For finite mean energy this requires $`s<1/d`$ and yields

```math
E(C)\ge
\frac{s(d-1)}{1-ds}.
\tag{15}
```

The construction (1) attains equality. Indeed, when $`ds<1`$ its moment is finite, and (4) makes (14) an equality. Therefore

```math
\boxed{
E_1(0;s,d)=\frac{s(d-1)}{1-ds},
\qquad 0<s<1/d.
}
\tag{16}
```

Equivalently, at a finite budget $`E>0`$,

```math
\boxed{
p_{\rm exact}^{\max}(E;d)
=
\frac{E}{dE+d-1}.
}
\tag{17}
```

The right side is strictly below $`1/d`$ and approaches that threshold only as $`E\to\infty`$.

## 4. The sharp positive-error limit

For fixed $`0<s<1/d`$,

```math
\boxed{
\lim_{\varepsilon\downarrow0}
E_1(\varepsilon;s,d)
=
\frac{s(d-1)}{1-ds}.
}
\tag{18}
```

The exact construction supplies the upper bound for every error. Finite truncations also approach this value with success exactly $`s`$ and joint error tending to zero.

For the lower bound, choose any sequence of errors tending to zero and nearly optimal catalysts whose energies approach the lower limit. The exact construction bounds these energies uniformly. Let $`p^{(n)}`$ be their decreasing Schmidt spectra and $`\mu_n`$ their index moments. By (11), the moments are uniformly bounded. In particular,

```math
\sum_{j>k}p_j^{(n)}
\le\frac{\mu_n}{k}
\qquad(k\ge1).
\tag{19}
```

This gives uniform tightness. After taking a subsequence, the spectra converge in $`\ell^1`$ to a normalized decreasing sequence $`p`$. Fatou's lemma gives

```math
\mu(p)\le\liminf_n\mu_n<\infty.
\tag{20}
```

For each fixed $`k`$, the [approximate tail inequality](converse.md) passes to the limit and becomes (13). Summing only after taking this limit gives (14), hence $`\mu(p)\ge s(d-1)/[2(1-ds)]`$. Combining with (11) and (20) proves the required lower limit.

This order of operations matters. Summing an error-dependent additive bound over infinitely many tails would not establish (18).

## 5. Exactness, finite rank and repeated use

A finite-rank pure catalyst cannot return exactly while producing $`|\Phi_d\rangle`$ on a nonzero-probability LOCC branch. If its Schmidt rank is $`D<\infty`$, the desired product has rank $`dD>D`$, whereas a local Kraus branch cannot increase Schmidt rank. The exact finite-energy states above evade this finite-rank obstruction through infinite support, not through an uncharged extra shared system.

Exact return is promised only on success. Repeating the exact protocol $`k`$ times gives $`k`$ consecutive successes with probability $`s^k`$. A failure consumes the catalyst. Neither the construction nor the bound describes an indefinitely reusable entanglement source.

The spectrum conversion tools behind (13) are inherited from Vidal's monotones and infinite-dimensional SLOCC theory. The optimized energy formula and its relation to the critical and supercritical accuracy laws are discussed against that prior work in [related work](../references/related_work.md).

