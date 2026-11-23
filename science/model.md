# Model and main results

Alice and Bob extract a fixed pure entangled target while returning their known pure oscillator catalyst on an announced success. Failure may consume the catalyst. The target's Schmidt spectrum and the catalyst's physical mode count determine the optimal initial photon inventory.

## States and charged inventory

Fix $`m\ge1`$ equal-frequency oscillator modes at each party, with common frequency $`\omega>0`$. Their only initially shared entanglement is a known pure catalyst $`|C\rangle`$. With vacuum energy subtracted, its total initial mean photon number is

```math
E(C)=\left\langle C\left|
\sum_{a=1}^m a_a^\dagger a_a+
\sum_{b=1}^m b_b^\dagger b_b
\right|C\right\rangle.
```

The excitation energy is $`\hbar\omega E(C)`$. Both parties' photons count, including initial local squeezing and displacement. Finite mean energy does not require finite Fock support.

Target registers begin in a product pure state. The desired finite pure target is known, including its local Schmidt bases, and can be written

```math
|\phi_\lambda\rangle
=\sum_{i=1}^d\sqrt{\lambda_i}\,|i\rangle_A|i\rangle_B,
```

where $`d\ge2`$, $`\lambda_1\ge\cdots\ge\lambda_d>0`$ and $`\sum_i\lambda_i=1`$. Zero Schmidt coefficients are omitted. Known local changes of basis implement any finite pure target with this spectrum. The uniform spectrum $`\lambda_i=1/d`$ gives $`|\Phi_d\rangle`$; $`d=2`$ is one Bell pair.

## Operations, heralding and return

Allowed protocols use local operations and classical communication (LOCC), arbitrary product local ancillas and classical randomization. No fresh shared entanglement or quantum communication is supplied. Local preparation time, control work, gate complexity and the local energy of target/work registers are unrestricted and are not part of the initial catalyst inventory.

The converse covers finite-round LOCC and trace-norm limits of their subnormalized announced-success outputs, with success probability and retained output converging. It includes adaptive protocols, discarded local environments, mixed retained outputs and the corresponding physically defined sequential limits. The attaining protocols use a single local two-outcome filter, one announcement and local isometries.

Fix $`0\lt s\lt1`$. An announced success has actual probability $`p_{\rm suc}\ge s`$ and normalized retained state $`\rho_{\rm suc}`$ satisfying

```math
F_{\rm joint}
=\langle C,\phi_\lambda|\rho_{\rm suc}|C,\phi_\lambda\rangle
\ge1-\varepsilon.
```

This is squared fidelity with the complete pure reference. It tests catalyst return, target preparation and their joint decoupling. The corresponding purified distance is $`\sqrt{1-F_{\rm joint}}`$. Returning only a marginal or permitting residual target–catalyst correlations under another error criterion defines a different task.

Failure is unrestricted. In the attaining constructions it destroys the catalyst to a product state. A protocol exceeding success $`s`$ can independently discard some success flags, so success exactly $`s`$ suffices for upper bounds.

Define

```math
E_m(\varepsilon;s,\lambda)
=\inf\{E(C):p_{\rm suc}\ge s,\ F_{\rm joint}\ge1-\varepsilon\},
```

over the stated pure catalysts and protocols. Infinite support with finite mean energy is allowed. Every positive-error upper bound also has finite Schmidt support and finite-dimensional local operations.

The limit $`\varepsilon\downarrow0`$ holds at fixed $`m,s,\lambda`$. Constants may depend on all these parameters. There is no uniform claim with growing target rank/mode count, changing Schmidt probabilities or success approaching a boundary.

## The spectral success–energy law

Let $`q_s\in(0,1)`$ be the unique solution and define $`b_s>0`$ by

```math
\sum_{i=1}^d(s\lambda_i)^{q_s}=1,
\qquad b_s=\frac1{q_s}-1.
```

For $`q\in(0,1)`$, use the natural-log Rényi entropy

```math
H_q(\lambda)=\frac{\log\sum_i\lambda_i^q}{1-q}.
```

The critical success is

```math
\boxed{
s_c(\lambda,m)
=\left(\sum_i\lambda_i^{m/(m+1)}\right)^{-(m+1)/m}
=e^{-H_{m/(m+1)}(\lambda)/m}.
}
```

**Theorem 1 (sharp fixed-parameter inventory law).** In the model above:

| Success promise | Optimal initial photons as $`\varepsilon\downarrow0`$ |
|---|---|
| $`s\lt s_c(\lambda,m)`$ | Convergence to an attained finite exact-return optimum $`E_m(0;s,\lambda)>0`$ |
| $`s=s_c(\lambda,m)`$ | $`\Theta_{m,s,\lambda}(\log(1/\varepsilon))`$ |
| $`s_c(\lambda,m)\lt s\lt1`$ | $`\Theta_{m,s,\lambda}(\varepsilon^{-a_m(s,\lambda)})`$ |

The positive exponent in the last row is

```math
a_m(s,\lambda)=\frac1{m b_s}-1.
```

The three rows equivalently have $`b_s>1/m`$, $`b_s=1/m`$ and $`b_s\lt 1/m`$. Exact finite-energy return is possible precisely in the strict first regime. The critical and supercritical orders match over all allowed LOCC protocols, including mixed success outputs. The [accuracy proof](target_accuracy.md) gives both the universal converse and a finite cutoff with success exactly $`s`$.

## The exact optimal catalyst

**Theorem 2 (universal exact passive-energy minimizer).** Set

```math
A=\frac{1-s}{1-s\lambda_1}.
```

Form a multiset containing one coefficient $`A`$ and, for every finite word $`(i_1,\ldots,i_\ell)`$ whose first symbol is not 1, a coefficient

```math
A\prod_{a=1}^{\ell}(s\lambda_{i_a}).
```

Its decreasing rearrangement $`r=(r_j)`$ is normalized. Every exactly feasible source spectrum is majorized by $`r`$. If $`e_j`$ is the $`j`$th local $`m`$-mode photon number in increasing order with multiplicity, then

```math
\boxed{E_m(0;s,\lambda)=2\sum_{j\ge1}e_jr_j.}
```

The equality includes the value infinity. When finite, the minimum is attained in matched passive Fock bases by a bounded root filter followed by local Schmidt reindexing. On success it returns exactly $`|C\rangle\otimes|\phi_\lambda\rangle`$; on failure it leaves a product vacuum.

The spectrum has $`r_j=\Theta_{s,\lambda}(j^{-1/q_s})`$. The [exact-spectrum proof](target_spectrum.md) establishes its optimality using a majorization-preserving contraction and derives its exponent by weighted-tree counting. [Passive energy](spectral_energy.md) supplies the physical basis-independent bound. The optimum is an exact spectrum sum, rather than a simple elementary formula for every target or the exact frontier at each positive error.

## Uniform-target formulas retained as a special case

For $`\lambda_i=1/d`$, write $`E_m(\varepsilon;s,d)`$ as shorthand. Then

```math
\begin{aligned}
s_c&=d^{-1/m},\\
b_s&=\frac{\log(1/s)}{\log d},\\
a_m(s,d)&=\frac{\log(sd^{1/m})}{\log(1/s)}.
\end{aligned}
```

The weighted-word spectrum becomes the logarithmic-block construction in [construction](construction.md), and [converse](converse.md) gives its direct rank-dilation proof.

For one oscillator per party, the exact and limiting subcritical energy simplify to

```math
E_1(0;s,d)
=\lim_{\varepsilon\downarrow0}E_1(\varepsilon;s,d)
=\frac{s(d-1)}{1-ds},
\quad 0\lt s\lt1/d.
```

Equivalently, at a finite photon budget $`E>0`$, the maximum exact success is $`E/(dE+d-1)`$. [Exact success](exact_success.md) retains the direct derivation and the infinite-dimensional local dilation.

## Mode count and a physical example

The minimum number of modes per party for exact finite-energy return is

```math
m_{\min}^{\rm exact}(s,\lambda)
=\left\lfloor\frac1{b_s}\right\rfloor+1.
```

The strict boundary is essential. For uniform targets this reduces to $`\lfloor\log d/\log(1/s)\rfloor+1`$.

With one mode per party, $`\lambda=(0.9,0.1)`$ has critical success $`0.625`$, whereas a Bell pair of the same Schmidt rank has critical success $`0.5`$. At success $`0.6`$, the former admits exact return at finite mean energy and the latter does not. The [interpretation](interpretation.md) and [mode-threshold page](mode_threshold.md) explain this spectrum dependence.

## Scope and attribution

The catalyst is known and pure; the target has fixed finite Schmidt rank and known local bases. Arbitrary mixed initial catalysts, infinite-rank targets, the deterministic endpoint $`s=1`$, energy-conserving control restrictions and uniform varying-parameter limits are outside the matching theorem. The cost is initial catalyst photon inventory, without a preparation-work, gate-count, runtime or fault-tolerance guarantee.

Stochastic Schmidt-tail conversion, infinite-dimensional SLOCC theory, sorted-spectrum fidelity and passive energy are inherited foundations. The added account optimizes the exact self-borrowing spectrum and the success-dependent photon/accuracy law, identifying the Rényi order selected by oscillator mode count. [Related work](../references/related_work.md) gives the model-level comparison.

[Scientific route](README.md) · [Exact spectrum](target_spectrum.md) · [Accuracy law](target_accuracy.md) · [Verification](../verification/README.md)
