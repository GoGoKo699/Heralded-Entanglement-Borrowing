# Matching finite catalysts

The construction uses a geometrically weighted spectrum on logarithmic Schmidt-rank blocks. A two-outcome filter announces success with probability exactly $`s`$. After local reindexing, the successful state approximates the original catalyst and $`|\Phi_d\rangle`$ jointly.

Throughout, $`m\ge1`$, $`d\ge2`$ and $`0<s<1`$ are fixed. The [model](model.md) defines the charged inventory and allowed operations.

## 1. A normalized self-similar spectrum

Define

```math
A=\frac{1-s}{1-s/d}
=\frac{d(1-s)}{d-s}.
\tag{1}
```

For an index $`j\ge1`$, let $`\ell(j)=\lceil\log_d j\rceil`$, with $`\ell(1)=0`$, and put

```math
p_j^{(\infty)}
=
A\left(\frac{s}{d}\right)^{\ell(j)}.
\tag{2}
```

The root is $`p_1^{(\infty)}=A`$. For $`\ell\ge1`$, block $`\ell`$ consists of

```math
d^{\ell-1}<j\le d^\ell,
\qquad
n_\ell=(d-1)d^{\ell-1}
\tag{3}
```

equal entries. Its probability mass is $`A(d-1)s^\ell/d`$. Therefore

```math
\sum_{j\ge1}p_j^{(\infty)}
=
A\left[
1+\frac{d-1}{d}\frac{s}{1-s}
\right]
=1.
\tag{4}
```

This is a decreasing probability sequence. For every $`j\ge2`$ it obeys

```math
p_j^{(\infty)}
=
\frac{s}{d}\,
p_{\lceil j/d\rceil}^{(\infty)}.
\tag{5}
```

Normalization holds for every $`s<1`$, even when the associated mean photon number is infinite. Finite truncations below always have finite energy.

## 2. A finite cutoff and a physical catalyst

Choose an integer $`L\ge1`$ and set $`D=d^L`$. The mass omitted above index $`D`$ is

```math
t_L
=
\sum_{j>D}p_j^{(\infty)}
=
\frac{d-1}{d-s}s^{L+1}.
\tag{6}
```

Let $`Z_L=1-t_L`$ and define

```math
p_j^{(L)}
=
\begin{cases}
p_j^{(\infty)}/Z_L,&1\le j\le D,\\
0,&j>D.
\end{cases}
\tag{7}
```

Enumerate the $`m`$-mode Fock basis at either party in nondecreasing total photon number. Write its vectors as $`|f_j\rangle`$ and its photon numbers as $`e_j`$, so $`e_1=0`$. The finite catalyst is

```math
|C_L\rangle
=
\sum_{j=1}^{D}
\sqrt{p_j^{(L)}}\,
|f_j\rangle_A|f_j\rangle_B.
\tag{8}
```

Its initial total photon number is exactly

```math
E_{m,L}
=
2\sum_{j=1}^{D}e_jp_j^{(L)}.
\tag{9}
```

Both its Schmidt rank $`D`$ and its physical Fock support are finite. No additional shared state is used.

## 3. A root-only filter with exact success probability

Alice measures the catalyst with success operator

```math
K_L
=
\sqrt{k_L}\,|f_1\rangle\langle f_1|
+
\sum_{j=2}^{D}|f_j\rangle\langle f_j|,
\qquad
k_L=1-\frac{1-s}{p_1^{(L)}}.
\tag{10}
```

The operator may be extended arbitrarily as a contraction outside the occupied support. Since

```math
k_L
=
\frac{s}{d}
+
\left(1-\frac{s}{d}\right)t_L,
\tag{11}
```

it lies in $`[0,1]`$. The complementary filter is a valid local failure outcome. The success probability is exactly

```math
\begin{aligned}
p_{\rm suc}
&=
p_1^{(L)}k_L+\sum_{j=2}^{D}p_j^{(L)}\\
&=
p_1^{(L)}-(1-s)+1-p_1^{(L)}
=s.
\end{aligned}
\tag{12}
```

Alice announces this one-bit outcome. Conditional on success, the pure state's Schmidt probabilities are

```math
r_j^{(L)}
=
\begin{cases}
[p_1^{(L)}-1+s]/s,&j=1,\\
p_j^{(L)}/s,&2\le j\le D,\\
0,&j>D.
\end{cases}
\tag{13}
```

The failure state is the product Fock vacuum: only the root has nonzero failure amplitude.

## 4. Local reindexing and exact fidelity

The desired pure reference $`|C_L\rangle\otimes|\Phi_d\rangle`$ has decreasing Schmidt probabilities

```math
q_j^{(L)}
=
\frac1d\,p_{\lceil j/d\rceil}^{(L)},
\qquad
1\le j\le dD.
\tag{14}
```

Both parties apply the local reindexing

```math
|f_j\rangle|0\rangle_T
\longmapsto
|f_{\lceil j/d\rceil}\rangle
|(j-1)\bmod d\rangle_T,
\qquad
1\le j\le D.
\tag{15}
```

On this finite occupied subspace, it is an isometry and extends to a finite-dimensional local unitary after completing the unused basis vectors. It uses no communication beyond the success announcement.

For every $`2\le j\le D`$, equations (5), (7) and (13) give

```math
r_j^{(L)}=q_j^{(L)}.
\tag{16}
```

Define the omitted *target* mass

```math
\begin{aligned}
b_L
&=
\sum_{j>D}q_j^{(L)}
=
\sum_{i>D/d}p_i^{(L)}\\
&=
\frac{(d-1)(1-s)}{d-s}\,
\frac{s^L}{Z_L}.
\end{aligned}
\tag{17}
```

The successful spectrum moves precisely this mass to the root:

```math
r_1^{(L)}=q_1^{(L)}+b_L.
\tag{18}
```

Consequently the actual joint squared fidelity is

```math
F_L
=
\left[
1-q_1^{(L)}-b_L+
\sqrt{q_1^{(L)}\bigl(q_1^{(L)}+b_L\bigr)}
\right]^2.
\tag{19}
```

This compares the complete physical output with the original finite catalyst and target. It does not merely compare the target marginal.

Since the square-root term in (19) is at least $`q_1^{(L)}`$,

```math
1-F_L\le2b_L.
\tag{20}
```

Also $`Z_L\ge A`$, because the truncated spectrum contains the root. Thus

```math
b_L\le\frac{d-1}{d}s^L,
\qquad
1-F_L
\le
\frac{2(d-1)}d\,s^L.
\tag{21}
```

At fixed $`s,d`$, $`q_1^{(L)}\to A/d>0`$ and $`b_L=\Theta_{s,d}(s^L)`$. Expanding (19) around $`b_L=0`$ further gives $`1-F_L=b_L+O_{s,d}(b_L^2)`$. The stated error scale is therefore attained by this family.

## 5. Photon inventory and the three regimes

Fock counting gives $`e_j=\Theta_m(j^{1/m})`$ for $`j\ge2`$; see [spectral energy](spectral_energy.md). On block $`\ell`$, all indices have order $`d^\ell`$. Equations (2), (3), (7) and (9) imply

```math
E_{m,L}
=
\Theta_{m,s,d}
\left(
\sum_{\ell=1}^{L}
\bigl(sd^{1/m}\bigr)^\ell
\right).
\tag{22}
```

The bounds hold with constants independent of $`L`$. In particular, for $`g=sd^{1/m}`$,

```math
E_{m,L}
=
\begin{cases}
\Theta_{m,s,d}(1),&g<1,\\
\Theta_{m,d}(L),&g=1,\\
\Theta_{m,s,d}(g^L),&g>1.
\end{cases}
\tag{23}
```

A requested error $`0<\varepsilon<1`$ is met by taking

```math
L=
\left\lceil
\frac{\log\!\left(2(d-1)/(d\varepsilon)\right)}
{\log(1/s)}
\right\rceil.
\tag{24}
```

Substituting this into (23) gives a bounded photon inventory below the threshold, a logarithm at the threshold and

```math
E_{m,L}
=
O_{m,s,d}
\left(
\varepsilon^{-\log(sd^{1/m})/\log(1/s)}
\right)
\tag{25}
```

above it. [The converse](converse.md) proves the matching lower orders.

For one oscillator per party, the finite inventory also has the exact expression

```math
E_{1,L}
=
\frac{A(d-1)}{dZ_L}
\left[
\frac{d+1}{d}
\sum_{\ell=1}^{L}(ds)^\ell
-
\sum_{\ell=1}^{L}s^\ell
\right].
\tag{26}
```

This follows by summing the consecutive photon numbers $`j-1`$ in each block. When $`ds<1`$, it tends to $`s(d-1)/(1-ds)`$, the sharp [exact-success budget](exact_success.md).

## 6. The cutoff remains a resource

The finite-rank implementation has

```math
D=d^L
=
O_{s,d}
\left(
\varepsilon^{-\log d/\log(1/s)}
\right).
\tag{27}
```

Its largest occupied total photon number at either party is $`e_D=O_m(D^{1/m})`$. A bounded *mean* inventory below threshold therefore coexists with a growing cutoff and increasingly rare high-energy components. The construction does not claim bounded support, efficient preparation or an efficient implementation of the local reindexing.

At exact zero error below threshold, the infinite spectrum (2) is used instead. [Exact success](exact_success.md) describes the corresponding local dilation and explains why finite rank cannot attain exact return.

