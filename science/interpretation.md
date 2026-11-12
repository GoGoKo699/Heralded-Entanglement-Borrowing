# What the heralding threshold means

Alice and Bob want a Bell pair while keeping their shared entangled reservoir usable. They promise that, whenever the experiment reports success, the returned reservoir and the Bell pair are jointly close to the desired product state. A failed experiment may destroy the reservoir. The [model](model.md) prices the reservoir's initial mean photon inventory and fixes its physical mode count.

## Success changes the divergence class

For one oscillator at each party and a Bell-pair target, the critical success probability is $`s_c=1/2`$. At every fixed $`0<s<1/2`$, exact success-conditioned return is possible with initial total photons

```math
E=\frac{s}{1-2s}.
```

This is the exact optimum for zero error when infinite-support pure catalysts are admitted, and the limiting optimum for finite-error approximations. It is an initial inventory, not the energy consumed in one trial. At $`s=1/2`$, the optimal inventory instead grows as $`\log(1/\varepsilon)`$. At $`1/2<s<1`$, it grows as a power of inverse joint infidelity. The [converse](converse.md) optimizes over all allowed LOCC protocols, rather than only the explicit filter.

| Fixed success requirement | One-mode Bell-pair consequence |
|---|---|
| $`s=1/4`$ | Exact return is attainable with $`E=1/2`$ initial photons in total. |
| $`s=1/2`$ | Bounded energy cannot make the joint error vanish; the matching cost is logarithmic. |
| $`s=3/4`$ | The matching cost is $`\Theta(\varepsilon^{-a})`$, with $`a=\log(3/2)/\log(4/3)`$. |

The limits keep success probability fixed. The constants need not stay bounded as success approaches the threshold or one. The results do not provide a uniform crossover in these parameters.

## Why photons and modes both matter

The initial Schmidt spectrum must have enough weight far down its ordered tail to supply both the old catalyst and the new target. Extracting a $`d`$-dimensional maximally entangled state replicates every catalyst Schmidt probability $`d`$ times. Successful LOCC must therefore retain a prescribed fraction of the tail at successively larger index scales. The [tail recurrence](converse.md) makes this requirement quantitative.

Converting an index into an energy depends on the available modes. For $`m`$ equal-frequency oscillator modes per party, the number of Fock states below excitation $`n`$ is $`\binom{n+m}{m}`$. The ordered local energy therefore grows like $`j^{1/m}`$. This density of states moves the threshold to

```math
s_c=d^{-1/m}.
```

The [mode law](mode_threshold.md) gives the resulting logarithmic and power costs. For a Bell pair, exact finite-energy return with success $`1/2`$ requires at least two modes per party; success $`9/10`$ requires at least seven. The boundary is strict: equality with the critical success does not permit finite-energy exact return.

Mode count cannot be left free in an energy-only statement. A growing number of modes supplies a growing low-energy degeneracy. Local product ancillas do not supply additional initial shared entanglement; they cannot replace the initial Schmidt-tail requirement.

## What happens on failure

The exact [self-similar construction](exact_success.md) returns the same catalyst on success and a separable vacuum state on failure. Its successes can be repeated, but $`k`$ consecutive exact successes have probability $`s^k`$. Once failure occurs, the initial entangled resource has been consumed. This is consistent with average entanglement monotonicity.

The success flag is part of the task. Averaging successful and failed branches gives a different output guarantee. Likewise, returning only the catalyst marginal while allowing correlations with the target defines a different optimization. Here a single joint fidelity tests catalyst return, target preparation and their decoupling.

## Finite approximations and implementation resources

Every positive-error upper bound uses a finite Schmidt cutoff $`D=d^L`$ and finite local operations. At fixed $`s<1`$, $`L=O(\log(1/\varepsilon))`$, so the cutoff is polynomial in inverse error, with an exponent depending on success probability. The [construction](construction.md) provides its normalized state, a bounded local filter, exact success probability and joint output fidelity.

Exact zero-error attainment below threshold uses infinite Schmidt rank even though its mean energy is finite. No finite-rank catalyst can exactly generate a nontrivial maximally entangled target and return itself with nonzero success: the desired Schmidt rank would be multiplied by $`d`$. Finite mean energy and finite Hilbert support are different requirements.

The charged inventory does not establish an efficient state-preparation method, a gate count, a control-work cost, an energy-conserving implementation, robustness to loss, or a fault-tolerance threshold. Initial catalyst purity is assumed. Arbitrary mixed initial catalysts and growing target dimension are outside the theorem.

## Relation to established conversion theory

Stochastic conversion criteria and infinite-dimensional polynomial-tail phenomena are established foundations. The root filter also uses a standard stochastic-conversion mechanism. The contribution here is the optimization of initial oscillator energy at fixed success and joint error, including the mode-dependent critical probability and matching accuracy exponents. [Related work](../references/related_work.md) separates this claim from deterministic embezzling families, thermal catalysis and catalytic distillation supplied with fresh noisy resources.
