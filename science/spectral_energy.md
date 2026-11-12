# The oscillator energy carried by a Schmidt spectrum

The energy budget in the [model](model.md) counts the initial photons in the shared catalyst. It is not a bound on local control work. This distinction lets us separate the spectrum of entanglement, which local operations cannot freely create, from the choice of physical Schmidt bases, which can only increase the least initial energy needed to realize that spectrum.

Each party has a fixed number $`m\geq1`$ of equal-frequency oscillator modes. We measure energy above vacuum in units of one photon. Let

```math
N_m=\sum_{a=1}^{m}a_a^\dagger a_a
```

be the local photon-number operator. The two parties share a pure catalyst with nonincreasing squared Schmidt coefficients

```math
p_1\geq p_2\geq\cdots\geq0,
\qquad \sum_{j\geq1}p_j=1.
```

Zero coefficients are appended when the Schmidt rank is finite. Define its index tail by

```math
P_k=\sum_{j>k}p_j,
\qquad k\geq0.
```

## Fock counting

The local eigenspace with exactly $`h`$ photons has dimension

```math
g_m(h)=\binom{h+m-1}{m-1}.
```

Consequently the number of Fock states with at most $`h`$ photons is

```math
A_m(h)=\sum_{u=0}^{h}g_m(u)=\binom{h+m}{m}.
```

List the eigenvalues of $`N_m`$ in nondecreasing order, including their multiplicities, as $`e_1,e_2,\ldots`$. Then

```math
e_j=\min\left\{h\in\mathbb N_0:
j\leq\binom{h+m}{m}\right\},
\qquad e_1=0.
```

For fixed $`m`$, polynomial Fock counting gives

```math
A_m(h)=\frac{h^m}{m!}\left(1+O_m(h^{-1})\right),
\qquad
e_j=(m!j)^{1/m}+O_m(1).
```

The additive remainder accounts for both integer excitation numbers and finite degeneracies. In particular, for sufficiently large $`j`$,

```math
c_m j^{1/m}\leq e_j\leq C_m j^{1/m}.
```

For one mode the exact expression is $`e_j=j-1`$.

## Passive Schmidt assignment

**Energy bound.** Every physical realization of the pure catalyst satisfies

```math
E=\langle N_{m,A}+N_{m,B}\rangle
\geq2\mu_m(p),
\qquad
\mu_m(p):=\sum_{j\geq1}e_jp_j.
```

Both sides of the inequality may be infinite. Equality is attainable by assigning the $`j`$th Schmidt vector on each side to the $`j`$th Fock basis state in the energy ordering.

To prove the bound, let $`\rho`$ be either local reduced state and let $`\Pi_h`$ project onto the local Fock states with at most $`h`$ photons. Its rank is $`A_m(h)`$. The Ky Fan variational principle gives

```math
\operatorname{Tr}(\rho\Pi_h)
\leq\sum_{j=1}^{A_m(h)}p_j.
```

The integer-valued spectral decomposition of the number operator and Tonelli's theorem therefore imply

```math
\begin{aligned}
\operatorname{Tr}(N_m\rho)
&=\sum_{h\geq0}\left[1-\operatorname{Tr}(\rho\Pi_h)\right]\\
&\geq\sum_{h\geq0}\sum_{j>A_m(h)}p_j\\
&=\sum_{j\geq1}e_jp_j.
\end{aligned}
```

The two reduced states of a pure bipartite catalyst have the same nonzero eigenvalues, so their bounds add. This argument does not assume that the actual Schmidt vectors are number states, nor that local controls conserve energy.

Local product ancillas do not change the initial Schmidt spectrum across Alice and Bob. A mixed local ancilla may be purified on the same side. It therefore cannot evade this initial-energy bound. An additional shared entangled state would change the input resource and is excluded by the [model](model.md).

## Tail energy identity

For every probability spectrum, summation by parts in its nonnegative form gives

```math
\boxed{
\mu_m(p)=\sum_{k\geq1}(e_{k+1}-e_k)P_k.
}
```

Indeed, substitute $`e_j=\sum_{k=1}^{j-1}(e_{k+1}-e_k)`$ and exchange the two nonnegative sums. The identity is valid without first assuming a finite mean. Degeneracies merely set some of the increments to zero.

For one mode this becomes the familiar first-moment identity

```math
\mu_1(p)=\sum_{k\geq1}P_k
=\sum_{j\geq1}(j-1)p_j.
```

## Geometric index blocks

Fix the target Schmidt dimension $`d\geq2`$. At large $`\ell`$, the ordered Fock energies obey

```math
\begin{aligned}
e_{d^{\ell+1}}-e_{d^\ell}
&=(m!)^{1/m}(d^{1/m}-1)d^{\ell/m}+O_m(1)\\
&\geq c_{m,d}d^{\ell/m}.
\end{aligned}
```

Thus there is an index $`\ell_0(m,d)`$ such that, for every integer $`L>\ell_0`$,

```math
\begin{aligned}
\mu_m(p)
&\geq\sum_{\ell=\ell_0}^{L-1}
\sum_{k=d^\ell}^{d^{\ell+1}-1}
(e_{k+1}-e_k)P_k\\
&\geq\sum_{\ell=\ell_0}^{L-1}
\bigl(e_{d^{\ell+1}}-e_{d^\ell}\bigr)P_{d^{\ell+1}}\\
&\geq c_{m,d}\sum_{\ell=\ell_0}^{L-1}
d^{\ell/m}P_{d^{\ell+1}}.
\end{aligned}
```

This is why finite degeneracies do not create a loophole in the [converse](converse.md): a whole geometric block still carries a definite total energy increment. If the tail at $`d^\ell`$ is bounded below by a constant times $`s^\ell`$, the energy is bounded below by a constant times

```math
\sum_{\ell\leq L}(d^{1/m}s)^\ell.
```

Conversely, placing a spectrum with mass $`O_{s,d}(s^\ell)`$ in the block $`d^{\ell-1}\lt j\leq d^\ell`$ costs at most a constant times the same sum. The [construction](construction.md) has exactly this form. The change from a convergent sum to a logarithmic or growing geometric sum yields the [mode-dependent threshold](mode_threshold.md).

## One-mode product identity

Let $`\Phi_d`$ be the fixed maximally entangled target. The Schmidt spectrum of the desired joint state $`\psi\otimes\Phi_d`$ is

```math
q_j=\frac1d\,p_{\lceil j/d\rceil}.
```

In particular, $`Q_{dk}=P_k`$, where $`Q_k=\sum_{j>k}q_j`$. For one oscillator per party, averaging the $`d`$ repeated positions gives the exact identity

```math
\begin{aligned}
\mu_1(q)
&=\sum_{i\geq1}\frac{p_i}{d}
\sum_{a=1}^{d}\bigl[d(i-1)+a-1\bigr]\\
&=d\mu_1(p)+\frac{d-1}{2}.
\end{aligned}
```

This affine relation produces the sharp one-mode [exact-success energy formula](exact_success.md). For $`m>1`$ the ordered energies have degeneracies and are not affine in the index, so this exact constant must not be reused. The asymptotic block bounds above still apply.

## Fixed mode count is part of the resource model

All statements take $`m`$ fixed. Increasing the number of shared catalyst modes changes the number of orthogonal states available at low photon number. For example, the one-photon subspace already has dimension $`m`$ locally. Unlimited free catalyst modes would therefore remove any mode-independent conclusion based on photon energy alone.

The [interpretation](interpretation.md) separates this inventory of shared catalyst modes from initially unentangled local work systems, and separates initial photon number from control work, gate count and preparation cost. None of these energy estimates supplies a physical implementation bound for the local filters or reindexings.

[Back to the scientific model](model.md) · [Arbitrary-LOCC converse](converse.md) · [Finite constructions](construction.md)
