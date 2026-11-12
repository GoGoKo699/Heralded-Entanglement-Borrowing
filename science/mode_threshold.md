# The mode threshold comes from the density of states

The success threshold is determined by how many orthogonal catalyst states fit below a given excitation energy. For a fixed number of equal-frequency oscillator modes, that counting law turns the Schmidt-tail recurrence into a physical energy bound.

## 1. Counting low-energy oscillator states

For $`m`$ modes at one party, the number of Fock basis vectors with total photon number at most $`h\ge0`$ is

```math
N_m(h)
=
\#\{(n_1,\ldots,n_m)\in\mathbb N_0^m:
n_1+\cdots+n_m\le h\}
=
\binom{h+m}{m}.
\tag{1}
```

Enumerate the corresponding photon numbers with multiplicity as $`e_1\le e_2\le\cdots`$, with $`e_1=0`$. At fixed $`m`$,

```math
N_m(h)
=
\frac{h^m}{m!}\bigl(1+O_m(h^{-1})\bigr),
\qquad
e_j=(m!j)^{1/m}(1+o(1)).
\tag{2}
```

Thus $`e_j=\Theta_m(j^{1/m})`$ for $`j\ge2`$. Photon degeneracies are already included. The passive-energy lower bound is

```math
E(C)\ge2\sum_{j\ge1}e_jp_j,
\tag{3}
```

where $`p_j`$ are the catalyst's decreasing Schmidt probabilities. [Spectral energy](spectral_energy.md) proves this bound for arbitrary physical Schmidt bases.

## 2. Exact return forces tails at every rank scale

Let

```math
P_k=\sum_{j>k}p_j.
\tag{4}
```

For the desired catalyst and maximally entangled target, the product spectrum is $`q_j=p_{\lceil j/d\rceil}/d`$, so $`Q_{dk}=P_k`$.

At exact return, the [LOCC converse](converse.md) gives

```math
P_k\ge sQ_k,
\qquad
P_{dk}\ge sP_k.
\tag{5}
```

There is a nonzero seed, because

```math
P_1
\ge sQ_1
=
s\left(1-\frac{p_1}{d}\right)
\ge s\left(1-\frac1d\right).
\tag{6}
```

Iteration therefore forces

```math
P_{d^\ell}
\ge
s^\ell P_1
\qquad(\ell\ge0).
\tag{7}
```

These tails are a requirement on every allowed protocol, rather than a property imposed by the construction.

For any nonnegative increasing energy sequence with $`e_1=0`$, summation by parts gives

```math
\sum_{j\ge1}e_jp_j
=
\sum_{k\ge1}(e_{k+1}-e_k)P_k.
\tag{8}
```

The equality holds by monotone summation, including the possibility that both sides are infinite.

To use (7), group the indices in (8) into disjoint blocks $`d^\ell\le k<d^{\ell+1}`$. Since the tails decrease,

```math
\begin{aligned}
\sum_{k=d^\ell}^{d^{\ell+1}-1}
(e_{k+1}-e_k)P_k
&\ge
\bigl(e_{d^{\ell+1}}-e_{d^\ell}\bigr)
P_{d^{\ell+1}}.
\end{aligned}
\tag{9}
```

Although individual energy increments can vanish inside a degenerate shell, equation (2) implies

```math
e_{d^{\ell+1}}-e_{d^\ell}
=
\Theta_{m,d}\bigl(d^{\ell/m}\bigr)
\tag{10}
```

for all sufficiently large $`\ell`$. Substituting (7) into (9) shows that finite mean energy requires convergence of

```math
\sum_{\ell\ge0}
\bigl(sd^{1/m}\bigr)^\ell.
\tag{11}
```

Consequently exact return at finite energy is impossible when $`sd^{1/m}\ge1`$.

Conversely, the [self-similar exact construction](exact_success.md) assigns block mass proportional to $`s^\ell`$ at photon cost of order $`d^{\ell/m}`$. Its mean energy is finite when $`sd^{1/m}<1`$. This establishes the necessary and sufficient condition

```math
\boxed{
\text{Exact joint return at finite mean energy is possible}
\quad\Longleftrightarrow\quad
s<d^{-1/m}.
}
\tag{12}
```

The catalyst is pure and may have infinite Fock support. No statement about arbitrary mixed catalysts follows.

## 3. The same counting law determines approximate costs

At nonzero error, the tail recurrence becomes

```math
\sqrt{P_{dk}}
\ge
\sqrt{s}\,
\bigl(\sqrt{P_k}-\sqrt{2\varepsilon}\bigr)_+.
\tag{13}
```

For fixed $`0<s<1`$, [the converse](converse.md) proves that nonzero tails of order $`s^\ell`$ must persist through

```math
L_\varepsilon
=
\frac{\log(1/\varepsilon)}{\log(1/s)}
-O_{s,d}(1)
\tag{14}
```

rank scales. Inserting these forced tails into (8)–(10) gives

```math
E(C)
\ge
c_{m,s,d}
\sum_{\ell=\ell_0}^{L_\varepsilon}
\bigl(sd^{1/m}\bigr)^\ell,
\tag{15}
```

where $`\ell_0`$ is a fixed finite index.

The [finite construction](construction.md) attains the same sum with $`L=\log(1/\varepsilon)/\log(1/s)+O_{s,d}(1)`$. Thus the three different divergence classes in the [main theorem](model.md) follow from an ordinary geometric series:

- If $`sd^{1/m}<1`$, the energy stays bounded. It is also bounded away from zero at small error by (13) at $`k=1`$ and $`e_2=1`$.
- If $`sd^{1/m}=1`$, each forced rank scale has constant-order energy cost, producing $`\Theta(\log(1/\varepsilon))`$.
- If $`sd^{1/m}>1`$, the last forced rank scales dominate. Their cost is $`\Theta(\varepsilon^{-a_m})`$, where

```math
a_m
=
\frac{\log(sd^{1/m})}{\log(1/s)}
=
\frac{\log d}{m\log(1/s)}-1.
\tag{16}
```

The exponent and matching orders concern initial photon inventory at fixed $`m,d,s`$. They do not quantify the cost of preparing the high-rank state or implementing the local controls.

## 4. The minimum number of modes for exact finite-energy return

Solving (12) for the integer $`m`$ gives

```math
m>\frac{\log d}{\log(1/s)},
\qquad
\boxed{
m_{\min}^{\rm exact}(s,d)
=
\left\lfloor
\frac{\log d}{\log(1/s)}
\right\rfloor+1.
}
\tag{17}
```

The inequality is strict because the equality case has a divergent mean energy. For one Bell pair, $`d=2`$:

| Promised success $`s`$ | Minimum modes per party for exact return at finite mean energy |
|---|---:|
| $`1/4`$ | 1 |
| $`1/2`$ | 2 |
| $`3/4`$ | 3 |
| $`9/10`$ | 7 |

For example, one mode per party at success $`1/2`$ is precisely critical and needs logarithmically increasing mean energy as the error vanishes. Two modes per party put the same success promise below the threshold, permitting exact finite-energy return with infinite support.

For every fixed $`s<1`$ and finite $`d`$, some finite mode count satisfies (12). This statement does not give a uniform energy bound as $`s\to1`$ or as $`m`$ changes. The constants in the fixed-mode energy laws are allowed to depend on $`m`$.

## 5. Why the inventory must include modes and cutoff

Adding modes changes the low-excitation degeneracy. It changes the relation between Schmidt rank and mean photon number even though each mode has the same frequency. A mean-energy statement therefore needs its mode count.

All initially shared catalyst modes are counted in $`m`$. Local product ancillas used during LOCC do not change the initial shared Schmidt spectrum. Their availability does not bypass (3) or the tail recurrence.

The exact subcritical states have infinite support. Every positive-error construction has finite support, but its Fock cutoff grows with accuracy. Mean photons, mode count and cutoff are distinct quantities. [Interpretation](interpretation.md) explains how those distinctions affect the physical conclusion; [verification](../verification/README.md) describes finite checks of the formulas.

