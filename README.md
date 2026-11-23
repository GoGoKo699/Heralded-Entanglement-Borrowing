# Heralded Entanglement Borrowing

**How does the entanglement spectrum of a desired target determine the energy needed to borrow it?** This project gives the optimal exact catalyst and sharp energy–accuracy laws for a known pure oscillator source returned on a successful trial.

Alice and Bob share a pure catalyst with a fixed number $`m`$ of equal-frequency oscillator modes each. Local operations and classical communication produce a prescribed finite pure target with Schmidt probabilities $`\lambda=(\lambda_1,\ldots,\lambda_r)`$. On an announced success of probability at least $`s`$, the full returned catalyst and target must have joint squared fidelity at least $`1-\varepsilon`$ with their desired product state. **Failure may consume the catalyst.** The resource $`E`$ is the catalyst's initial total mean photon number across both parties.

## The target spectrum controls the threshold

For fixed $`m\ge1`$, positive target Schmidt probabilities of fixed rank $`r\ge2`$, and fixed $`0<s<1`$, the critical success is

```math
\boxed{
s_c(\lambda,m)
=\exp\!\left[-\frac{H_{m/(m+1)}(\lambda)}{m}\right].
}
```

Here $`H_\alpha(\lambda)=\log(\sum_i\lambda_i^\alpha)/(1-\alpha)`$ is Rényi entropy with natural logarithms. The oscillator density of states selects its order $`m/(m+1)`$.

| Success requirement | Optimal initial photon inventory as $`\varepsilon\downarrow0`$ |
|---|---|
| $`s<s_c(\lambda,m)`$ | Converges to the finite exact optimum; exact joint return is possible |
| $`s=s_c(\lambda,m)`$ | $`\Theta(\log(1/\varepsilon))`$ |
| $`s_c(\lambda,m)<s<1`$ | $`\Theta(\varepsilon^{-a})`$, with the spectrum-dependent exponent below |

Define the unique $`q_s\in(0,1)`$ and exponent by

```math
\sum_{i=1}^r(s\lambda_i)^{q_s}=1,
\qquad
a=\frac{1}{m(1/q_s-1)}-1.
```

The power applies in the supercritical row, where $`a>0`$. All limits fix the target spectrum, mode count and success before sending the error to zero. The lower bounds cover the full allowed LOCC class, including mixed retained success outputs. Finite catalysts and bounded local filters attain the approximate orders at success exactly $`s`$.

With one oscillator per party, a target with probabilities $`(0.9,0.1)`$ has threshold $`5/8`$, while a Bell pair has threshold $`1/2`$. At success $`s=0.6`$, the former permits exact finite-energy return and the latter does not. Equal Schmidt rank therefore need not mean the same borrowing regime.

## An optimal catalyst, with an explicit filter

The [target-spectrum account](science/target_spectrum.md) gives a decreasing spectrum $`r^{(s,\lambda)}`$ that majorizes every spectrum permitting exact borrowing. Assigning it to the ordered Fock levels minimizes the exact initial photon inventory for every fixed mode count:

```math
E_m^{\rm exact}(s,\lambda)
=2\sum_{j\ge1}e_j r_j^{(s,\lambda)},
```

where $`e_j`$ is the $`j`$th local $`m`$-mode photon number, including degeneracies. This sum is finite precisely below the critical success. A root-only local filter succeeds exactly $`s`$; local reindexing then returns the catalyst and supplies the target. Exact attainment has infinite Schmidt support. The [accuracy proof](science/target_accuracy.md) gives finite cutoffs at every positive error and preserves the promised success when truncating.

## The maximally entangled special case

For $`\lambda_i=1/d`$, the threshold reduces to $`s_c=d^{-1/m}`$ and the power exponent is

```math
a_m(s,d)=\frac{\log(d^{1/m}s)}{\log(1/s)}.
```

For one oscillator per party, the exact optimum also has the closed form

```math
p_{\rm exact}^{\max}(E;d)=\frac{E}{dE+d-1},
\qquad
E_1^{\rm exact}(s,d)=\frac{s(d-1)}{1-ds}
\quad(0<s<1/d).
```

The [uniform-target construction](science/construction.md), [tail recurrence](science/converse.md), and [one-mode exact calculation](science/exact_success.md) retain these useful explicit formulas. They are specializations of the target-spectrum law.

## Read the science

Start with the [physical interpretation](science/interpretation.md), [model](science/model.md), or [proof map](science/README.md).

| Question | Scientific account |
|---|---|
| Which states, operations and resources are supplied? | [Model and main results](science/model.md) |
| Why is there one optimal exact spectrum? | [Majorization fixed point and weighted-word catalyst](science/target_spectrum.md) |
| Why do arbitrary successful outputs obey the same energy orders? | [General-target accuracy law](science/target_accuracy.md) |
| How does the oscillator spectrum set the physical cost? | [Spectral energy](science/spectral_energy.md) |
| What does the number of modes change? | [Mode threshold](science/mode_threshold.md) |
| Which ingredients are inherited? | [Related work](references/related_work.md) and [bibliography](references/references.bib) |

Schmidt-tail conversion, infinite-dimensional stochastic LOCC and root filtering are established foundations. The contribution is the optimized self-borrowing spectrum and its success-dependent photon frontier, including the target-specific Rényi boundary. The literature comparison states its actual scope.

## Learn the project

The educational anchor is John Watrous, [*The Theory of Quantum Information* (2018)](https://cs.uwaterloo.ca/~watrous/TQI/), using the author's available manuscript. Fidelity, majorization and bipartite entanglement provide the foundations; the oscillator, fixed-point and heralding arguments are developed here.

Begin with the [worked examples](learning/WORKED_EXAMPLE.md), then follow the [Watrous bridge](learning/WATROUS_BRIDGE.md) and [30-milestone map](learning/MILESTONES.md).

## Reproduce the finite checks

With Python 3.11 or later, run from the repository root:

```bash
python3 verification/run_checks.py
```

The standard-library suite checks finite instruments, success-conditioned joint fidelity, target spectra, photon accounting, uniform specializations and representative construction laws. [Verification](verification/README.md) distinguishes exact rational identities from numerical illustrations. The general optimality and asymptotic statements depend on the analytical proofs.

## Scope

The initial catalyst is known and pure, the target is a fixed finite pure state, and the mode count and success stay fixed as error vanishes. All initially shared catalyst modes are counted. Product local ancillas and target registers supply no extra shared entanglement. Return concerns the entire catalyst–target product on success.

Initial photon inventory does not price preparation work, control work, gates or runtime. Exact finite-energy attainment uses infinite support; positive-error implementations can have finite support. Mixed initial catalysts, deterministic success $`s=1`$, energy-conserving control restrictions and uniform limits with varying target or success are outside these laws.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
