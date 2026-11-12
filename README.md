# Heralded Entanglement Borrowing

**How much initial energy is needed to extract entanglement while returning the source on a successful trial?** This project determines a sharp success threshold and matching energy–accuracy laws for a known pure oscillator catalyst.

Alice and Bob share a pure catalyst with a fixed number $`m`$ of equal-frequency oscillator modes each. They use local operations and classical communication to produce a fixed maximally entangled target $`\Phi_d`$. On an announced success of probability at least $`s`$, the returned catalyst and target must have joint squared fidelity at least $`1-\varepsilon`$ with their desired product state. **Failure may consume the catalyst.** The charged resource $`E`$ is the catalyst's initial total mean photon number across both parties.

## Principal results

The critical success probability is

```math
\boxed{s_c=d^{-1/m}.}
```

At fixed $`m\ge1`$, $`d\ge2`$ and $`0\lt s\lt 1`$, the minimum initial inventory satisfies:

| Success requirement | Optimal photon inventory as $`\varepsilon\downarrow0`$ |
|---|---|
| $`s\lt s_c`$ | Bounded; exact joint return is possible at finite mean energy |
| $`s=s_c`$ | $`\Theta(\log(1/\varepsilon))`$ |
| $`s_c\lt s\lt 1`$ | $`\Theta(\varepsilon^{-a_m})`$, where $`a_m=\log(d^{1/m}s)/\log(1/s)`$ |

The lower bounds cover all allowed LOCC protocols and mixed retained success outputs. Explicit finite catalysts attain the logarithmic and power orders. The [model](science/model.md) states the complete assumptions, operation closure and limiting convention.

For **one oscillator per party**, the maximum success at an initial photon budget $`E>0`$ and exact joint return is

```math
\boxed{p_{\rm exact}^{\max}(E;d)=\frac{E}{dE+d-1}.}
```

Equivalently, below $`s=1/d`$, the exact optimum and the vanishing-error limit are $`s(d-1)/(1-ds)`$. Exact finite-energy attainment uses infinite Schmidt rank. Every positive-error upper bound has a finite Schmidt cutoff and finite local operations. [Exact success](science/exact_success.md) separates these two statements.

For one Bell pair, one mode per party has threshold $`1/2`$. The same success becomes subcritical with two modes per party. More generally, exact finite-energy return requires strictly more than $`\log d/\log(1/s)`$ modes per party; see the [mode threshold](science/mode_threshold.md).

## Read the science

Start with the [physical interpretation](science/interpretation.md) and [model](science/model.md), or use the [scientific map](science/README.md) for a proof-oriented route.

| Question | Scientific account |
|---|---|
| What makes an approximate successful return expensive? | [Arbitrary-LOCC converse](science/converse.md) |
| How does the oscillator density of states enter? | [Spectral energy](science/spectral_energy.md) |
| Which finite states and filters attain the costs? | [Construction](science/construction.md) |
| When is exact finite-energy return possible? | [Exact success](science/exact_success.md) |
| How many physical modes are necessary? | [Mode threshold](science/mode_threshold.md) |
| What is inherited, and what is the added result? | [Related work](references/related_work.md) and [bibliography](references/references.bib) |

The proof combines established Schmidt-tail conversion theory with a fidelity-to-tail recurrence, oscillator spectral counting and matching self-similar catalysts. The optimized photon–success–accuracy law is the contribution; stochastic infinite-dimensional conversion and the filtering mechanism are attributed foundations.

[The LLM reading guide](llms.txt) maps scientific questions to authoritative pages.

## Learn the project

The single educational anchor is John Watrous, [*The Theory of Quantum Information* (2018)](https://cs.uwaterloo.ca/~watrous/TQI/), using the author's available manuscript. Its treatment of fidelity, majorization and bipartite entanglement supplies the finite-dimensional foundations; the oscillator and heralded-energy arguments are developed in this project.

| Entry | What it provides |
|---|---|
| [Worked example](learning/WORKED_EXAMPLE.md) | A complete finite Bell-pair experiment: catalyst probabilities, local filter, success, joint fidelity and photon inventory. |
| [30-milestone map](learning/MILESTONES.md) | A shared route from quantum-state foundations to the construction, converse, mode threshold and physical meaning. |
| [Watrous bridge](learning/WATROUS_BRIDGE.md) | Verified source sections, notation translations and the additional steps connecting the textbook to the project. |

## Reproduce the finite checks

With Python 3.11 or later, run from the repository root:

```bash
python3 verification/run_checks.py
```

The suite uses only the Python standard library. It checks exact finite instruments, success-conditioned joint fidelity, photon accounting, stable small-error evaluation, oscillator degeneracies and representative asymptotic construction laws. [Verification](verification/README.md) documents the expected results and what these finite tests do not prove. The universal converse and asymptotic optimization are analytical arguments in the scientific pages.

## Scope

The source catalyst is known and pure. Mode count, target dimension and success probability stay fixed as error vanishes. Target registers and local product ancillas supply no extra shared entanglement. The return guarantee concerns the full catalyst and target jointly, on success only.

The cost is initial photon inventory, without a preparation-work, control-work, gate-count, runtime or fault-tolerance claim. Finite mean energy can coexist with infinite support; finite-error cutoffs grow with accuracy. Arbitrary mixed initial catalysts, energy-conserving control restrictions and uniform limits approaching the success boundaries are outside the theorem. The deterministic endpoint $`s=1`$ is not part of the matching fixed-success law.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
