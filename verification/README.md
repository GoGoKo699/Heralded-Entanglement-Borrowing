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

For small examples the filter, probabilities, photon means and Fock degeneracies are exact fractions or integers. Full vector overlap is calculated independently of the shell formula. For large cutoffs, the script evaluates exact geometric sums and exact cumulative Fock-energy sums without allocating an exponentially long vector. Infidelity is computed by rationalizing the small difference before taking square roots; it remains nonzero in examples far below ordinary floating-point unit roundoff.

The mixed-output example attaches a local environment whose root/rest states have overlap `99/100`, then discards it. Its retained output has lower fidelity while the complete branch keeps its Schmidt spectrum. The tested tail inequalities use the actual success-conditioned fidelity of this physical example.

## Scope

These checks verify the named constructions, identities and selected limiting estimates. They do not prove optimality over all catalyst spectra or all LOCC instruments, the infinite-dimensional extension, or the compactness argument. Those are analytical claims in the scientific account. Successful checks do not establish novelty, efficient hardware realization, bounded control work, or robustness to implementation noise.

The large-cutoff checks keep target dimension, success probability and mode count fixed. They do not verify uniform bounds as those parameters vary jointly with the error. Target passive-index energy is a mathematical moment used in the converse; it must not be confused with a claim that the actual output target has that oscillator Hamiltonian.

After an intentional scientific change, inspect the affected derivation and numerical values before regenerating the reference summary:

```bash
python3 verification/run_checks.py --write-expected
python3 verification/run_checks.py
```

Updating the expected summary is not itself validation of a changed theorem.
