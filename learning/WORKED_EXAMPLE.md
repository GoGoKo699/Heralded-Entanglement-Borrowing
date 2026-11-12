# A finite example with four occupied number states

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
