# The target spectrum determines the exact optimum

Fix a finite pure target with positive decreasing Schmidt probabilities $`\lambda=(\lambda_1,\ldots,\lambda_d)`$, where $`d\ge2`$. The mode count and success promise $`0\lt s\lt1`$ are fixed. The [model](model.md) specifies the photon inventory, joint return criterion and allowed LOCC protocols.

The optimal exact catalyst has an explicit spectrum. It minimizes every passive spectral-energy cost at once. Combining its tail with oscillator state counting gives the critical success probability

```math
s_c(\lambda,m)
=\left(\sum_{i=1}^d\lambda_i^{m/(m+1)}\right)^{-(m+1)/m}.
```

The proof separates a general stochastic-conversion principle from its physical energy consequence.

## 1. Exact return as a majorization inequality

Let $`p=(p_j)_{j\ge1}`$ be the decreasing squared Schmidt coefficients of any pure source catalyst. Write

```math
\begin{aligned}
q(p)&=(p\otimes\lambda)^\downarrow,\\
P_k&=\sum_{j>k}p_j,
&Q_k&=\sum_{j>k}q_j(p).
\end{aligned}
```

A down arrow denotes decreasing rearrangement, with multiplicity. The [general tail inequality](converse.md#the-tail-inequality) at zero error gives $`P_k\ge sQ_k`$ for every finite $`k\ge1`$. It includes mixed retained success outputs and discarded environments under the stated LOCC closure.

For decreasing probability vectors, use $`p\prec u`$ to mean that every ordered partial sum of $`p`$ is no larger than the corresponding partial sum of $`u`$. Define

```math
F_s(p)=(1-s)\delta_1+s\,q(p),
```

where the extra mass is added to the first coordinate. This vector is already decreasing and normalized. Exact return necessarily implies

```math
p\prec F_s(p).
```

The Schmidt-tail condition and the first-coordinate construction are established stochastic-conversion ingredients; see [related work](../references/related_work.md). The additional step here is to solve the self-consistency problem and optimize the physical inventory.

### Monotonicity and contraction

The map $`F_s`$ preserves majorization. Tensoring by a fixed probability vector preserves majorization: the largest $`k`$ entries of $`p\otimes\lambda`$ can be chosen by allocating $`k_i`$ entries to each sorted stream $`\lambda_i p`$, with $`\sum_i k_i=k`$. Each candidate sum is a weighted sum of ordered partial sums of $`p`$. Adding the same first-coordinate mass then preserves all the resulting inequalities.

Decreasing rearrangement is nonexpansive in $`\ell^1`$. For finite lists this follows by uncrossing any pairing of oppositely ordered entries in the sum of absolute differences; summable infinite lists follow by truncation. Consequently

```math
\begin{aligned}
\|F_s(p)-F_s(u)\|_1
&\le s\|p\otimes\lambda-u\otimes\lambda\|_1\\
&=s\|p-u\|_1.
\end{aligned}
```

The space of decreasing probability sequences is closed in $`\ell^1`$ and complete. Since $`s\lt1`$, the contraction has a unique fixed point $`r=r(s,\lambda)`$. For an exactly feasible source,

```math
p\prec F_s(p)\prec F_s^2(p)\prec\cdots.
```

The iterates converge in $`\ell^1`$ to $`r`$. Passing to each finite partial sum proves

```math
\boxed{p\prec r.}
```

Thus every exactly feasible catalyst is at least as spread out in Schmidt index as this one fixed spectrum.

## 2. An explicit weighted-word spectrum

Choose one largest target coefficient as $`\lambda_1`$; ties cause no problem. Put

```math
A=\frac{1-s}{1-s\lambda_1},
\qquad \beta_i=s\lambda_i.
```

Form the following multiset, keeping a separate entry for every word:

- One root with weight $`A`$.
- For every word $`w=(i_1,\ldots,i_\ell)`$, $`\ell\ge1`$, whose first symbol satisfies $`i_1\ne1`$, one weight

```math
r_w=A\prod_{a=1}^{\ell}\beta_{i_a}.
```

Sort this multiset decreasingly to obtain $`r`$. Equal numerical values retain their multiplicity. Its normalization follows from

```math
A\left[1+\frac{s(1-\lambda_1)}{1-s}\right]=1.
```

The root is largest. Multiplying every entry by every $`\lambda_i`$ gives a useful exact multiset identity:

```math
r\otimes\lambda
=\{A\lambda_1\}
\;\sqcup\;
\{r_w/s:\ w\ne\varnothing\}.
```

Here $`\sqcup`$ is union with multiplicity. The root terms with $`i\ne1`$ produce words of length one; multiplying a nonroot word by a target coefficient appends one symbol. The remaining root term is $`A\lambda_1`$. It is largest because all other entries are at most $`A\lambda_1`$.

If $`q=(r\otimes\lambda)^\downarrow`$, this proves

```math
q_1=A\lambda_1,
\qquad q_j=r_j/s\quad(j\ge2),
```

and hence $`r=F_s(r)`$. The multiset is therefore the unique fixed point identified above.

### Exact physical protocol

Assign $`r_j`$ to the $`j`$th Fock state at each party, ordered by increasing total photons. Alice's success filter has squared diagonal factors

```math
K_1^2=s\lambda_1,
\qquad K_j^2=1\quad(j\ge2).
```

It is a bounded contraction. Since $`r_jK_j^2=sq_j`$ at every index, success has probability exactly $`s`$. On success, both parties reindex their Schmidt bases according to the sorted pairs in $`r\otimes\lambda`$. The resulting state is exactly the original catalyst tensored with the target. Known local target bases are included in these local isometries. The failure branch contains only the root and is the product Fock vacuum.

The countable reindexing is an allowed isometry. A local unentangled flag gives a unitary dilation by the same complement-basis argument as in [the uniform construction](exact_success.md#local-dilation). No finite-gate, bounded-work or energy-conserving implementation is asserted. Positive-error versions use finite support and finite-dimensional operations; see [the accuracy construction](target_accuracy.md#3-a-finite-cutoff-with-success-exactly-s).

## 3. Universal exact passive-energy optimum

Let $`e_1\le e_2\le\cdots`$ be any nonnegative increasing energy sequence with $`e_1=0`$. For a source spectrum $`p`$,

```math
\sum_{j\ge1}e_jp_j
=\sum_{k\ge1}(e_{k+1}-e_k)P_k.
```

The identity uses only nonnegative summation, so infinite values are allowed. Since $`p\prec r`$, its tails obey $`P_k\ge R_k`$, where $`R_k=\sum_{j>k}r_j`$. Therefore

```math
\sum_{j\ge1}e_jp_j\ge\sum_{j\ge1}e_jr_j.
```

For the actual oscillator inventory, [passive Schmidt assignment](spectral_energy.md#passive-schmidt-assignment) bounds both parties' energy below by this sum and attains it in matched Fock bases. Thus

```math
\boxed{
E_m(0;s,\lambda)=2\sum_{j\ge1}e_jr_j.
}
```

If the series diverges, no finite-energy exact protocol exists. If it converges, the root-filter protocol attains the minimum. The optimum is a spectrum sum at every fixed $`m`$, not generally an elementary expression. It is an exact zero-error result; it does not identify the exact optimum at each positive error.

## 4. The tail exponent from weighted tree counting

There is a unique $`q_s\in(0,1)`$ satisfying

```math
\boxed{\sum_{i=1}^d(s\lambda_i)^{q_s}=1.}
```

Indeed, the sum is continuous and strictly decreasing in its exponent, equals $`d>1`$ at zero and $`s\lt1`$ at one. Define

```math
b_s=\frac1{q_s}-1>0.
```

Consider a full weighted $`d`$-ary tree with root weight $`B>0`$ and child factors $`\beta_i`$. At a small threshold $`x\lt B`$, stop each branch at its first weight below $`x`$. This is a finite tree because every child factor is at most $`s\lambda_1\lt1`$. Each stopping leaf has weight between $`\beta_{\min}x`$ and $`x`$, with a harmless choice of strict endpoint convention.

Splitting a node conserves the sum of its children's $`q_s`$ powers. The stopping leaves consequently have total $`q_s`$ mass $`B^{q_s}`$. Their number is bounded above and below by fixed positive multiples of $`x^{-q_s}`$. A finite full $`d`$-ary tree with $`I`$ internal vertices and $`L`$ leaves satisfies $`L=(d-1)I+1`$. Thus the number of tree vertices of weight at least $`x`$ is also $`\Theta(x^{-q_s})`$.

The nonroot catalyst weights are a finite forest of these trees, rooted at $`A\beta_i`$ for $`i\ne1`$. Hence, as $`x\downarrow0`$,

```math
\#\{j:r_j\ge x\}=\Theta_{s,\lambda}(x^{-q_s}).
```

Inverting the counting bounds and summing the resulting power tail gives

```math
\begin{aligned}
r_j&=\Theta_{s,\lambda}(j^{-1/q_s}),\\
R_k&=\Theta_{s,\lambda}(k^{-b_s}).
\end{aligned}
```

These are two-sided order bounds. Ties or arithmetic relations between the $`\log\beta_i`$ do not require a limiting leading coefficient and do not change the exponents.

## 5. Oscillator threshold and Rényi entropy

For $`m`$ equal-frequency modes, ordered Fock counting gives $`e_j=\Theta_m(j^{1/m})`$ for large $`j`$. The exact optimal energy is finite precisely when

```math
\frac1{q_s}>1+\frac1m,
\qquad\text{equivalently}\qquad
q_s<\frac{m}{m+1}.
```

At equality, $`e_jr_j=\Theta(1/j)`$ and the series diverges logarithmically. Set $`q_*=m/(m+1)`$. Since the defining power sum is decreasing,

```math
q_s<q_*
\quad\Longleftrightarrow\quad
s<\left(\sum_i\lambda_i^{q_*}\right)^{-1/q_*}.
```

Using natural logarithms, $`H_q(\lambda)=\log(\sum_i\lambda_i^q)/(1-q)`$, this is the strict success boundary

```math
\boxed{s_c(\lambda,m)=e^{-H_{q_*}(\lambda)/m}.}
```

The mode count selects the Rényi order. Targets of equal Schmidt rank can therefore lie on opposite sides of a finite-energy borrowing threshold. [Interpretation](interpretation.md) gives an explicit two-qubit example; [mode threshold](mode_threshold.md) describes the integer-mode condition.

For $`\lambda_i=1/d`$, the equation for $`q_s`$ gives

```math
q_s=\frac{\log d}{\log(d/s)},
\qquad b_s=\frac{\log(1/s)}{\log d},
```

and $`s_c=d^{-1/m}`$. The tree reduces to the equal-weight logarithmic blocks in [the original construction](construction.md). In particular, the exact one-mode energy reduces to $`s(d-1)/(1-ds)`$ when $`s\lt1/d`$.

[Model](model.md) · [Sharp accuracy law](target_accuracy.md) · [Passive energy](spectral_energy.md) · [Related work](../references/related_work.md)
