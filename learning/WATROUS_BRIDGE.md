# From Watrous to heralded entanglement borrowing

Alice and Bob share an entangled oscillator state. They want an additional known pure entangled target and the original shared state back whenever a local measurement announces success. A failed attempt may consume the shared state. The scientific question is how the target's full Schmidt spectrum and promised success probability change the initial photon inventory needed for accurate joint return.

The educational anchor is John Watrous, [*The Theory of Quantum Information*](https://cs.uwaterloo.ca/~watrous/TQI/), Cambridge University Press, **2018**. The author's page identifies the edition and supplies its chapter manuscripts and errata. The section numbers below refer to that 2018 manuscript. The book develops finite-dimensional foundations; the oscillator limits and the energy law are supplied by this project.

Use this bridge alongside the [30-milestone map](MILESTONES.md) and the [worked examples](WORKED_EXAMPLE.md). The examples follow complete filters for a Bell target and an unequal target, including success probability, failure output, initial photons and joint fidelity. Specialists can start directly with the [model and theorems](../science/model.md).

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

The known target $`|T_\lambda\rangle`$ has fixed positive decreasing Schmidt probabilities $`\lambda=(\lambda_1,\ldots,\lambda_d)`$, with $`d\ge2`$. Its definition and product spectrum are developed in step 3 below.

### Root fidelity and squared joint fidelity

To keep the conventions distinct, denote the book's fidelity by $`F_W`$:

```math
F_W(\rho,\sigma)
=\left\|\sqrt\rho\sqrt\sigma\right\|_1.
```

This project tests a pure reference $`|T\rangle=|C\rangle\otimes|T_\lambda\rangle`$ and uses

```math
F_{\rm joint}
=\langle T|\rho_{\rm suc}|T\rangle
=F_W(\rho_{\rm suc},|T\rangle\langle T|)^2.
```

Consequently the promised error $`F_{\rm joint}\ge1-\varepsilon`$ means $`F_W\ge\sqrt{1-\varepsilon}`$. The associated purified distance is at most $`\sqrt\varepsilon`$. This square matters when translating a small overlap error into the exponent of an energy bound.

The reference contains both the returned catalyst and the target. A good target marginal alone does not test whether the catalyst was returned and decoupled. The state $`\rho_{\rm suc}`$ is normalized conditional on the announced success; its actual probability is at least the separately promised parameter $`s`$.

### Majorization and tail direction

For decreasing normalized spectra, $`p\prec q`$ means that every initial partial sum of $`p`$ is at most the corresponding sum of $`q`$. Equivalently, with

```math
P_k=\sum_{j>k}p_j,
\qquad Q_k=\sum_{j>k}q_j,
```

the inequalities become $`P_k\ge Q_k`$. This is the direction used for deterministic conversion: a more spread-out Schmidt spectrum can be converted to a more concentrated one. Heralded conversion instead has an average constraint that includes the success probability and the failure branch.

## The steps supplied by this project

### 1. From finite rank to finite mean energy

A finite-rank catalyst of rank $`D`$ would need to become a product of rank $`dD`$ to return exactly while adding $`T_\lambda`$. A local Kraus branch cannot increase Schmidt rank. Exact success at finite $`D`$ is therefore impossible.

An oscillator with finite mean photons can still have infinitely many nonzero Schmidt probabilities. The exact subcritical construction uses this distinction. At every positive requested error, [finite truncation](../science/target_accuracy.md) instead gives a finite-rank state and finite local operations. The passage to countable spectra is proved using bounded finite-index tails and nonnegative summation; it is not obtained by simply replacing a finite dimension symbol with infinity.

### 2. From LOCC to a success-weighted tail bound

For each fixed $`k`$, a pure-state Schmidt tail is one minus the sum of the $`k`$ largest reduced-state eigenvalues. That complement is concave. A local instrument leaves the other party's reduced state unchanged on average, so the average tail cannot increase.

At exact joint return, dropping the nonnegative failure contribution gives $`P_k\ge sQ_k`$. For approximate mixed success outputs, [the converse](../science/converse.md#the-tail-inequality) retains all local environments, compares complete pure branches with the desired output, and controls their square-root spectral distances. It establishes

```math
P_k\ge
s\left(\sqrt{Q_k}-\sqrt{2\varepsilon}\right)_+^2,
\qquad x_+=\max\{x,0\}.
```

This reduction is needed because a retained success output can be mixed and its discarded environment can contain entanglement. The proof also specifies how the bound passes to the allowed trace-norm limits of announced-success outputs.

### 3. The complete target spectrum replaces rank alone

Write the fixed known target in its Schmidt bases as

```math
|T_\lambda\rangle
=\sum_{i=1}^{d}\sqrt{\lambda_i}|i\rangle|i\rangle,
\quad \lambda_1\ge\cdots\ge\lambda_d>0,
\quad \sum_i\lambda_i=1.
```

We consider entangled targets with $`d\ge2`$. A maximally entangled $`d`$-level target has $`\lambda_i=1/d`$; a product target needs no borrowed entanglement. For source spectrum $`p`$, the joint reference spectrum is

```math
q(p)=\mathrm{sort}\{p_j\lambda_i:j\ge1,\ 1\le i\le d\}.
```

For uniform targets this repeats every $`p_j/d`$ exactly $`d`$ times and gives $`Q_{dk}=P_k`$. With unequal targets, different product streams interleave. Their known sorted labels replace the special quotient-and-remainder indexing.

### 4. A fixed point identifies the least costly exact catalyst

Set $`\delta_1=(1,0,\ldots)`$ and define

```math
\mathcal F_s(p)=(1-s)\delta_1+s\,q(p).
```

The extra mass is added to the first coordinate after sorting $`q(p)`$. Exact feasibility implies $`p\prec\mathcal F_s(p)`$. The map preserves majorization and contracts $`\ell^1`$ distance by at most $`s\lt 1`$. Its unique fixed point $`r`$ therefore majorizes every feasible source: iterate the comparison and pass each finite ordered sum to the limit.

More concentrated spectra cost less under increasing passive energies. Consequently $`r`$ minimizes the exact initial photon inventory over all allowed pure catalysts and LOCC protocols. Finding this optimizer is stronger than exhibiting one successful filter.

Its explicit coefficients form a rooted word forest. The root has weight

```math
A=\frac{1-s}{1-s\lambda_1}.
```

Every nonempty word $`(i_1,\ldots,i_k)`$ with $`i_1\ne1`$ contributes $`A s^k\lambda_{i_1}\cdots\lambda_{i_k}`$. Sort the root and all these coefficients decreasingly. Restricting the first letter avoids counting the branch already absorbed in the root. [Target spectra](../science/target_spectrum.md) proves normalization, the fixed-point identity and optimality, including ties.

Alice attenuates only the root amplitude by $`\sqrt{s\lambda_1}`$. The successful state has spectrum $`q(r)`$ and probability exactly $`s`$. Its known sorted product labels give local isometries producing $`|C^\star\rangle\otimes|T_\lambda\rangle`$. Failure has probability $`1-s`$ and leaves the product vacuum. These are unrestricted local controls; they are not asserted to conserve photons.

### 5. Weighted word counting determines the exact energy boundary

Put $`\beta_i=s\lambda_i`$. There is a unique $`q_s\in(0,1)`$ satisfying

```math
\sum_i\beta_i^{q_s}=1.
```

A tree vertex of weight $`w`$ has children of weights $`w\beta_i`$. Raising weights to $`q_s`$ makes their sum conserved at every split. Stop branches when they first cross a small threshold $`x`$. The stopped weights lie between fixed multiples of $`x`$, so their number is of order $`x^{-q_s}`$. The corresponding sorted spectrum and tail obey

```math
r_j=\Theta(j^{-1/q_s}),
\qquad R_k:=\sum_{j>k}r_j=\Theta(k^{-b_s}),
\qquad b_s=\frac1{q_s}-1.
```

This weighted counting replaces the uniform target's equal-size blocks. Constants depend on the fixed target and $`s`$.

For $`m`$ modes per party, the number of Fock states with at most $`h`$ photons is $`\binom{h+m}{m}`$. Their ordered energies satisfy $`e_j=\Theta_m(j^{1/m})`$. Passive assignment gives

```math
E_{\rm exact}=2\sum_j e_jr_j
=2\sum_{k\ge1}(e_{k+1}-e_k)R_k,
```

whenever the sum converges. The factor two counts both parties. [Spectral energy](../science/spectral_energy.md) justifies this rearrangement for arbitrary physical Schmidt bases and degenerate Fock levels.

Set $`q_*=m/(m+1)`$. The Rényi entropy of the ordinary target probability vector is, with natural logarithms,

```math
H_q(\lambda)=\frac{\log\sum_i\lambda_i^q}{1-q}.
```

The exact threshold is

```math
s_c(\lambda,m)
=\left(\sum_i\lambda_i^{q_*}\right)^{-1/q_*}
=\exp[-H_{q_*}(\lambda)/m].
```

Finite exact energy is possible precisely when $`s\lt s_c`$, equivalently $`b_s>1/m`$. Equality has logarithmically divergent energy and is excluded from exact finite-energy feasibility. For $`m=1`$, the unequal rank-two target $`\lambda=(0.9,0.1)`$ has $`s_c=0.625`$; a Bell target of the same rank has $`s_c=0.5`$. Thus rank alone cannot decide exact borrowing at $`s=0.6`$.

### 6. Approximate return inherits the optimal tails to an accuracy cutoff

The success-weighted fidelity-to-tail inequality from step 2 already uses an arbitrary desired pure spectrum $`q`$. It therefore applies without a uniform-target assumption.

The top $`k`$ product coefficients are selected from the $`d`$ sorted streams $`\lambda_i p`$. Allocating $`k_i`$ entries to stream $`i`$ gives

```math
Q_k=\min_{\substack{k_1+\cdots+k_d=k\\k_i\ge0}}
\sum_i\lambda_iP_{k_i},
\qquad P_0=1.
```

The associated square-root tail operator contracts one-sided uniform errors by $`\sqrt s`$. Comparing the arbitrary source with $`r`$ yields

```math
P_k\ge
\left(\sqrt{R_k}
-\frac{\sqrt{2s\varepsilon}}{1-\sqrt s}\right)_+^2.
```

Hence $`P_k`$ is at least a fixed fraction of $`R_k`$ while the latter exceeds a fixed multiple of $`\varepsilon`$, through $`k=\Theta(\varepsilon^{-1/b_s})`$. This [stability argument](../science/target_accuracy.md) supplies the unequal-target converse. The bound permits mixed retained success outputs, discarded local environments and the model's admitted LOCC closure.

For attainment, keep the $`D`$ largest fixed-point coefficients and normalize by $`1-t`$, where $`t=R_D`$. Adjust the root filter so success remains exactly $`s`$. After sorted reindexing, the successful spectrum equals the desired spectrum at indices $`2,\ldots,D`$ and moves the omitted target mass

```math
b=\frac{(1-s)t}{s(1-t)}
```

to its first entry. Its exact overlap gives $`1-F_{\rm joint}\le2b=O(t)`$. Thus $`D=\Theta(\varepsilon^{-1/b_s})`$ suffices with finite support and finite local operations at every positive error.

The [complete matched law](../science/target_accuracy.md) is:

| Fixed success promise | Optimal initial inventory as $`\varepsilon\downarrow0`$ |
|---|---|
| $`s\lt s_c(\lambda,m)`$ | Converges to $`E_{\rm exact}\lt \infty`$; the infinite-support optimum attains exact return. |
| $`s=s_c(\lambda,m)`$ | $`\Theta(\log(1/\varepsilon))`$. |
| $`s>s_c(\lambda,m)`$ | $`\Theta(\varepsilon^{-a})`$ with $`a=1/(m b_s)-1>0`$. |

Below threshold, bounded-energy compactness controls catalysts that change with accuracy. One must first pass fixed-index tail inequalities to a limit and then use lower semicontinuity of energy. This identifies the limiting optimum rather than merely giving one bounded construction.

## Recover the uniform target

For $`\lambda_i=1/d`$ the exponent equation becomes $`d(s/d)^{q_s}=1`$. Consequently

```math
b_s=\frac{\log(1/s)}{\log d},
\quad s_c=d^{-1/m},
\quad a=\frac{\log(sd^{1/m})}{\log(1/s)}.
```

The weighted words reduce to the original geometric blocks. For one mode per party the exact energy further simplifies to $`s(d-1)/(1-ds)`$ below $`s=1/d`$. The [Bell example](WORKED_EXAMPLE.md) preserves this specialization and its explicit quotient-and-remainder map; the unequal example shows why sorted product labels are needed more generally.

## Reading route and boundaries

Follow the [worked examples](WORKED_EXAMPLE.md), then [model](../science/model.md), [target spectra](../science/target_spectrum.md), [target accuracy](../science/target_accuracy.md) and [spectral energy](../science/spectral_energy.md). The original [construction](../science/construction.md), [converse](../science/converse.md), [exact success](../science/exact_success.md) and [mode threshold](../science/mode_threshold.md) retain the uniform specialization and its dependencies.

All asymptotic statements fix $`m`$, the full target spectrum $`\lambda`$ and $`0\lt s\lt 1`$ before sending the joint squared-infidelity to zero. The initial catalyst is pure. For the explicit filter, $`k`$ successive exact successes have probability $`s^k`$; failure consumes the catalyst. Mean photons, the number of modes, the largest occupied Fock level, preparation complexity and local control work are separate resources.

Watrous supplies the finite-dimensional foundation. The fixed-point optimizer, weighted word counting, Rényi threshold, approximate stability and sharp oscillator inventory law belong to the project's scientific account and its [research-level comparisons](../references/related_work.md). Mixed initial catalysts, energy-preserving controls, loss robustness, the deterministic endpoint $`s=1`$ and uniform varying-parameter limits remain separate questions.
