# What the target spectrum changes

Alice and Bob want an entangled pair while keeping their shared reservoir usable on every announced success. A failed experiment may destroy that reservoir. The return guarantee compares the complete catalyst–target output with their desired product, so it tests both preparation and decoupling. The resource is the reservoir's initial mean photon inventory at a fixed physical mode count.

The central distinction is between the rank of the target and its actual entanglement spectrum. Two targets of the same rank can require different divergence classes of photon inventory under the same success promise.

## A biased pair and a Bell pair

Take one oscillator mode per party. A Bell target has Schmidt probabilities $`(1/2,1/2)`$ and critical success $`1/2`$. For the biased pure target

```math
|\phi\rangle=\sqrt{0.9}|00\rangle+\sqrt{0.1}|11\rangle,
```

the critical success is instead

```math
s_c=\frac1{(\sqrt{0.9}+\sqrt{0.1})^2}=\frac58.
```

Both targets have Schmidt rank two. At the same success promise $`s=0.6`$:

| Target | One-mode consequence as joint infidelity vanishes |
|---|---|
| Bell pair | Photon inventory must diverge as a power of inverse error. |
| Biased pair above | A finite-energy infinite-support catalyst permits exact joint return. |

The comparison concerns the prescribed target. Converting a biased pair into a Bell pair is a further probabilistic task and changes the total success promise. It does not invalidate the difference.

More generally, at fixed $`m`$ modes per party, the target spectrum enters through

```math
s_c(\lambda,m)=e^{-H_{m/(m+1)}(\lambda)/m}.
```

The density of oscillator states selects a Rényi order. At fixed rank, the uniform target has the smallest critical success, because it maximizes that Rényi entropy. Making the target less entangled can therefore change a fixed success promise from an infinite-energy boundary into a finite-energy regime.

## Why the spectrum and density of states meet

To return the catalyst and add a target, the desired Schmidt probabilities are all products $`p_j\lambda_i`$. For a uniform target these are equal copies of each source coefficient, which yields a simple rank-dilation recurrence. A nonuniform target branches the source into differently weighted streams.

The optimal exact catalyst solves this self-consistency problem. It has one largest coefficient and a weighted tree of smaller coefficients. A root-only local filter produces the product spectrum on success. The tree's branching pressure determines a tail exponent $`b_s`$ through

```math
\sum_i(s\lambda_i)^{q_s}=1,
\qquad b_s=1/q_s-1.
```

Meanwhile, $`m`$ oscillator modes have $`\binom{h+m}{m}`$ Fock states below photon number $`h`$. The $`j`$th ordered energy thus grows like $`j^{1/m}`$. Multiplying this physical growth by the optimal Schmidt tail gives the three regimes:

| Tail compared with energy growth | Optimal inventory |
|---|---|
| $`b_s>1/m`$ | Finite exact-return energy; finite cutoffs approach it. |
| $`b_s=1/m`$ | $`\Theta(\log(1/\varepsilon))`$ as error vanishes. |
| $`b_s\lt 1/m`$ | $`\Theta(\varepsilon^{-[1/(m b_s)-1]})`$. |

The [exact-spectrum proof](target_spectrum.md) shows that this is an optimum over all catalysts, rather than only a property of one chosen tree. The [accuracy proof](target_accuracy.md) shows that arbitrary mixed-output LOCC cannot evade the necessary tails at nonzero error.

## The Bell-pair formulas remain explicit

For one mode and a Bell target, exact success-conditioned return at every fixed $`0\lt s\lt1/2`$ has optimal total initial photons

```math
E=\frac{s}{1-2s}.
```

At $`s=1/4`$, this is $`1/2`$ photon in total. At $`s=1/2`$, the optimum grows logarithmically with inverse joint infidelity. At $`s=3/4`$, it grows as a power with exponent $`\log(3/2)/\log(4/3)`$. [Exact success](exact_success.md) gives the direct rational calculation, and [construction](construction.md) gives finite logarithmic-block examples.

More modes change the low-energy degeneracy. Exact finite-energy Bell borrowing at success $`1/2`$ needs at least two modes per party; success $`9/10`$ needs seven. [Mode threshold](mode_threshold.md) gives both this uniform-target formula and the general spectrum-dependent condition.

## What success and failure mean

The exact attaining filter returns the original catalyst and desired target in a product state on success. On failure, the catalyst becomes a separable vacuum. Repeating it for $`k`$ consecutive successes has probability $`s^k`$. The source is consumed once failure occurs. This is consistent with average entanglement monotonicity and does not create an indefinitely reusable entanglement supply.

Averaging success and failure produces a different output guarantee. Returning only the catalyst marginal while allowing target correlations also defines a different optimization. The stated joint fidelity is the condition used in every bound and construction.

## Mean inventory, support and implementation

At positive error, finite cutoffs of the optimal spectrum give a complete protocol with success exactly $`s`$. The required Schmidt rank can be chosen of order $`\varepsilon^{-1/b_s}`$, and the largest occupied photon number is of order at most its $`1/m`$ power. Even below threshold, a bounded mean inventory can coexist with increasingly rare high-photon components and a growing cutoff.

Exact zero-error return needs infinite Schmidt rank. A finite-rank catalyst cannot produce any entangled finite pure target while returning itself exactly on a nonzero-probability LOCC branch: the desired product has strictly larger Schmidt rank. Finite mean energy and finite Hilbert support are different requirements.

The theorem fixes the target spectrum, success and mode count before error tends to zero. It assumes a known pure catalyst and unrestricted local control. Photon inventory does not quantify preparation work, gate count, runtime, loss robustness, fault tolerance or an energy-conserving implementation. Arbitrary mixed initial catalysts and the deterministic endpoint are separate problems.

Stochastic conversion criteria, infinite-dimensional Schmidt tails and root-filter mechanisms are established foundations. [Related work](../references/related_work.md) distinguishes them from the exact spectrum optimization and sharp target-dependent energy frontier here.
