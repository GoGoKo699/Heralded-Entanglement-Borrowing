# Sharp accuracy costs for an arbitrary finite pure target

The [optimal exact spectrum](target_spectrum.md) determines the cost even when the catalyst and target need only be returned with joint squared fidelity at least $`1-\varepsilon`$. All parameters $`m,\lambda,s`$ are fixed before $`\varepsilon\downarrow0`$, with $`0\lt s\lt1`$. Write its decreasing probabilities as $`r_j`$ and its tails as $`R_k=\sum_{j>k}r_j`$.

Let $`q_s`$ solve $`\sum_i(s\lambda_i)^{q_s}=1`$ and put $`b_s=1/q_s-1`$. Then $`R_k=\Theta(k^{-b_s})`$. This page proves the matching law

| Regime | Optimal initial photons |
|---|---|
| $`b_s>1/m`$ | $`E_m(\varepsilon;s,\lambda)\to E_m(0;s,\lambda)\lt \infty`$ |
| $`b_s=1/m`$ | $`\Theta(\log(1/\varepsilon))`$ |
| $`b_s\lt 1/m`$ | $`\Theta(\varepsilon^{-[1/(m b_s)-1]})`$ |

The lower bound permits every protocol in the [model](model.md), including mixed retained success outputs. The upper bound uses finite Schmidt support and a local filter whose success probability is exactly $`s`$.

## 1. A robust comparison with the exact optimal tail

For an arbitrary source spectrum $`p`$, put $`q=(p\otimes\lambda)^\downarrow`$ and denote the two tails by $`P_k,Q_k`$, with $`P_0=Q_0=1`$. The [fidelity-to-tail proof](converse.md#the-tail-inequality) uses only the desired joint pure spectrum, so it applies to this target without a uniformity assumption:

```math
P_k\ge s\left(\sqrt{Q_k}-\sqrt{2\varepsilon}\right)_+^2.
```

Its treatment of pure complete branches, possibly entangled discarded environments, averaged successful fidelity and trace-norm closure is unchanged. The target-dependent step begins with an exact allocation identity. Selecting the largest $`k`$ entries from the $`d`$ sorted streams $`\lambda_i p`$ gives

```math
Q_k=
\min_{\substack{k_1,\ldots,k_d\ge0\\\sum_i k_i=k}}
\sum_{i=1}^d\lambda_i P_{k_i}.
```

All $`k_i`$ are integers. For fixed $`k`$ the minimum is over a finite set. The identity is valid for infinite summable spectra because each selected set is finite; ties can be allocated in any consistent way.

Set $`X_k=\sqrt{P_k}`$ and define, for nonnegative bounded sequences with coordinate zero fixed at one,

```math
\begin{aligned}
G(X)_0&=1,\\
G(X)_k&=\sqrt{s}\,
\min_{\sum_i k_i=k}
\left(\sum_i\lambda_i X_{k_i}^2\right)^{1/2}
\quad(k\ge1).
\end{aligned}
```

This map is coordinatewise monotone. It also obeys a one-sided Lipschitz estimate. If $`Y_j\le X_j+d_0`$ for every $`j\ge1`$, while $`Y_0=X_0=1`$, Minkowski's inequality in each weighted Euclidean norm gives

```math
G(Y)_k\le G(X)_k+\sqrt{s}\,d_0
\qquad(k\ge1).
```

The bound holds after taking minima, since every allocation satisfies it.

Let $`Y_k=\sqrt{R_k}`$ for the exact fixed-point spectrum. Its relation $`r_j=s(r\otimes\lambda)_j^\downarrow`$ for $`j\ge2`$ gives $`Y=G(Y)`$. The approximate inequality gives

```math
X_k\ge G(X)_k-\delta,
\qquad \delta=\sqrt{2s\varepsilon}.
```

Define $`d_0=\sup_{k\ge0}(Y_k-X_k)_+`$. It is finite and the zeroth-coordinate difference is zero. The preceding two inequalities imply

```math
d_0\le\sqrt{s}\,d_0+\delta.
```

Therefore every allowed approximate protocol satisfies the uniform robust tail bound

```math
\boxed{
P_k\ge
\left(\sqrt{R_k}
-\frac{\sqrt{2s\varepsilon}}{1-\sqrt{s}}\right)_+^2.
}
```

In particular,

```math
R_k\ge\frac{8s\varepsilon}{(1-\sqrt{s})^2}
\quad\Longrightarrow\quad P_k\ge R_k/4.
```

No independent error is accumulated at each Schmidt index or at each tree generation. The contraction controls the entire tail sequence at once. This is why it retains the sharp power exponent.

## 2. Energy lower bounds

Since $`R_k=\Theta(k^{-b_s})`$, a constant fraction of this tail is forced up to an index $`K_\varepsilon=\Theta(\varepsilon^{-1/b_s})`$. Constants depend only on the fixed success and target. The passive tail identity gives

```math
E(C)\ge
\frac12\sum_{k=1}^{K_\varepsilon}
(e_{k+1}-e_k)R_k.
```

To handle oscillator degeneracies, group these indices into dyadic blocks. At all sufficiently large $`\ell`$,

```math
\begin{aligned}
e_{2^{\ell+1}}-e_{2^\ell}
&=\Theta_m(2^{\ell/m}),\\
R_{2^{\ell+1}}
&=\Theta_{s,\lambda}(2^{-\ell b_s}).
\end{aligned}
```

The contribution from a whole block is thus bounded below by a fixed positive multiple of $`2^{\ell(1/m-b_s)}`$. When $`b_s=1/m`$, there are $`\Theta(\log(1/\varepsilon))`$ constant-order blocks. When $`b_s\lt 1/m`$, the last blocks give

```math
E(C)=\Omega_{m,s,\lambda}
\left(\varepsilon^{-[1/(m b_s)-1]}\right).
```

The bound is on the actual initial photon inventory because passive energy is a lower bound in arbitrary physical Schmidt bases. Local product work systems do not change that source spectrum.

## 3. A finite cutoff with success exactly s

Choose any integer $`D\ge2`$, write

```math
t_D=\sum_{j>D}r_j,
\qquad Z_D=1-t_D,
\qquad p_j^{(D)}=r_j/Z_D\quad(j\le D),
```

and set the remaining source coefficients to zero. Assign these probabilities to the ordered Fock basis on both sides. Its total initial photons are exactly

```math
E_D=\frac{2}{Z_D}\sum_{j=1}^D e_jr_j.
```

Let $`q^\infty=(r\otimes\lambda)^\downarrow`$ and $`q^{(D)}=(p^{(D)}\otimes\lambda)^\downarrow`$. The largest $`D`$ entries of $`q^\infty`$ use only source indices at most $`D`$. Indeed, for $`D\ge2`$,

```math
q_D^\infty=r_D/s
>r_D\ge r_{D+1}\lambda_1.
```

Every entry coming from a source index greater than $`D`$ is at most the rightmost term. Hence

```math
q_j^{(D)}=q_j^\infty/Z_D
\qquad(1\le j\le D).
```

Alice passes every nonroot component and uses the squared root factor

```math
k_D=1-\frac{1-s}{p_1^{(D)}}
=s\lambda_1+(1-s\lambda_1)t_D.
```

It lies in $`[0,1]`$. The filter success is exactly

```math
p_1^{(D)}k_D+\sum_{j=2}^D p_j^{(D)}=s.
```

Changing the infinite-catalyst root factor without renormalizing it would instead fall short of the promised success. The displayed adjustment is part of the finite protocol.

After the filter and local Schmidt reindexing, the output probabilities $`v^{(D)}`$ obey

```math
\begin{aligned}
v_j^{(D)}&=q_j^{(D)}&& (2\le j\le D),\\
v_1^{(D)}&=q_1^{(D)}+b_D,\\
b_D&=\sum_{j>D}q_j^{(D)}
=\frac{(1-s)t_D}{s(1-t_D)}.
\end{aligned}
```

The map places all omitted target mass at the first coefficient. Matching Schmidt bases gives the exact joint squared fidelity

```math
F_D=
\left[
1-q_1^{(D)}-b_D+
\sqrt{q_1^{(D)}(q_1^{(D)}+b_D)}
\right]^2.
```

In particular, $`F_D\ge(1-b_D)^2`$ and $`1-F_D\le2b_D`$. These are joint catalyst–target guarantees. The protocol uses one two-outcome local filter, one success announcement and finite local isometries; the target basis is known. Its failure is again a product state.

## 4. Matching inventory orders

The exact-spectrum bounds give

```math
t_D=\Theta_{s,\lambda}(D^{-b_s}).
```

Taking $`D=\Theta_{s,\lambda}(\varepsilon^{-1/b_s})`$ with a sufficiently large fixed coefficient makes $`2b_D\le\varepsilon`$. For a fully finite prescription, increase $`D`$ until the explicit tail condition $`2(1-s)t_D/[s(1-t_D)]\le\varepsilon`$ holds.

Since $`e_jr_j=\Theta(j^{1/m-1-b_s})`$ at large $`j`$,

```math
E_D=
\begin{cases}
O_{m,s,\lambda}(1),&b_s>1/m,\\
\Theta_{m,s,\lambda}(\log D),&b_s=1/m,\\
\Theta_{m,s,\lambda}(D^{1/m-b_s}),&b_s\lt 1/m.
\end{cases}
```

The critical and supercritical upper bounds match Section 2. At every positive error the Fock cutoff is finite. Its largest occupied local photon number is $`e_D=O_m(D^{1/m})`$. Neither its growth nor the local preparation/control complexity is charged by the mean inventory.

## 5. The exact subcritical limit

Below the threshold, $`2\sum_j e_jr_j`$ converges. The normalized cutoffs tend to that exact optimum, so they supply the required upper limit using finite catalysts. To prove the matching lower limit, consider errors tending to zero and nearly optimal sources with uniformly bounded energy. Passive energy then gives uniform spectral tightness:

```math
\sum_{j>K}p_j
\le\frac{E(C)}{2e_{K+1}}.
```

Because $`e_{K+1}\to\infty`$, a subsequence converges in $`\ell^1`$ to a normalized decreasing spectrum $`p`$. Tensoring and decreasing rearrangement are $`\ell^1`$ continuous. The approximate tail inequality therefore passes to the zero-error inequality at every fixed $`k`$. It implies $`p\prec r`$. Lower semicontinuity of the nonnegative energy sum yields

```math
\liminf_{\varepsilon\downarrow0}E_m(\varepsilon;s,\lambda)
\ge2\sum_j e_jr_j.
```

Combining with the cutoff upper limit proves

```math
\boxed{
\lim_{\varepsilon\downarrow0}E_m(\varepsilon;s,\lambda)
=E_m(0;s,\lambda)
=2\sum_j e_jr_j\lt \infty.
}
```

No convergence of optimizing LOCC maps is required. Above or at threshold, the matched divergent laws already rule out a bounded-energy vanishing-error sequence.

## 6. Uniform targets and boundaries

For $`\lambda_i=1/d`$, $`b_s=\log(1/s)/\log d`$. The exponent becomes

```math
\frac1{m b_s}-1
=\frac{\log(sd^{1/m})}{\log(1/s)},
```

recovering [the logarithmic-block calculation](construction.md) and [its converse](converse.md). Choosing $`D=d^L`$ recovers their explicit finite cutoffs and fidelity formula.

The theorem fixes the finite target spectrum, success and mode count before error tends to zero. It does not include arbitrary mixed initial catalysts, the deterministic endpoint $`s=1`$, uniform crossovers at a changing success or target, energy-conserving controls, efficient preparation, or an operational work/runtime advantage.

[Model](model.md) · [Exact spectrum](target_spectrum.md) · [Mode threshold](mode_threshold.md) · [Verification](../verification/README.md)
