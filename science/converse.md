# A converse for every allowed LOCC protocol

This page proves the energy lower bounds in the [model](model.md). It allows adaptive local operations and classical communication, discarded local environments, mixed conditional outputs, countably many outcomes and the specified trace-norm closure of LOCC. The initial shared catalyst is pure; an arbitrary mixed shared catalyst is a different optimization.

Write its sorted squared Schmidt coefficients as $`p=(p_j)_{j\geq1}`$ and define

```math
P_k=\sum_{j>k}p_j.
```

The desired joint pure state is $`T=\psi\otimes\Phi_d`$. Its sorted Schmidt probabilities and tails are

```math
q_j=\frac1d\,p_{\lceil j/d\rceil},
\qquad Q_k=\sum_{j>k}q_j,
\qquad Q_{dk}=P_k.
```

The announced success probability is at least a fixed $`s>0`$. Squared fidelity with a pure target means its Born probability: if $`\rho_{\mathrm{succ}}`$ is the normalized successful output, the error requirement is

```math
\langle T|\rho_{\mathrm{succ}}|T\rangle\geq1-\epsilon.
```

## The tail inequality

Every allowed protocol satisfies, for each finite $`k\geq1`$,

```math
\boxed{
P_k\geq s\left(\sqrt{Q_k}-\sqrt{2\epsilon}\right)_+^2.
}
```

Here $`x_+=\max\{x,0\}`$. This is the load-bearing inequality. It compares the original Schmidt tails with the tails required to return the catalyst and add the target on a successful branch. Failure outputs need not return the catalyst.

### Average monotonicity of a Schmidt tail

For a pure bipartite state, $`P_k`$ equals one minus the sum of the $`k`$ largest eigenvalues of either reduced state. The Ky Fan variational principle makes that sum convex, so its complement is concave. Under a local instrument, the average reduced state of the other party is unchanged. Concavity therefore gives

```math
P_k(\psi)\geq\sum_z t_z P_k(\phi_z),
```

for the complete pure branches $`\phi_z`$ of the instrument, with probabilities $`t_z`$. Applying this argument at each local step gives average monotonicity for an LOCC protocol. This is the Vidal-tail foundation; its infinite-dimensional extension and ensemble form are inherited from the works discussed in [related work](../references/related_work.md).

Every discarded local system can be retained as a local Stinespring environment during this argument. Local mixed ancillas can be purified on the same side. Thus complete branches can be treated as pure without assuming that the retained output itself is pure. The initial cross-party Schmidt spectrum remains $`p`$ because no extra shared entanglement is supplied.

### Schmidt affinity and discarded environments

Consider one successful complete branch $`|\phi_z\rangle`$, including its local environments. Let $`f_z`$ be its retained-system squared fidelity with $`|T\rangle`$. Projection onto $`|T\rangle`$ gives a normalized environment vector $`|\eta_z\rangle`$ such that

```math
\left|\langle\phi_z|T\otimes\eta_z\rangle\right|=\sqrt{f_z}.
```

When $`f_z=0`$, any normalized environment vector suffices for the bounds below. The vector $`\eta_z`$ may be entangled across Alice and Bob; treating it as a local product would be an unjustified restriction.

Let $`r^z`$ be the complete branch's sorted Schmidt probabilities, let $`a^z`$ be those of $`\eta_z`$, and let $`b^z`$ be the sorted distribution $`q\otimes a^z`$. The Schmidt-affinity inequality gives

```math
\sqrt{f_z}\leq\sum_j\sqrt{r_j^z b_j^z}.
```

This is the singular-value trace inequality applied to the two pure-state coefficient operators. It remains valid for countable Schmidt spectra by the Hilbert-Schmidt version of that inequality, or by finite-rank approximation.

Tensoring a probability distribution with another probability distribution can only decrease its ordered partial sums:

```math
\sum_{j=1}^{k}b_j^z\leq\sum_{j=1}^{k}q_j.
```

For a direct proof, any $`k`$ selected entries of $`q\otimes a^z`$ involve at most $`k`$ indices of $`q`$. At each such index the selected $`a^z`$ entries sum to at most one. Their total is therefore at most the sum of the $`k`$ largest entries of $`q`$. Taking the supremum over the selected entries proves the claim, including infinite spectra. Hence the $`k`$th tail of $`b^z`$ is at least $`Q_k`$.

Define the distance between the sorted square-root spectra by

```math
h_z^2:=\sum_j\left(\sqrt{r_j^z}-\sqrt{b_j^z}\right)^2.
```

Both spectra are normalized, so

```math
h_z^2\leq2-2\sqrt{f_z}\leq2(1-f_z).
```

The norm of a tail of a vector changes by at most the norm of the full difference. If $`R_k^z=\sum_{j>k}r_j^z`$, this yields

```math
\sqrt{R_k^z}\geq\sqrt{Q_k}-h_z.
```

### Averaging the successful branches

Let the actual success probability be $`u\geq s`$, and let $`w_z`$ be the conditional weights of its successful complete branches. Fidelity with a pure target is linear, so

```math
\sum_z w_z f_z\geq1-\epsilon,
\qquad
\sum_z w_z h_z^2\leq2\epsilon.
```

Minkowski's inequality applied to $`\sqrt{Q_k}\leq\sqrt{R_k^z}+h_z`$ gives

```math
\left(\sum_z w_zR_k^z\right)^{1/2}
\geq\left(\sqrt{Q_k}-\sqrt{2\epsilon}\right)_+.
```

Average Schmidt-tail monotonicity on the complete instrument, followed by discarding its nonnegative failure contribution, now gives

```math
P_k\geq u\sum_z w_zR_k^z
\geq u\left(\sqrt{Q_k}-\sqrt{2\epsilon}\right)_+^2
\geq s\left(\sqrt{Q_k}-\sqrt{2\epsilon}\right)_+^2.
```

Thus no assumption of a pure retained success state, a single success Kraus operator or deterministic recovery was used.

### Infinite outcomes and closure

The Schmidt tails lie in $`[0,1]`$. For countable outcomes the preceding sums therefore converge, and finite truncations extend the same inequalities by nonnegative or dominated convergence. Normal measurable instruments with continuous outcomes use the corresponding integrals and the same $`L^2`$ argument.

For clarity about limiting protocols, let $`\sigma_{\mathrm{succ}}`$ denote the unnormalized successful retained output. Put

```math
u=\operatorname{Tr}\sigma_{\mathrm{succ}},
\qquad
v=\langle T|\sigma_{\mathrm{succ}}|T\rangle.
```

The proof actually yields the continuous unnormalized statement

```math
P_k\geq
\left(\sqrt{uQ_k}-\sqrt{2(u-v)}\right)_+^2.
```

Both $`u`$ and $`v`$ are continuous under trace-norm convergence of the flagged output. Consequently the bound extends to the trace-norm closure of finite protocols specified in the [model](model.md), including a limit with actual success $`u\geq s`$ and $`v\geq u(1-\epsilon)`$. Merely having a sequence of success probabilities that tends to zero would not satisfy that promise. This argument concerns ordinary tensor-product systems and normal local instruments; it asserts no commuting-operator embezzlement result.

## A geometric tail recurrence

Since $`q_1=p_1/d\leq1/d`$, the tail inequality has a uniform seed:

```math
P_1\geq s\left(\sqrt{1-1/d}-\sqrt{2\epsilon}\right)_+^2.
```

Taking $`k=dn`$ and using $`Q_{dn}=P_n`$ gives

```math
\sqrt{P_{dn}}\geq\sqrt{s}
\left(\sqrt{P_n}-\sqrt{2\epsilon}\right)_+.
```

Let $`x_\ell=\sqrt{P_{d^\ell}}`$. For fixed $`0<s<1`$, iteration yields

```math
x_\ell\geq
s^{\ell/2}x_0
-\sqrt{2s\epsilon}\,
\frac{1-s^{\ell/2}}{1-\sqrt{s}}.
```

The formula follows from the weaker linear inequality $`x_{\ell+1}\geq\sqrt{s}x_\ell-\sqrt{2s\epsilon}`$, which remains valid when its right side is negative.

For sufficiently small $`\epsilon`$, depending only on fixed $`s,d`$, the seed satisfies

```math
x_0\geq b_{s,d}:=\tfrac12\sqrt{s(1-1/d)}>0.
```

Put $`B_s=\sqrt{2s}/(1-\sqrt{s})`$. Whenever

```math
s^{\ell/2}b_{s,d}\geq2B_s\sqrt{\epsilon},
```

the recurrence implies

```math
P_{d^\ell}\geq\frac{b_{s,d}^2}{4}s^\ell.
```

It follows that there is an integer cutoff

```math
L=\frac{\log(1/\epsilon)}{\log(1/s)}+O_{s,d}(1)
```

for which this bound holds for all $`0\leq\ell\leq L`$. An explicit valid cutoff is the floor of $`\log[b_{s,d}^2/(4B_s^2\epsilon)]/\log(1/s)`$, once this is nonnegative. The additive constant does not depend on the catalyst or protocol.

## Energy lower bounds for a fixed number of modes

The [spectral-energy bound](spectral_energy.md#geometric-index-blocks) converts the tail recurrence into

```math
E\geq c_{m,s,d}
\sum_{\ell=\ell_0}^{L-1}(d^{1/m}s)^\ell.
```

Changing the finitely many initial terms only changes constants. Let $`r=d^{1/m}s`$.

| Success regime | Consequence of the sum |
|---|---|
| $`r<1`$ | A positive energy lower bound; the [exact finite-energy construction](exact_success.md) applies. |
| $`r=1`$ | $`E=\Omega_{m,s,d}(\log(1/\epsilon))`$. |
| $`r>1`$, with $`s<1`$ | $`E=\Omega_{m,s,d}(\epsilon^{-a_m})`$, where $`a_m=\log(r)/\log(1/s)`$. |

In the last row, $`r^L`$ is a constant multiple of $`\epsilon^{-a_m}`$ because the uncertainty in $`L`$ is additive and bounded. Thus the proof establishes the power itself, without a missing logarithmic factor. The [finite constructions](construction.md) give the corresponding upper bounds; see the combined [threshold statement](mode_threshold.md).

These limits fix $`m,d,s`$ before sending $`\epsilon`$ to zero. In particular, the constants involving $`1-\sqrt{s}`$ do not give a uniform crossover when $`s`$ approaches one.

## Exact return and the mode threshold

At zero error the tail inequality reduces to

```math
P_k\geq sQ_k,
\qquad
P_{d^\ell}\geq s^\ell P_1,
\qquad
P_1\geq s(1-1/d)>0.
```

If $`d^{1/m}s\geq1`$, substituting these inequalities into the infinite energy-block sum makes that sum diverge. Hence finite initial energy is impossible at or above

```math
s_c=d^{-1/m}.
```

Below $`s_c`$, the [self-similar catalyst](exact_success.md) has finite energy and gives an exact successful return. This proves both directions of the threshold for pure initial catalysts.

There is also a separate finite-rank obstruction. If $`p`$ has finite positive rank $`R`$, then $`P_R=0`$, whereas $`q`$ has rank $`dR`$ and $`Q_R>0`$. The exact tail inequality at $`k=R`$ rules out every nonzero success probability. Exact finite-energy attainment therefore uses infinite Schmidt rank. At every strictly positive error, the [construction](construction.md) instead has finite rank.

## The sharp one-mode subcritical limit

For one mode, exact success and the [one-mode product identity](spectral_energy.md#one-mode-product-identity) imply

```math
\mu_1(p)=\sum_{k\geq1}P_k
\geq s\sum_{k\geq1}Q_k
=s\left[d\mu_1(p)+\frac{d-1}{2}\right].
```

For finite energy and $`0<s<1/d`$ this gives

```math
E\geq\frac{s(d-1)}{1-ds}.
```

The [exact construction](exact_success.md) attains the bound. To establish that the same value is the limit of the approximate optimum, one must also control catalysts that depend on $`\epsilon`$; substituting zero into a fixed-catalyst inequality alone would not suffice.

Let $`\epsilon_j\downarrow0`$ and choose protocols whose energies approach the approximate infima. The exact construction bounds these energies above by a fixed constant, up to an arbitrarily small optimization slack. Let $`p^{(j)}`$ be their sorted Schmidt spectra. Since physical energy is at least the passive energy, their first index moments satisfy

```math
\sum_{a\geq1}(a-1)p_a^{(j)}\leq C.
```

In particular, $`P_K^{(j)}\leq C/K`$. This uniform tail bound gives an $`\ell^1`$-convergent subsequence of the sorted probability vectors, with a normalized limit $`p`$. Lower semicontinuity gives

```math
\mu_1(p)\leq\liminf_j\mu_1(p^{(j)})<\infty.
```

At every fixed $`k`$, both $`P_k^{(j)}`$ and the repeated-spectrum tail $`Q_k^{(j)}`$ converge. Passing to the limit in the proved tail inequality gives $`P_k\geq sQ_k`$. Summing these nonnegative inequalities then yields the exact mean-index inequality for $`p`$, and therefore

```math
\liminf_{\epsilon\downarrow0}E_1(\epsilon;s,d)
\geq\frac{s(d-1)}{1-ds}.
```

The exact construction supplies the reverse inequality. Consequently

```math
\boxed{
\lim_{\epsilon\downarrow0}E_1(\epsilon;s,d)
=\frac{s(d-1)}{1-ds},
\qquad 0<s<1/d.
}
```

No convergence of the optimizing LOCC maps is needed for this argument: it uses compactness of the spectra and the necessary tail inequalities. For $`m>1`$, the threshold and orders remain proved, but this affine one-mode constant is not claimed.

## A lower bound at the deterministic boundary

For $`s=1`$ the recurrence becomes

```math
x_\ell\geq x_0-\ell\sqrt{2\epsilon}.
```

The seed is bounded below by a positive constant at sufficiently small error. Thus $`P_{d^L}`$ stays bounded below by a positive constant for an integer $`L=\Theta_d(\epsilon^{-1/2})`$. The passive energy then obeys

```math
E\geq2e_{d^L+1}P_{d^L}
\geq c_{m,d}\,d^{L/m}.
```

Equivalently,

```math
\log(1+E)=\Omega_{m,d}(\epsilon^{-1/2}).
```

This boundary lower bound is not a matching endpoint assertion in the main theorem, which fixes $`s<1`$. Taking $`s\uparrow1`$ inside its power formula is not justified. Deterministic embezzling families are discussed and credited in [related work](../references/related_work.md); the finite construction here is proved for each fixed $`s<1`$.

[Scientific model](model.md) · [Spectral energy](spectral_energy.md) · [Exact success](exact_success.md) · [Finite constructions](construction.md) · [Interpretation](interpretation.md)
