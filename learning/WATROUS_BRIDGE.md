# From Watrous to heralded entanglement borrowing

Alice and Bob share an entangled oscillator state. They want an additional Bell pair and the original shared state back whenever a local measurement announces success. A failed attempt may consume the shared state. The scientific question is how the promised success probability changes the initial photon inventory needed for an accurate joint return.

The educational anchor is John Watrous, [*The Theory of Quantum Information*](https://cs.uwaterloo.ca/~watrous/TQI/), Cambridge University Press, **2018**. The author's page identifies the edition and supplies its chapter manuscripts and errata. The section numbers below refer to that 2018 manuscript. The book develops finite-dimensional foundations; the oscillator limits and the energy law are supplied by this project.

Use this bridge alongside the [30-milestone map](MILESTONES.md) and the [worked example](WORKED_EXAMPLE.md). The example follows one complete filter, including its success probability, failure output and joint fidelity. Specialists can start directly with the [model and theorems](../science/model.md).

## Relevant parts of the anchor

The entries identify a short route through one book, rather than a requirement to read it in full.

| Verified location | Connection to this project |
|---|---|
| [§1.1.3, *Operator decompositions and norms*](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), especially equations (1.162)–(1.164) | Singular values give Schmidt amplitudes. Their squares form the probability sequence used below. |
| [§2.2.2, *Representations and characterizations of channels*](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf); §2.3.2 | Kraus and Stinespring representations describe a local filter, its announced outcome and discarded local systems. |
| [§3.2, *The fidelity function*](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), Definition 3.11 and equation (3.64) | Translate the book's fidelity into the squared convention of the return guarantee. |
| [§4.3.1, *Majorization for real vectors*](https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf) | Ordered probability sums compare how concentrated two spectra are. |
| [§6.1.2, *Separable maps and the LOCC paradigm*](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf) | Local quantum operations and classical messages define the allowed processing. |
| [§6.2.1, *Entanglement transformation*](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), Theorem 6.33 | Finite-dimensional deterministic pure-state conversion provides the starting relation between LOCC and majorization. |

## Translate the notation first

### Schmidt amplitudes and probabilities

Write a normalized pure catalyst as

```math
|C\rangle=
\sum_{j\ge1}\sqrt{p_j}\,
|u_j\rangle_A|v_j\rangle_B,
\qquad
p_1\ge p_2\ge\cdots\ge0,
\qquad \sum_jp_j=1.
```

The amplitudes are $`\sqrt{p_j}`$. The reduced density operators have eigenvalues $`p_j`$. Thus a singular value $`s_j`$ in the book's decomposition corresponds to $`p_j=s_j^2`$ here. The [construction](../science/construction.md) specifies a pure coherent superposition with these amplitudes; an equation between probability vectors does not make that state a classical mixture.

The basis index $`j`$ orders probabilities. It is not automatically the physical photon number. Connecting the two requires the separate [spectral-energy argument](../science/spectral_energy.md).

### Root fidelity and squared joint fidelity

To keep the conventions distinct, denote the book's fidelity by $`F_W`$:

```math
F_W(\rho,\sigma)
=\left\|\sqrt\rho\sqrt\sigma\right\|_1.
```

This project tests a pure reference $`|T\rangle=|C\rangle\otimes|\Phi_d\rangle`$ and uses

```math
F_{\rm joint}
=\langle T|\rho_{\rm suc}|T\rangle
=F_W(\rho_{\rm suc},|T\rangle\langle T|)^2.
```

Consequently the promised error $`F_{\rm joint}\ge1-\varepsilon`$ means $`F_W\ge\sqrt{1-\varepsilon}`$. The associated purified distance is at most $`\sqrt\varepsilon`$. This square matters when translating a small overlap error into the exponent of an energy bound.

The reference contains both the returned catalyst and the target. A good target marginal alone does not test whether the catalyst was returned and decoupled. The state $`\rho_{\rm suc}`$ is normalized conditional on the announced success; its probability is a separate resource parameter $`s`$.

### Majorization and tail direction

For decreasing normalized spectra, $`p\prec q`$ means that every initial partial sum of $`p`$ is at most the corresponding sum of $`q`$. Equivalently, with

```math
P_k=\sum_{j>k}p_j,
\qquad Q_k=\sum_{j>k}q_j,
```

the inequalities become $`P_k\ge Q_k`$. This is the direction used for deterministic conversion: a more spread-out Schmidt spectrum can be converted to a more concentrated one. Heralded conversion instead has an average constraint that includes the success probability and the failure branch.

## The steps supplied by this project

### 1. From finite rank to finite mean energy

A finite-rank catalyst of rank $`D`$ would need to become a product of rank $`dD`$ to return exactly while adding $`\Phi_d`$. A local Kraus branch cannot increase Schmidt rank. Exact success at finite $`D`$ is therefore impossible.

An oscillator with finite mean photons can still have infinitely many nonzero Schmidt probabilities. The exact subcritical construction uses this distinction. At every positive requested error, [finite truncation](../science/construction.md) instead gives a finite-rank state and finite local operations. The passage to countable spectra is proved using bounded finite-index tails and nonnegative summation; it is not obtained by simply replacing a finite dimension symbol with infinity.

### 2. From LOCC to a success-weighted tail bound

For each fixed $`k`$, a pure-state Schmidt tail is one minus the sum of the $`k`$ largest reduced-state eigenvalues. That complement is concave. A local instrument leaves the other party's reduced state unchanged on average, so the average tail cannot increase.

At exact joint return, dropping the nonnegative failure contribution gives $`P_k\ge sQ_k`$. For approximate mixed success outputs, [the converse](../science/converse.md#the-tail-inequality) retains all local environments, compares complete pure branches with the desired output, and controls their square-root spectral distances. It establishes

```math
P_k\ge
s\left(\sqrt{Q_k}-\sqrt{2\varepsilon}\right)_+^2,
\qquad x_+=\max\{x,0\}.
```

This reduction is needed because a retained success output can be mixed and its discarded environment can contain entanglement. The proof also specifies how the bound passes to the allowed trace-norm limits of announced-success outputs.

### 3. From an added target to repeated rank scales

The target $`\Phi_d`$ has $`d`$ equal Schmidt probabilities. Tensoring with it repeats each catalyst probability $`d`$ times and divides it by $`d`$:

```math
q_j=\frac1d p_{\lceil j/d\rceil},
\qquad Q_{dk}=P_k.
```

The tail bound therefore compares the catalyst to itself at two index scales:

```math
\sqrt{P_{dk}}
\ge\sqrt{s}
\left(\sqrt{P_k}-\sqrt{2\varepsilon}\right)_+.
```

At zero error, every step from $`k`$ to $`dk`$ must retain a fraction $`s`$ of the tail. At small error, [iteration](../science/converse.md#a-geometric-tail-recurrence) forces tails of order $`s^\ell`$ through approximately

```math
L=\frac{\log(1/\varepsilon)}{\log(1/s)}+O_{s,d}(1)
```

scales. This is the link between a conditional output guarantee and a requirement on the initial spectrum.

### 4. From rank scales to physical photons

For $`m`$ oscillator modes per party, the number of local Fock states with at most $`h`$ photons is $`\binom{h+m}{m}`$. Thus their ordered energies grow as $`e_j\asymp j^{1/m}`$ at fixed $`m`$. Assigning larger Schmidt probabilities to lower energies minimizes the initial inventory and gives

```math
E(C)\ge2\sum_je_jp_j
=2\sum_{k\ge1}(e_{k+1}-e_k)P_k.
```

The factor two counts both parties. [Spectral energy](../science/spectral_energy.md) proves this inequality for arbitrary physical Schmidt bases, including the degeneracies of multimode Fock energies. It is an initial-state rearrangement bound, not a claim that LOCC conserves photon energy.

The required tails then cost a geometric sum with ratio $`g=sd^{1/m}`$. The [matching construction](../science/construction.md#5-photon-inventory-and-the-three-regimes) places mass of order $`s^\ell`$ in the corresponding rank blocks, so it attains the same order. The [mode-threshold account](../science/mode_threshold.md) combines the two directions:

| Ratio $`g`$ | Initial inventory as joint error vanishes |
|---|---|
| $`g<1`$ | Bounded; an infinite-support state permits exact return at finite energy. |
| $`g=1`$ | $`\Theta(\log(1/\varepsilon))`$. |
| $`g>1`$, with $`s<1`$ | $`\Theta(\varepsilon^{-a_m})`$, where $`a_m=\log(g)/\log(1/s)`$. |

These are fixed-$`m,d,s`$ limits. The [one-mode exact optimum](../science/exact_success.md) further evaluates the subcritical budget as $`s(d-1)/(1-ds)`$. Its failure output is vacuum, so successive exact successes have probability $`s^k`$ after $`k`$ repetitions. Conditional return does not provide an indefinitely reusable entanglement source.

## Reading route and boundaries

Follow the [worked example](WORKED_EXAMPLE.md), then [model](../science/model.md), [construction](../science/construction.md), [converse](../science/converse.md), [exact success](../science/exact_success.md) and [mode threshold](../science/mode_threshold.md). The [milestones](MILESTONES.md) organize these connections from basic objects to the complete result. [Interpretation](../science/interpretation.md) separates mean photons, mode count, growing Fock cutoff and local control costs.

Watrous supplies the finite-dimensional mathematical foundation. The countable-spectrum tail extension, oscillator counting, success-dependent energy optimization and matching asymptotic construction are additional steps explained in the scientific pages. Their primary-paper attribution is collected in [related work](../references/related_work.md); those citations identify research dependencies rather than additional educational anchors. Preparation efficiency, control work, loss robustness, arbitrary mixed catalysts and the deterministic endpoint $`s=1`$ are outside the stated law.
