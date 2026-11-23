# Verification

Run the deterministic checks from the repository root:

```bash
python3 verification/run_checks.py
```

Python 3.11 or later is sufficient; no third-party packages are required. The script uses exact rational probabilities and 100-digit decimal square roots and logarithms. Its reviewed numerical summaries are in [expected_results.json](expected_results.json).

## What the checks address

| Check | Scientific failure mode addressed |
| --- | --- |
| Full finite Schmidt vectors for dimensions two and three | An incorrect parent index, truncation normalization, or quotient/remainder target assignment |
| Explicit root filter and both instrument branches | A nonphysical filter, an incorrect success probability, or forgetting catalyst consumption on failure |
| Direct success-state overlap and stable infidelity | Confusing amplitude error with squared infidelity, or cancellation that reports zero error at high precision |
| Source photons and target passive-index identity | A missing factor of two between one party and the complete catalyst, or an incorrect energy offset |
| Conditional and unconditional output fidelities | Reporting a success-conditioned guarantee as an unconditional one |
| Selected tail inequalities, including a mixed retained output | Concrete checks of the Hellinger-tail step on physical finite examples |
| Large-cutoff block sums | Bounded subcritical energy, logarithmic critical growth, and the full supercritical energy/error exponent |
| Fock-state enumeration and exact binomial degeneracies | An incorrect density of states when the number of modes changes |
| Passive energy, a reversed basis, and an explicit local basis rotation | Selected checks of the passive assignment and its physical energy meaning |
| Fixed-mode construction growth and strict mode thresholds | Conflating critical with subcritical success, or leaving additional catalyst modes uncounted |
| Nonuniform root-pruned word spectra against exhaustive word enumeration | Incorrect word multiplicities, tie handling, or the target-dependent root coefficient |
| Arbitrary-target finite filters and complete tensor-sorted joint outputs | Losing exact success after truncation, omitting the factor `1-s` in the displaced target mass, or testing only one marginal |
| Independent tensor-sort fixed-point iterates and rational majorization examples | An incorrect fixed-point map, contraction estimate, or direction of the majorization ordering |
| Exhaustive top-k allocations versus directly sorted tensor tails | Incorrect transfer of the uniform-target tail dilation to unequal Schmidt coefficients |
| Nonuniform passive photon costs for one, two and three modes per party | Substituting Schmidt rank for ordered Fock-state energy, or misassigning tied energy levels |
| Uniform-spectrum recurrence and counting-root identities | Failure of the general target-spectrum account to recover the established maximally entangled case |
| A nonuniform critical point and finite tail/energy growth | Replacing the target-spectrum threshold by a rank-only threshold, or confusing critical and power-divergent regimes |

For small examples the filter, probabilities, photon means and Fock degeneracies are exact fractions or integers. Full vector overlap is calculated independently of the shell formula. For large cutoffs, the script evaluates exact geometric sums and exact cumulative Fock-energy sums without allocating an exponentially long vector. Infidelity is computed by rationalizing the small difference before taking square roots; it remains nonzero in examples far below ordinary floating-point unit roundoff.

The mixed-output example attaches a local environment whose root/rest states have overlap `99/100`, then discards it. Its retained output has lower fidelity while the complete branch keeps its Schmidt spectrum. The tested tail inequalities use the actual success-conditioned fidelity of this physical example.

The additional [target-spectrum checks](check_target_spectrum.py) use four exact rational target/success pairs, including repeated largest Schmidt coefficients and uniform targets. They test six cutoffs per pair, including cutoffs through tied blocks. A priority-queue word enumeration is compared with exhaustive finite words; an explicit bound on the largest omitted word ensures that the compared prefix is complete. The finite successful spectrum is compared with a directly sorted catalyst–target tensor product, and its squared joint fidelity is computed from the complete overlap. All squared filter factors, normalization constants, success probabilities and displaced target masses are exact fractions.

These checks also compare independent finite iterations of the tensor-sort map with the word-forest prefix, check rational T-transforms, and exhaustively allocate top-k terms among the target's Schmidt streams. These are finite tests of the fixed-point and tail mechanisms; no optimizer or numerical linear-programming dependency is used. For small supports, every distinct assignment of the listed Fock energies is compared with the passive assignment. Larger supports use independent Fock occupation enumeration and the weighted-tail energy identity.

For the nonuniform target with probabilities `(9/10, 1/10)`, the one-mode critical success is exactly `5/8`: its scaled weights have square roots `3/4` and `1/4`. Finite prefixes through 8192 coefficients corroborate the predicted tail power and the subcritical, logarithmic-critical and supercritical passive-energy behavior. The displayed slopes are finite-cutoff diagnostics with stated tolerances, not exact asymptotic constants or bounds uniform in the target.

## Scope

These checks verify the named constructions, identities and selected limiting estimates. They do not prove optimality over all catalyst spectra or all LOCC instruments, the infinite-dimensional extension, the stopped-tree counting theorem, the uniform square-root-tail comparison, or the compactness argument. Those are analytical claims in the scientific account. Successful checks do not establish novelty, efficient hardware realization, bounded control work, or robustness to implementation noise.

The large-cutoff checks keep target dimension, success probability and mode count fixed. They do not verify uniform bounds as those parameters vary jointly with the error. Target passive-index energy is a mathematical moment used in the converse; it must not be confused with a claim that the actual output target has that oscillator Hamiltonian.

After an intentional scientific change, inspect the affected derivation and numerical values before regenerating the reference summary:

```bash
python3 verification/run_checks.py --write-expected
python3 verification/run_checks.py
```

Updating the expected summary is not itself validation of a changed theorem.
