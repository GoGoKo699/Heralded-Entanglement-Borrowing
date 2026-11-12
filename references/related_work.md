# Related work and attribution

The result concerns a pure catalyst in a fixed number $`m`$ of equal-frequency oscillator modes per party. An LOCC protocol succeeds with probability at least a fixed $`s`$, and its conditional output has joint squared fidelity at least $`1-\varepsilon`$ with the original catalyst tensored with $`\Phi_d`$. Failure can consume the catalyst. The optimized resource is its initial total mean photon number.

The central conclusion is the success threshold $`s_c=d^{-1/m}`$: finite-energy exact return is possible below it; at the threshold the approximate cost grows logarithmically; above it, for fixed $`s\lt 1`$, the cost has the matched power

```math
E_m(\varepsilon;s,d)
=\Theta_{s,d,m}\!\left(\varepsilon^{-a_m}\right),
\qquad
a_m=\frac{\log d}{m\log(1/s)}-1.
```

All these limits fix $`m,d,s`$ as $`\varepsilon\downarrow0`$. The spectrum-conversion tools below are inherited. The contribution here is their optimization under a photon inventory and a fixed mode count, including the approximate arbitrary-LOCC converse. See the [model](../science/model.md) for the charged resources and return convention.

## Pure-state conversion and infinite-dimensional tails

[Vidal (1999)](https://doi.org/10.1103/PhysRevLett.83.1046), *Entanglement of pure states for a single copy*, gives the optimal finite-dimensional success probability as the minimum ratio of sorted Schmidt tails. Its average-monotone tail family is the main converse tool used here. The inspected preprint is [quant-ph/9902033v2](https://arxiv.org/abs/quant-ph/9902033v2), revised 26 March 1999. The tail theorem and the use of local filters are established results.

[Vidal, Jonathan and Nielsen (2000)](https://doi.org/10.1103/PhysRevA.62.012304), *Approximate transformations and robust manipulation of bipartite pure-state entanglement*, develops fidelity-optimal pure-state LOCC transformations and the comparison of entanglement through sorted Schmidt spectra. The inspected version is [quant-ph/9910099v2](https://arxiv.org/abs/quant-ph/9910099v2). The present approximate converse combines this spectral viewpoint with a fidelity-to-tail estimate and iteration across the target's Schmidt-index dilation.

[Owari, Matsumoto and Murao (2004)](https://doi.org/10.1103/PhysRevA.70.050301), *Entanglement convertibility for infinite-dimensional pure bipartite states*, establishes that stochastic conversion has a much richer order in infinite dimension, including under bounded-energy and finite-information-exchange conditions. Its [quant-ph/0406141v1](https://arxiv.org/abs/quant-ph/0406141v1) is the relevant precursor. Consequently, infinite Schmidt rank and finite energy already coexist with nontrivial stochastic convertibility; their coexistence is part of the background to this project.

[Owari, Braunstein, Nemoto and Murao (2008)](https://www-users.york.ac.uk/~sb54/papers/obnm08.pdf), *$`\epsilon`$-convertibility of entangled states and extension of Schmidt rank in infinite-dimensional systems*, extends Nielsen's and Vidal's criteria to approximate convertibility on separable infinite-dimensional spaces. The version is [quant-ph/0609167v4](https://arxiv.org/abs/quant-ph/0609167v4), published in *Quantum Information and Computation* **8**, 30–52. Theorem 2 and Appendix D supply the infinite-dimensional stochastic tail criterion and average tail monotonicity. Appendix D also uses a spectrum with extra weight at its first coefficient followed by a local filter. Our filter shares this established mechanism. The additional step is a spectrum that reproduces itself after multiplication by a uniform $`d`$-level distribution, together with the optimal energy asymptotics.

## Entanglement embezzlement

[van Dam and Hayden (2003)](https://doi.org/10.1103/PhysRevA.67.060302), *Universal entanglement transformations without communication*, introduces universal approximate embezzlement; its preprint is [quant-ph/0201041v1](https://arxiv.org/abs/quant-ph/0201041v1). [Leung and Wang (2014)](https://doi.org/10.1103/PhysRevA.90.042331), inspected as [1311.6842v2](https://arxiv.org/abs/1311.6842v2), studies general universal embezzling families and alternatives to the original construction. These establish the broad phenomenon of borrowing entanglement with small joint disturbance and growing Schmidt support.

[Zanoni, Theurer and Gour (2024)](https://doi.org/10.22331/q-2024-06-13-1368), *Complete Characterization of Entanglement Embezzlement*, characterizes universal families under LOCC using pure-to-mixed conversion and a conversion distance. The inspected [2303.17749v3](https://arxiv.org/abs/2303.17749v3) is dated 10 April 2024. Definition 5 and Theorem 6 concern families that can approximately embezzle every finite-dimensional target. Here the target dimension is fixed and heralded destructive failure is admitted; the result evaluates success-dependent oscillator energy and its dependence on mode count. The universal-family characterization remains an important antecedent, with different operational parameters.

[Schwartzman (2025)](https://doi.org/10.1103/pfyl-hwf2), *Complexity of entanglement embezzlement*, derives circuit-complexity obstructions as accuracy or borrowed entanglement increases. The inspected preprint is [2410.19051v2](https://arxiv.org/abs/2410.19051v2). Its charged resource is operation complexity. The photon laws here concern initial inventory; preparing the catalyst, implementing its filter and supplying local control work can have additional costs.

## Energy restrictions and heralded catalysis

[Ng, Mančinska, Cirstoiu, Eisert and Wehner (2015)](https://doi.org/10.1088/1367-2630/17/8/085004), *Limits to catalysis in quantum thermodynamics*, gives error lower bounds under dimension and mean-energy restrictions for catalytic thermal operations. The [published paper](https://qutech.nl/wp-content/uploads/2017/03/Limits-to-catalysis-in-quantum-thermodynamics.pdf), especially Section 2.2 and Appendix D, is the comparison source; [1405.3039v1](https://arxiv.org/abs/1405.3039v1) is its preprint. The energy argument uses diagonal catalysts with a finite partition function, thermal-operation monotones and catalyst trace-distance error; Appendix D.2 treats state-dependent system transformations. The present LOCC task instead supplies an independent success requirement and tests the full conditional catalyst–target output. Its subcritical exact-success construction is compatible with those unconditional thermal-operation restrictions.

[Fang and Liu (2026)](https://doi.org/10.1038/s41467-026-72686-0), *One-shot distillation with constant overhead using catalysts*, shows how catalysts convert multi-shot resource distillation into one-shot protocols. The [published full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC13347000/) and current [2410.14547v3](https://arxiv.org/abs/2410.14547v3), revised 2 September 2026, were inspected. Theorem 7 trades fresh input count against success probability, starting from an existing multi-input distillation protocol and consuming at least one resource input. The paper also discusses catalyst loss on probabilistic failure. This establishes the broader heralding tradeoff. Here the initial catalyst is the only shared entanglement resource, its mode count is fixed, and its photon inventory is optimized; the fresh-input overhead theorem does not evaluate these costs.

[Donnadieu, Sekatski, Brunner and Barizien (2026)](https://arxiv.org/abs/2609.18570), *Catalytic Activation of Genuine Multipartite Entanglement and Nonlocality*, introduces a heralded conversion of mixtures into tensor products and applies it to supplied multipartite entangled states. This comparison uses the abstract of the announced version, [2609.18570v1](https://arxiv.org/abs/2609.18570v1); the full text was unavailable during this review. The supplied multipartite input and activation task distinguish the stated result from catalyst-only bipartite extraction. No detailed theorem-level comparison with its unavailable proofs is asserted.

## A related Gaussian task

[Gaussian Entanglement Borrowing](https://github.com/GoGoKo699/Gaussian-Entanglement-Borrowing) studies pure Gaussian catalysts, Gaussian LOCC and a fixed pure Gaussian target. Its [model](https://github.com/GoGoKo699/Gaussian-Entanglement-Borrowing/blob/18a3d6706e67553547e2b5f933d29eee65120abf/science/model.md) and [photon–mode tradeoff](https://github.com/GoGoKo699/Gaussian-Entanglement-Borrowing/blob/18a3d6706e67553547e2b5f933d29eee65120abf/science/tradeoff.md) were inspected at revision `18a3d6706e67553547e2b5f933d29eee65120abf`. They charge photon inventory and catalyst modes under a joint squared-fidelity return criterion, allowing positive-probability heralding. The shared question is how physical inventory constrains return with added entanglement. The catalyst spectra, allowed operations and target are different: $`\Phi_d`$ is a finite-dimensional target here. The two photon laws therefore compare distinct tasks and do not establish an operations advantage on one matched target.

## Scope of the comparison

The comparisons identify the inherited conversion criteria, filtering constructions, embezzlement framework and previous resource tradeoffs. The added conclusion is the fixed-mode success threshold and matched conditional-fidelity photon laws, with failure consumption explicit. The searches and source readings provide a bounded comparison with the works above. They do not constitute an exhaustive priority claim. Bibliographic records are in [references.bib](references.bib).
