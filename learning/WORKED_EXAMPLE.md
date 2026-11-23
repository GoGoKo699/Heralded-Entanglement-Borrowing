# Worked borrowing filters: Bell and unequal targets

Both examples use one oscillator per party and four occupied number states. They charge the total initial mean photons, keep the success probability exact, and compare the whole successful output with the original catalyst tensor the requested target. The second example shows why two targets of the same Schmidt rank can have different exact finite-energy thresholds.

## Bell target: a four-state filter

Alice and Bob share one oscillator each. They want to extract the Bell state

```math
|\Phi_2\rangle
=\frac{|00\rangle+|11\rangle}{\sqrt2}
```

into two initially unentangled target qubits, while returning their shared oscillator state on an announced success. This example succeeds with probability $`s=1/4`$. Its successful output approximates the **joint** reference consisting of the original catalyst and the Bell pair.

The calculation follows the [finite construction](../science/construction.md), with target dimension $`d=2`$ and cutoff level $`L=2`$. The [Watrous bridge](WATROUS_BRIDGE.md) supplies the background on Schmidt decompositions, local instruments and fidelity. The probabilities below are squared Schmidt coefficients; the state amplitudes are their positive square roots.

## The shared state and its initial energy

The untruncated construction starts at $`6/7`$ and divides a coefficient by eight when passing to its next block. Its first four entries are

```math
\left(\frac67,\frac3{28},\frac3{224},\frac3{224}\right).
```

They sum to $`111/112`$. Keeping these four entries and dividing by that sum gives

```math
p=\left(\frac{32}{37},\frac4{37},\frac1{74},\frac1{74}\right).
```

Use these coefficients in increasing photon-number order on both sides:

```math
|C_2\rangle
=\sqrt{\frac{32}{37}}|0,0\rangle
+\sqrt{\frac4{37}}|1,1\rangle
+\sqrt{\frac1{74}}|2,2\rangle
+\sqrt{\frac1{74}}|3,3\rangle.
```

Here the two entries in $`|n,n\rangle`$ label Alice's and Bob's oscillators. The initial mean photon number in **both** oscillators is

```math
\begin{aligned}
E_2
&=2\left(
0\frac{32}{37}
+1\frac4{37}
+2\frac1{74}
+3\frac1{74}\right)\\
&=\frac{13}{37}
\approx0.35135135.
\end{aligned}
```

Each party's oscillator has mean $`13/74`$. Its highest occupied number state has three photons. Thus a small mean and a finite excitation cutoff describe different resources. The [energy account](../science/spectral_energy.md) explains why this increasing-energy assignment is optimal for the chosen Schmidt spectrum.

## One local filter produces the success flag

Alice attenuates only the vacuum component. On the occupied support, her success operator is

```math
K
=\sqrt{\frac{17}{128}}|0\rangle\langle0|
+\sum_{n=1}^{3}|n\rangle\langle n|.
```

Its squared vacuum amplitude is

```math
1-\frac{1-s}{p_1}
=1-\frac{3/4}{32/37}
=\frac{17}{128}.
```

All squared filter amplitudes lie between zero and one. The complementary operator $`\sqrt{I-K^\dagger K}`$ supplies a valid failure outcome. Alice tells Bob which outcome occurred.

| Initial photon number at each party | Initial probability | Unnormalized success probability | Probability conditioned on success |
| --- | --- | --- | --- |
| $`0`$ | $`32/37`$ | $`17/148`$ | $`17/37`$ |
| $`1`$ | $`4/37`$ | $`16/148`$ | $`16/37`$ |
| $`2`$ | $`1/74`$ | $`2/148`$ | $`2/37`$ |
| $`3`$ | $`1/74`$ | $`2/148`$ | $`2/37`$ |

The success column sums to

```math
\frac{17+16+2+2}{148}=\frac14.
```

Dividing by $`1/4`$ gives the conditional spectrum

```math
r=\frac1{37}(17,16,2,2).
```

Failure occurs only in the vacuum component, with probability

```math
\frac{32}{37}\left(1-\frac{17}{128}\right)
=\frac34.
```

On failure, the shared oscillator state is the product vacuum. The protocol promises return on success; the failure branch consumes the entanglement resource.

## Reindexing separates an oscillator and a target qubit

On success, each party coherently writes the parity of its local number into its target qubit and keeps the integer quotient in the oscillator:

```math
|n\rangle|0\rangle_T
\longmapsto
|\lfloor n/2\rfloor\rangle|n\bmod2\rangle_T,
\qquad n=0,1,2,3.
```

These four input vectors have four orthogonal outputs, so this finite-support map extends to a local unitary. It measures neither the number nor the target bit; it preserves their superposition.

The desired reference is $`|C_2\rangle\otimes|\Phi_2\rangle`$. Each original coefficient $`p_j`$ therefore appears twice, divided by two. The table lists local oscillator/target labels; Alice and Bob have the same labels in each Schmidt term.

| Ordered term | Oscillator number | Target bit | Desired probability $`q_j`$ | Actual successful probability $`r_j`$ |
| --- | --- | --- | --- | --- |
| $`1`$ | $`0`$ | $`0`$ | $`16/37`$ | $`17/37`$ |
| $`2`$ | $`0`$ | $`1`$ | $`16/37`$ | $`16/37`$ |
| $`3`$ | $`1`$ | $`0`$ | $`2/37`$ | $`2/37`$ |
| $`4`$ | $`1`$ | $`1`$ | $`2/37`$ | $`2/37`$ |
| $`5`$ | $`2`$ | $`0`$ | $`1/148`$ | $`0`$ |
| $`6`$ | $`2`$ | $`1`$ | $`1/148`$ | $`0`$ |
| $`7`$ | $`3`$ | $`0`$ | $`1/148`$ | $`0`$ |
| $`8`$ | $`3`$ | $`1`$ | $`1/148`$ | $`0`$ |

The absent desired terms have total probability

```math
b=4\frac1{148}=\frac1{37}.
```

The successful state matches terms two through four exactly and puts this missing mass at the first term: $`r_1=q_1+b`$. Notice that $`b=1/37`$ is the missing mass of the **desired doubled spectrum**. It differs from the $`1/112`$ mass removed when first truncating the infinite source.

## The joint fidelity is explicit

All amplitudes are positive in the same Schmidt basis. Their overlap is

```math
\begin{aligned}
\langle C_2|\langle\Phi_2|\psi_{\rm suc}\rangle
&=\sum_{j=1}^{8}\sqrt{q_jr_j}\\
&=\frac{4\sqrt{17}+16+2+2}{37}\\
&=\frac{20+4\sqrt{17}}{37}.
\end{aligned}
```

The squared joint fidelity and its infidelity are therefore

```math
\begin{aligned}
F_{\rm suc}
&=\frac{672+160\sqrt{17}}{1369}
\approx0.97275157,\\
\epsilon_2=1-F_{\rm suc}
&\approx0.02724843.
\end{aligned}
```

This compares the complete successful output with the original oscillator state **and** the Bell pair together. The general construction's convenient bound holds:

```math
\epsilon_2\le2b=\frac2{37}\approx0.05405405.
```

Success conditioning matters. If failed trials are retained in the output average, their vacuum/zero-target state has squared overlap $`q_1=16/37`$ with the same pure reference. The averaged fidelity is

```math
\begin{aligned}
F_{\rm avg}
&=\frac14F_{\rm suc}+\frac34\frac{16}{37}\\
&=\frac{612+40\sqrt{17}}{1369}
\approx0.56751222.
\end{aligned}
```

Thus the $`0.97275157`$ fidelity belongs to the announced successful quarter of trials. A failed trial does not return a reusable catalyst.

## Increasing the cutoff improves return accuracy

Repeat the same construction with $`L=3`$, so eight source number states are occupied. Its normalized source spectrum is

```math
p^{(3)}
=\left(\frac{128}{149},\frac{16}{149},
\frac2{149},\frac2{149},
\frac1{596},\frac1{596},\frac1{596},\frac1{596}\right).
```

The squared vacuum filter amplitude is $`65/512`$, the missing target mass is $`1/149`$, and the overlap becomes $`(84+8\sqrt{65})/149`$. The success probability remains exactly $`1/4`$.

| Source level | Schmidt rank | Highest photon number per party | Initial total mean photons | Conditional joint infidelity |
| --- | --- | --- | --- | --- |
| $`L=2`$ | $`4`$ | $`3`$ | $`13/37\approx0.35135135`$ | $`0.02724843`$ |
| $`L=3`$ | $`8`$ | $`7`$ | $`63/149\approx0.42281879`$ | $`0.00672607`$ |

The mean photons approach $`1/2`$ as the cutoff grows. The [exact-success result](../science/exact_success.md) gives this limiting value directly:

```math
E_0
=\frac{s(d-1)}{1-ds}
=\frac{1/4}{1-1/2}
=\frac12.
```

Every finite cutoff still has nonzero return error: a source of Schmidt rank $`D`$ cannot produce the exact desired rank $`2D`$ on a nonzero-success LOCC branch. Zero-error attainment below the threshold uses the infinite-support, finite-mean-energy state. The finite examples demonstrate how its mean energy can stay bounded while its cutoff increases.

The [verification script](../verification/run_checks.py) checks the same filter, vector overlap, conditional guarantee and energy accounting for several finite instances. Those calculations support the construction; the universal lower bound is the analytical [converse](../science/converse.md).


## Unequal target: the spectrum changes the feasibility boundary

Now request

```math
|T_\lambda\rangle
=\sqrt{\frac9{10}}|00\rangle
+\sqrt{\frac1{10}}|11\rangle
```

with success probability $`s=3/5`$. For one mode per party, the [general threshold](../science/target_spectrum.md) is

```math
s_c(\lambda,1)
=\frac1{(\sqrt{9/10}+\sqrt{1/10})^2}
=\frac58.
```

Thus $`s=3/5\lt 5/8`$ permits exact joint return at finite mean photons in the infinite-support limit. A Bell target also has rank two, but its threshold is $`1/2`$; at the same success probability its optimal inventory instead diverges as accuracy improves. The comparison concerns two different requested states, not an extra free conversion between them.

### Construct and truncate the optimal spectrum

Here the root weight and edge factors are

```math
A=\frac{1-s}{1-s\lambda_1}=\frac{20}{23},
\quad \beta_1=\frac{27}{50},
\quad \beta_2=\frac3{50}.
```

The optimal [word spectrum](../science/target_spectrum.md) consists of the root and all words starting with label $`2`$. Its four largest entries are the root and the words $`2,21,211`$:

```math
r_1=\frac{20}{23},\quad
r_2=\frac6{115},\quad
r_3=\frac{81}{2875},\quad
r_4=\frac{2187}{143750}.
```

Their sum is $`Z=138737/143750`$ and the omitted source tail is $`t=5013/143750`$. Renormalization gives the finite catalyst probabilities

```math
p=\frac1{138737}(125000,7500,4050,2187).
```

Assign these probabilities to $`|0,0\rangle,\ldots,|3,3\rangle`$, using their positive square roots as amplitudes. The initial total mean photons are

```math
E=2\sum_{j=1}^{4}(j-1)p_j
=\frac{44322}{138737}
\approx0.31946777.
```

Each local cutoff is three photons. This inventory is not the local work needed to implement the filter.

### Apply the adjusted root filter

The squared vacuum filter amplitude is

```math
\kappa
=1-\frac{1-s}{p_1}
=\frac{173763}{312500}.
```

Alice applies $`K=\sqrt\kappa\,|0\rangle\langle0|+\sum_{n=1}^{3}|n\rangle\langle n|`$ on the occupied support and announces its outcome. The success probability remains exactly

```math
p_1\kappa+\sum_{j=2}^{4}p_j
=1-(1-s)=\frac35.
```

The normalized successful spectrum is

```math
u=\frac1{138737}(115842,12500,6750,3645).
```

Failure comes only from the attenuated root. It has probability $`2/5`$ and leaves the product vacuum. Retaining that failure output would change the operational fidelity being reported.

### Sort the desired product labels

The desired product spectrum contains the eight numbers $`p_j\lambda_i`$. Its four largest entries are shown with the actual successful coefficients:

| Ordered entry | Catalyst index in the desired output | Target Schmidt label | Desired probability | Actual successful probability |
|---:|---:|---:|---:|---:|
| $`1`$ | $`1`$ | $`1`$ | $`112500/138737`$ | $`115842/138737`$ |
| $`2`$ | $`1`$ | $`2`$ | $`12500/138737`$ | $`12500/138737`$ |
| $`3`$ | $`2`$ | $`1`$ | $`6750/138737`$ | $`6750/138737`$ |
| $`4`$ | $`3`$ | $`1`$ | $`3645/138737`$ | $`3645/138737`$ |

For example, the fourth term uses catalyst index $`3`$ and target label $`1`$. It is not the fourth entry of a repeated-pair list. Each party therefore maps its four occupied source states to local oscillator/target labels

```math
|0\rangle\mapsto|0\rangle|0\rangle_T,\quad
|1\rangle\mapsto|0\rangle|1\rangle_T,
```

```math
|2\rangle\mapsto|1\rangle|0\rangle_T,\quad
|3\rangle\mapsto|2\rangle|0\rangle_T.
```

These outputs are orthogonal, so this finite-support map extends to a local unitary with the target initialized in $`|0\rangle_T`$. No number measurement is made.

The four omitted desired coefficients are

```math
\frac1{1387370}(19683,7500,4050,2187).
```

Their total mass is

```math
b=\frac{3342}{138737}
=\frac{(1-s)t}{s(1-t)}.
```

The output agrees with desired entries two through four and moves this omitted mass to entry one: $`u_1=q_1+b`$. The source tail $`t`$ and omitted product mass $`b`$ are different quantities, just as in the Bell example.

### Compute the complete joint overlap

In the aligned Schmidt basis,

```math
\langle C,T_\lambda|\psi_{\rm suc}\rangle
=\frac{22895+\sqrt{112500\cdot115842}}{138737}.
```

Therefore

```math
F_{\rm joint}\approx0.97588216,
\qquad 1-F_{\rm joint}\approx0.02411784.
```

The convenient general bound also holds:

```math
1-F_{\rm joint}\le2b\approx0.04817749.
```

The fidelity is conditional on the successful $`3/5`$ of attempts and includes the returned oscillator state as well as the unequal target. Enlarging the sorted cutoff gives error tending to zero at the same success probability. Because $`s\lt 5/8`$, its initial photon inventory converges to the finite exact optimum. No simple rational formula for that general unequal-target optimum is asserted here.

The [accuracy proof](../science/target_accuracy.md) establishes the all-size statement and its matching arbitrary-LOCC lower bound. The finite example illustrates the explicit construction and its resource accounting; it does not replace the proof.
