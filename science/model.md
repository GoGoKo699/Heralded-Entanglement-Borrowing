# Model and main results

A shared entangled state can supply a maximally entangled target while being returned on an announced success. The catalyst may be consumed on failure. This account determines how the required initial oscillator energy depends on the promised success probability and the accuracy of that joint return.

## States and physical inventory

Fix integers $`m\ge1`$ and $`d\ge2`$. Alice and Bob each hold exactly $`m`$ catalyst oscillator modes, all at the same frequency $`\omega>0`$. They share a known pure state $`|C\rangle`$. With zero-point energy subtracted, its initial total mean photon number is

```math
E(C)=
\left\langle C\left|
\sum_{a=1}^{m}a_a^\dagger a_a+
\sum_{b=1}^{m}b_b^\dagger b_b
\right|C\right\rangle.
\tag{1}
```

The corresponding excitation energy is $`\hbar\omega E(C)`$. Both parties' photons are counted, including any local squeezing or displacement in the initial catalyst. All initially shared entanglement is contained in these catalyst modes.

The target registers $`A_T,B_T`$ are initially in a product pure state. Their desired state is

```math
|\Phi_d\rangle=
\frac1{\sqrt d}\sum_{r=0}^{d-1}|r\rangle_{A_T}|r\rangle_{B_T}.
\tag{2}
```

The target dimension is fixed. For $`d=2`$ this is one Bell pair; $`d=2^k`$ represents $`k`$ Bell pairs.

A finite number of oscillator modes still has an infinite-dimensional Hilbert space. Finite mean energy does not require a finite Fock cutoff. We distinguish exact infinite-support constructions from finite-support constructions at every positive error.

## Operations, heralding and return

The allowed protocols use local operations and classical communication (LOCC), with arbitrary product local ancillas and classical randomization. These ancillas supply no initial shared entanglement. Local work, local control complexity and preparation time are unrestricted. No fresh entangled specimens or quantum communication are supplied.

The converse applies to finite-round LOCC and to trace-norm limits of their subnormalized announced-success outputs, with the success probability and retained output converging. This includes the corresponding physically defined limits of sequential LOCC protocols. The construction uses a single local two-outcome filter, one announcement and local isometries; no limiting sequence of communication rounds is needed.

Fix a promised success probability $`0<s<1`$. An announced success has actual probability $`p_{\rm suc}\ge s`$. Its normalized retained state $`\rho_{\rm suc}`$ must obey

```math
F_{\rm joint}
=
\langle C,\Phi_d|\rho_{\rm suc}|C,\Phi_d\rangle
\ge1-\varepsilon.
\tag{3}
```

This is squared fidelity with the complete pure reference. It requires return of the original catalyst, preparation of the target and their joint decoupling. It is stronger than requiring separate accurate marginals without a joint condition. The associated purified distance is $`\sqrt{1-F_{\rm joint}}`$.

The failure branch is unrestricted. In the exact attaining construction it destroys the catalyst. A protocol with $`p_{\rm suc}>s`$ may independently discard a fraction of its success flags, so using success probability exactly $`s`$ is sufficient for optimization.

Only the initial catalyst inventory (1) is minimized. In particular, $`E(C)`$ is not the work spent preparing or operating the apparatus. Target registers and local control ancillas introduce no additional shared entanglement, but their local energy is not included in this inventory.

## Optimization and limiting convention

Define

```math
E_m(\varepsilon;s,d)
=
\inf\left\{
E(C):
\begin{array}{l}
|C\rangle\text{ is a pure }m\text{-mode-per-party catalyst},\\
p_{\rm suc}\ge s,\quad F_{\rm joint}\ge1-\varepsilon
\end{array}
\right\}.
\tag{4}
```

The infimum includes infinite-support states with finite mean energy. Every upper bound at $`\varepsilon>0`$ also has a finite-support implementation.

Unless stated otherwise, $`\varepsilon\downarrow0`$ while $`m,d,s`$ remain fixed. Constants in asymptotic bounds may depend on all three. No uniform joint limit with growing mode count or target dimension, or with $`s`$ approaching a boundary, is asserted.

Set

```math
g=d^{1/m}s,\qquad
s_c=d^{-1/m},\qquad
a_m(s,d)=
\frac{\log g}{\log(1/s)}.
\tag{5}
```

The logarithm base is immaterial in this ratio.

## The success–energy law

**Theorem 1 (fixed mode count and fixed success).** In the model above,

| Success promise | Optimal initial photon inventory as $`\varepsilon\downarrow0`$ |
|---|---|
| $`0<s<s_c`$ | $`E_m(\varepsilon;s,d)=\Theta_{m,s,d}(1)`$; exact joint return is possible at finite mean energy |
| $`s=s_c`$ | $`E_m(\varepsilon;s,d)=\Theta_{m,d}(\log(1/\varepsilon))`$ |
| $`s_c<s<1`$ | $`E_m(\varepsilon;s,d)=\Theta_{m,s,d}(\varepsilon^{-a_m(s,d)})`$ |

At or above $`s_c`$, exact joint return at finite mean energy is impossible. The critical logarithm and the supercritical power are matching lower and upper orders over all allowed pure catalysts and LOCC protocols, including mixed retained success outputs.

The mechanism has two parts. The target multiplies Schmidt rank by $`d`$ and forces a tail recurrence under successful approximate return. The number of low-energy Fock states determines the cost of the tails that must survive that recurrence. [The converse](converse.md) proves the recurrence and lower bounds. [The construction](construction.md) gives matching finite catalysts. [The spectral-energy account](spectral_energy.md) converts Schmidt rank into a physical photon inventory.

**Theorem 2 (sharp one-mode exact budget).** For one oscillator per party and any finite $`E>0`$, the maximum success probability for exact joint return with initial inventory at most $`E`$ is

```math
p_{\rm exact}^{\max}(E;d)
=
\frac{E}{dE+d-1}.
\tag{6}
```

It is attained by an infinite-support finite-energy pure catalyst. Equivalently, for $`0<s<1/d`$,

```math
E_1(0;s,d)
=
\frac{s(d-1)}{1-ds},
\qquad
\lim_{\varepsilon\downarrow0}
E_1(\varepsilon;s,d)
=
\frac{s(d-1)}{1-ds}.
\tag{7}
```

[Exact success](exact_success.md) proves these statements. For $`m>1`$, the threshold and divergence orders are established, but no corresponding exact finite-error frontier or simple exact subcritical energy constant is claimed.

## What the mode count changes

**Corollary 3 (exact finite-energy mode threshold).** At fixed $`d\ge2`$ and $`0<s<1`$, exact joint return with finite mean energy is possible precisely when

```math
m>\frac{\log d}{\log(1/s)}.
\tag{8}
```

Thus the smallest admissible integer mode count per party is

```math
m_{\min}^{\rm exact}(s,d)
=
\left\lfloor
\frac{\log d}{\log(1/s)}
\right\rfloor+1.
\tag{9}
```

The strict inequality matters at an integer boundary. These are exact finite-energy statements with infinite Fock support. Finite-support versions approach the same task at every positive error. [The mode-threshold page](mode_threshold.md) gives the proof and examples.

## Scope and attribution

The initial catalyst is pure. The result does not cover arbitrary mixed catalysts, arbitrary entangled targets, energy-conserving control restrictions, or unrestricted growing-parameter limits. It is an initial energy and mode inventory law, without a preparation, gate-count, runtime or work advantage claim. The deterministic endpoint $`s=1`$ is outside Theorem 1.

The proof uses established Schmidt-spectrum conversion tools: Vidal tail monotones, infinite-dimensional SLOCC conversion theory and fidelity bounds from sorted Schmidt coefficients. The added result is their optimization into the success-dependent oscillator energy law, including its critical order and supercritical exponent. [Related work](../references/related_work.md) states the comparison at the level of the actual models.

For the complete account, continue through [construction](construction.md), [converse](converse.md), [exact success](exact_success.md), [mode threshold](mode_threshold.md) and [interpretation](interpretation.md). Finite numerical checks and their limits are described in [verification](../verification/README.md).

