# The number of modes selects the Rényi threshold

A fixed mode count determines how many orthogonal catalyst states fit at low photon number. The target spectrum determines how much Schmidt weight successful borrowing forces at large indices. Their competition sets the exact finite-energy threshold.

## 1. Physical state counting

For $`m`$ equal-frequency modes per party, the number of local Fock basis vectors with at most $`h`$ photons is

```math
A_m(h)=\binom{h+m}{m}.
```

With photon energies listed in increasing order including degeneracy,

```math
e_j=\min\{h:j\le A_m(h)\},
\qquad e_1=0,
```

and, at fixed $`m`$,

```math
e_j=(m!j)^{1/m}+O_m(1).
```

For any pure catalyst with decreasing Schmidt probabilities $`p_j`$,

```math
E(C)\ge2\sum_j e_jp_j.
```

[Passive energy](spectral_energy.md) proves this inequality without assuming number-state Schmidt bases. Matched passive Fock bases attain it.

## 2. Target-dependent exact boundary

For a fixed finite pure target spectrum $`\lambda`$ and success $`0\lt s\lt1`$, let

```math
\sum_i(s\lambda_i)^{q_s}=1,
\qquad b_s=1/q_s-1.
```

The [exact-spectrum theorem](target_spectrum.md) gives a universally optimal catalyst with probabilities $`r_j=\Theta(j^{-1/q_s})`$. Every exactly feasible catalyst has tails at least as large as this spectrum. Its passive photon sum converges precisely when

```math
\frac1{q_s}>1+\frac1m,
\qquad\text{or equivalently}\qquad b_s>1/m.
```

At equality, the summand is of order $`1/j`$ and its sum diverges logarithmically. Finite-energy exact return therefore requires a strict inequality.

Writing $`q_*=m/(m+1)`$, this yields

```math
\boxed{
s\lt s_c(\lambda,m),
\qquad
s_c(\lambda,m)
=\left(\sum_i\lambda_i^{q_*}\right)^{-1/q_*}.
}
```

Equivalently $`s_c=e^{-H_{q_*}(\lambda)/m}`$ with natural-log Rényi entropy. The target rank alone is insufficient unless its nonzero Schmidt probabilities are uniform.

## 3. The minimum integer mode count

The exponent $`q_s`$ depends only on the target and success, not on $`m`$. Thus the exact finite-energy mode condition is

```math
m>\frac1{b_s}=\frac{q_s}{1-q_s}.
```

The smallest integer mode count per party is consequently

```math
\boxed{
m_{\min}^{\rm exact}(s,\lambda)
=\left\lfloor\frac1{b_s}\right\rfloor+1.
}
```

Every fixed finite target and fixed $`s\lt1`$ has $`q_s\lt1`$, so some finite mode count suffices. This statement does not supply a uniform energy bound as success tends to one or target parameters vary.

For a one-mode catalyst and $`\lambda=(0.9,0.1)`$, the critical success is $`5/8`$. At success $`0.6`$, one mode suffices for exact finite-energy return. At success $`5/8`$, one mode is exactly critical and two suffice for exact return. The [physical interpretation](interpretation.md) compares this with a Bell target.

## 4. Uniform targets recover the rank formula

For $`\lambda_i=1/d`$,

```math
q_s=\frac{\log d}{\log(d/s)},
\qquad b_s=\frac{\log(1/s)}{\log d}.
```

Therefore

```math
s_c=d^{-1/m},
\qquad
m_{\min}^{\rm exact}(s,d)
=\left\lfloor\frac{\log d}{\log(1/s)}\right\rfloor+1.
```

For one Bell pair:

| Promised success | Minimum modes per party for exact finite-energy return |
|---|---:|
| $`1/4`$ | 1 |
| $`1/2`$ | 2 |
| $`3/4`$ | 3 |
| $`9/10`$ | 7 |

The direct uniform-target proof uses $`Q_{dk}=P_k`$: exact success forces $`P_{dk}\ge sP_k`$, and a nonzero tail seed then persists at every geometric rank scale. Combining it with $`e_j=\Theta(j^{1/m})`$ gives a geometric energy series with ratio $`sd^{1/m}`$. [Converse](converse.md) and [construction](construction.md) retain the full recurrence and matching logarithmic-block calculation.

## 5. Approximate return at the boundary

The [robust tail comparison](target_accuracy.md#1-a-robust-comparison-with-the-exact-optimal-tail) forces the exact optimal tail up to indices of order $`\varepsilon^{-1/b_s}`$. Finite cutoffs attain that order with success exactly $`s`$. Consequently the energy is logarithmic when $`b_s=1/m`$ and a power with exponent $`1/(m b_s)-1`$ when $`b_s\lt 1/m`$.

Below the boundary, finite cutoffs converge to the exact optimal spectrum sum. At or above it, no bounded-energy family can make the joint error vanish. These conclusions optimize mean initial photon inventory; they do not optimize local preparation or control work.

Mode count, mean photons and Fock cutoff are separate resources. All initially shared catalyst modes count in $`m`$. Local product ancillas do not change the source Schmidt spectrum and cannot replace the required initial entanglement tail. Exact attainment below threshold has infinite support, whereas every positive-error upper construction has finite support.

[Model](model.md) · [Exact spectrum](target_spectrum.md) · [Accuracy law](target_accuracy.md) · [Interpretation](interpretation.md)
