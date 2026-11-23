# Thirty milestones for heralded entanglement borrowing

This is a common understanding map for the project. Its single educational anchor is John Watrous, *The Theory of Quantum Information* (2018). The [Watrous bridge](WATROUS_BRIDGE.md) identifies the verified sections, translates notation and supplies the steps from the book's finite-dimensional framework to this oscillator problem.

The map has **12 background/preliminary milestones** and **18 narrative/innovation milestones**. The background builds from the physical carriers and individual quantum operations to the complete task and resource model. The narrative builds the optimal target-dependent spectrum and filter, develops the approximate converse from a branch to an arbitrary protocol, and combines both routes into the full spectrum-dependent energy law. The uniform maximally entangled target is retained as a checked special case. This allocation reflects the project's connection between stochastic entanglement conversion and oscillator density of states.

Watrous's fidelity function is the unsquared root fidelity. The project's $`F_{\rm joint}`$ is its square. Oscillator counting, infinite-dimensional extensions and the optimized success–energy law are supplied by the project and its research-level references; the textbook is not credited with those results.

## M01 — The shared oscillator reservoir

**Phase:** Background/preliminaries.

**Central question:** What physical systems supply the entanglement, and which initial inventory is charged?

**Understanding target:** Identify the known pure catalyst, its $`m`$ oscillator modes at each party, the common frequency and the total initial mean photon number $`E(C)`$. Distinguish a mode count from a photon count.

**Dependencies and story role:** None. This fixes the physical objects before introducing their mathematical description.

**Conceptual connection:** A bipartite quantum state becomes a physical resource once its carriers and energy convention are specified.

**Source pointers:** Watrous §1.1.3, “Operator decompositions and norms,” for the finite-dimensional spectral language; [model: states and inventory](../science/model.md#states-and-charged-inventory); [spectral energy: Fock counting](../science/spectral_energy.md#fock-counting).

## M02 — Schmidt probabilities describe shared pure entanglement

**Phase:** Background/preliminaries.

**Central question:** Which part of a pure bipartite state is unchanged by a local change of basis?

**Understanding target:** Read a Schmidt decomposition, distinguish amplitudes $`\sqrt{p_j}`$ from probabilities $`p_j`$, and recognize that the two reduced states have the same nonzero spectrum. Explain why sorting that spectrum does not specify the physical oscillator basis.

**Dependencies and story role:** M01. This introduces the spectrum that will connect entanglement conversion to energy.

**Conceptual connection:** Local basis choices change the energy assigned to a spectrum while preserving its pure-state entanglement data.

**Source pointers:** Watrous §1.1.3, Schmidt decompositions; [spectral energy: passive Schmidt assignment](../science/spectral_energy.md#passive-schmidt-assignment); [exact-success spectrum](../science/exact_success.md#1-exact-conversion-with-finite-mean-energy).

## M03 — A pure target and its full Schmidt spectrum

**Phase:** Background/preliminaries.

**Central question:** What specifies the additional shared state required on success?

**Understanding target:** Read a known target $`|T_\lambda\rangle=\sum_{i=1}^{d}\sqrt{\lambda_i}|i,i\rangle`$ with fixed decreasing positive probabilities and $`d\ge2`$. Explain the complete reference $`|C\rangle\otimes|T_\lambda\rangle`$, its product probabilities $`p_j\lambda_i`$ and its finite-rank multiplication by $`r`$. Recognize a uniform $`d`$-level target as a special case.

**Dependencies and story role:** M02. This specifies the output before comparing targets of the same rank.

**Conceptual connection:** Tensor products convert a physical joint-return promise into ordered probability data; target rank alone does not specify those data.

**Source pointers:** Watrous §1.1.3 and §6.2.1; [model](../science/model.md); [general target spectrum](../science/target_spectrum.md); [notation bridge](WATROUS_BRIDGE.md).

## M04 — A local filter has an outcome and a probability

**Phase:** Background/preliminaries.

**Central question:** How can a local quantum operation produce an announced success without being deterministic?

**Understanding target:** Interpret a contraction $`K`$, its complementary measurement outcome, the Born probability of success and normalization of the successful state. Distinguish the filter's action from conditioning on its outcome.

**Dependencies and story role:** M02. This supplies the operation used in the attaining protocol.

**Conceptual connection:** Kraus representations turn an algebraic rescaling of Schmidt amplitudes into a valid physical instrument.

**Source pointers:** Watrous §2.2.2, “Representations and characterizations of channels,” and §2.3.2, “Basic notions concerning measurements”; [construction: root-only filter](../science/construction.md#3-a-root-only-filter-with-exact-success-probability).

## M05 — LOCC and the supply of ancillary systems

**Phase:** Background/preliminaries.

**Central question:** Which coordinated operations are allowed without supplying new shared entanglement?

**Understanding target:** Describe local operations, classical announcements, product local ancillas and classical randomization. Explain why a global entangling operation, a fresh entangled input and a local work system have different roles in this task.

**Dependencies and story role:** M01, M04. This grows from one filter to the allowed protocol class.

**Conceptual connection:** The same state transformation has a different resource meaning when its permitted communication and auxiliary inputs change.

**Source pointers:** Watrous §6.1.2, “Separable maps and the LOCC paradigm”; [model: operations and heralding](../science/model.md#operations-heralding-and-return); [interpretation: failure](../science/interpretation.md#what-success-and-failure-mean).

## M06 — Conditional joint fidelity is the return criterion

**Phase:** Background/preliminaries.

**Central question:** What does the promised return accuracy say after the success flag has been observed?

**Understanding target:** Read $`p_{\rm suc}\ge s`$ and $`F_{\rm joint}\ge1-\varepsilon`$ as separate requirements. Explain why the fidelity compares the complete retained catalyst–target state with a pure product reference, and translate it to Watrous's root-fidelity convention.

**Dependencies and story role:** M03, M04, M05. This completes the output promise.

**Conceptual connection:** Conditional normalization and a joint reference keep success probability, return accuracy and decoupling distinct.

**Source pointers:** Watrous §3.2, “The fidelity function”; [model: operations, heralding and return](../science/model.md#operations-heralding-and-return); [Watrous notation bridge](WATROUS_BRIDGE.md).

## M07 — Fidelity, Schmidt affinity and small tails

**Phase:** Background/preliminaries.

**Central question:** How does closeness of pure states constrain their ordered Schmidt probabilities?

**Understanding target:** Connect a pure-state overlap to the affinity $`\sum_j\sqrt{p_jq_j}`$. Recognize that a squared-infidelity budget controls a distance between square-root probabilities, including after grouping indices into a tail.

**Dependencies and story role:** M02, M06. This prepares the quantitative error step in the converse.

**Conceptual connection:** Quantum fidelity produces a classical probability-distance statement without replacing the quantum protocol by a classical one.

**Source pointers:** Watrous §1.1.3 and §3.2; [converse: Schmidt affinity and environments](../science/converse.md#schmidt-affinity-and-discarded-environments).

## M08 — Majorization and average Schmidt-tail monotonicity

**Phase:** Background/preliminaries.

**Central question:** What prevents LOCC from increasing shared pure-state entanglement on average?

**Understanding target:** Interpret an ordered partial sum and its complementary tail $`P_k=\sum_{j>k}p_j`$. Distinguish an average monotonicity statement from a bound on each successful branch alone.

**Dependencies and story role:** M02, M05. This supplies the entanglement constraint that will charge a successful return.

**Conceptual connection:** Majorization organizes pure-state conversion, while Schmidt-tail monotones retain the probabilities of stochastic outcomes.

**Source pointers:** Watrous §4.3.1, “Majorization for real vectors,” and §6.2.1; [converse: average monotonicity](../science/converse.md#average-monotonicity-of-a-schmidt-tail); [research-level conversion references](../references/related_work.md).

## M09 — Discarded local environments still matter in a proof

**Phase:** Background/preliminaries.

**Central question:** How can a converse handle a mixed retained success state when the initial catalyst is pure?

**Understanding target:** Explain a local Stinespring dilation and the role of a purification of the retained output. Recognize that an environment in a complete successful branch may be entangled across the parties, even though ancillary inputs supplied no shared entanglement.

**Dependencies and story role:** M04, M05, M06, M07, M08. This joins the operation, distance and entanglement foundations.

**Conceptual connection:** Uhlmann's theorem compares purifications, while majorization controls the additional Schmidt spectrum carried by an environment.

**Source pointers:** Watrous §2.2.2, §3.2.2 and §4.3.1; [converse: environments](../science/converse.md#schmidt-affinity-and-discarded-environments); [model: pure initial catalyst](../science/model.md#scope-and-attribution).

## M10 — Fock counting turns a mode budget into a density of states

**Phase:** Background/preliminaries.

**Central question:** How many orthogonal $`m`$-mode oscillator states fit below a given total photon number?

**Understanding target:** Interpret the count $`A_m(h)=\binom{h+m}{m}`$ and its fixed-$`m`$ consequence $`e_j=\Theta_m(j^{1/m})`$ for ordered energy levels. Explain why low-energy degeneracy increases with the mode count.

**Dependencies and story role:** M01, M02. This supplies the physical rank-to-energy relation.

**Conceptual connection:** Counting Fock configurations gives physical meaning to a location in an ordered Schmidt spectrum.

**Source pointers:** Watrous §1.1.3 for ordered spectral notation; the oscillator counting derivation is local: [spectral energy: Fock counting](../science/spectral_energy.md#fock-counting); [mode threshold: counting states](../science/mode_threshold.md#1-physical-state-counting).

## M11 — Passive assignment and the tail-energy identity

**Phase:** Background/preliminaries.

**Central question:** What is the least initial photon inventory compatible with a given Schmidt spectrum?

**Understanding target:** Explain why larger probabilities occupy lower Fock energies in the minimum-energy assignment. Interpret the exact identity $`\sum_j e_jp_j=\sum_k(e_{k+1}-e_k)P_k`$, including energy degeneracies.

**Dependencies and story role:** M02, M08, M10. This joins the spectral entanglement description to the charged physical resource.

**Conceptual connection:** Rearrangement bounds the inventory in arbitrary Schmidt bases; summation by parts expresses that inventory using the same tails that LOCC constrains.

**Source pointers:** Watrous §1.1.3 and §4.3.1 for the finite spectral foundations; [passive Schmidt assignment](../science/spectral_energy.md#passive-schmidt-assignment); [tail energy identity](../science/spectral_energy.md#tail-energy-identity).

## M12 — The complete optimization and its limits

**Phase:** Background/preliminaries.

**Central question:** Which physical task is optimized, and which parameters remain fixed?

**Understanding target:** Assemble a known pure catalyst, fixed mode count $`m`$, complete entangled target spectrum $`\lambda`$ and $`0\lt s\lt 1`$, success-conditioned joint squared fidelity, unrestricted failure and initial total photons. Explain the limit $`\varepsilon\downarrow0`$ with those parameters fixed, and distinguish finite mean energy from finite support.

**Dependencies and story role:** M01–M11. This integrates the background into the precise research question.

**Conceptual connection:** State conversion, oscillator density of states and conditional error become one optimization with explicit quantifiers and a full target specification.

**Source pointers:** Watrous §2.3.2, §3.2 and §6.1.2; [model and scope](../science/model.md); [general accuracy law](../science/target_accuracy.md).

## M13 — Sorted product streams contain the target information

**Phase:** Narrative/innovation.

**Central question:** How does adding an unequal target change the source spectrum?

**Understanding target:** Construct $`q(p)=\mathrm{sort}(p\otimes\lambda)`$ by merging the $`d`$ weighted source streams. Explain why products from different source indices interleave, and recover $`q_j=p_{\lceil j/d\rceil}/d`$ and $`Q_{dk}=P_k`$ for a uniform target.

**Dependencies and story role:** M03, M08, M12. This identifies the spectral operation used by both the optimizer and the approximate converse.

**Conceptual connection:** The complete target spectrum enters through sorted products, while uniform targets admit a simpler dilation in the rank index.

**Source pointers:** Watrous §1.1.3 and §4.3.1; [target spectrum](../science/target_spectrum.md); [target-tail allocation](../science/target_accuracy.md).

## M14 — The most concentrated feasible spectrum is a fixed point

**Phase:** Narrative/innovation.

**Central question:** Why does a particular successful catalyst minimize energy over all allowed pure catalysts?

**Understanding target:** Use exact tails $`P_k\ge sQ_k`$ to read $`p\prec\mathcal F_s(p)`$, where $`\mathcal F_s(p)=(1-s)\delta_1+s q(p)`$. Explain majorization preservation, the $`s`$-contraction in $`\ell^1`$, and iteration to the unique fixed point $`r`$. Conclude that $`r`$ majorizes every feasible spectrum and minimizes increasing passive energy.

**Dependencies and story role:** M08, M11, M13. This turns feasibility into a global optimization rather than one successful example.

**Conceptual connection:** An order-preserving contraction connects stochastic entanglement conversion with universal spectral-energy optimality.

**Source pointers:** Watrous §4.3.1 and §6.2.1 for the finite-dimensional foundations; [fixed-point optimization](../science/target_spectrum.md).

## M15 — A word forest gives the optimal spectrum explicitly

**Phase:** Narrative/innovation.

**Central question:** Which coefficients realize the fixed point for an arbitrary target?

**Understanding target:** Explain the root $`A=(1-s)/(1-s\lambda_1)`$ and the coefficients $`A s^k\lambda_{i_1}\cdots\lambda_{i_k}`$ for words whose first letter is not 1. Account for normalization and why pruning the first branch avoids duplicate counting. Distinguish normalization from finite photon energy.

**Dependencies and story role:** M02, M13, M14. This constructs the exact optimizer from the target probabilities.

**Conceptual connection:** Self-reproduction after target multiplication becomes an explicit weighted tree of Schmidt coefficients.

**Source pointers:** Watrous §1.1.3 for Schmidt notation; [root and word spectrum](../science/target_spectrum.md); [unequal worked example](WORKED_EXAMPLE.md).

## M16 — One filter and sorted local labels complete the protocol

**Phase:** Narrative/innovation.

**Central question:** How is the spectral fixed point realized by LOCC with an actual success flag?

**Understanding target:** Follow the root-only amplitude attenuation $`\sqrt{s\lambda_1}`$, success probability exactly $`s`$, product-vacuum failure and local reindexing into catalyst and target labels. Explain why unequal targets use known sorted product labels and why the countable-support operation needs an admitted local dilation.

**Dependencies and story role:** M04, M05, M13, M15. This converts the optimal spectrum into an operational exact protocol.

**Conceptual connection:** The identity $`r=(1-s)\delta_1+s q(r)`$ balances both outcomes of a local instrument without making the initial state mixed.

**Source pointers:** Watrous §2.2.2, §2.3.2 and §6.1.2; [exact filter and local isometries](../science/target_spectrum.md); [worked examples](WORKED_EXAMPLE.md).

## M17 — Weighted counting determines the long tail

**Phase:** Narrative/innovation.

**Central question:** How many coefficients of the optimal spectrum exceed a small weight?

**Understanding target:** Define $`\beta_i=s\lambda_i`$ and the unique $`q_s`$ in $`(0,1)`$ satisfying $`\sum_i\beta_i^{q_s}=1`$. Explain conserved powered mass at a tree split, stopping leaves near a weight threshold, and the resulting $`p_j^\star=\Theta(j^{-1/q_s})`$ and $`R_k=\Theta(k^{-b_s})`$, $`b_s=1/q_s-1`$.

**Dependencies and story role:** M10, M15. This extracts the quantitative large-index behavior needed to test physical energy.

**Conceptual connection:** A weighted branching identity converts a target-dependent coefficient construction into a polynomial counting law.

**Source pointers:** Watrous §1.1.3 for spectral ordering; the tree argument is supplied locally in [target counting](../science/target_spectrum.md).

## M18 — The Rényi threshold prices the complete target

**Phase:** Narrative/innovation.

**Central question:** When does the optimal exact spectrum have finite photon inventory?

**Understanding target:** Combine the fixed-point tail with $`m`$-mode ordered energies. Define $`q_*=m/(m+1)`$ and $`H_q(\lambda)=\log(\sum_i\lambda_i^q)/(1-q)`$, then explain $`s_c=\exp[-H_{q_*}(\lambda)/m]`$. Establish the strict condition $`s\lt s_c`$, including logarithmic divergence at equality and the different rank-two thresholds $`1/2`$ and $`5/8`$ for Bell and $`(0.9,0.1)`$ targets.

**Dependencies and story role:** M10, M11, M14, M17. This combines the exact optimization and oscillator density of states into a physical feasibility boundary.

**Conceptual connection:** The full target probability spectrum, through a mode-dependent Rényi entropy, determines the cost of its required tail.

**Source pointers:** Watrous §4.3.1 and §6.2.1 for the ordering framework; [threshold](../science/target_spectrum.md); [mode interpretation](../science/mode_threshold.md); [worked comparison](WORKED_EXAMPLE.md).

## M19 — A successful branch retains its required Schmidt tail

**Phase:** Narrative/innovation.

**Central question:** How does closeness to a pure joint reference constrain the complete successful state?

**Understanding target:** Combine Schmidt affinity, tail coarse graining and purification of discarded local systems. Explain why an entangled environment cannot lower the required tail below the desired retained spectrum, including for an unequal target.

**Dependencies and story role:** M07, M08, M09, M13. This develops the geometric step behind the approximate converse.

**Conceptual connection:** Fidelity of a retained output constrains a complete branch without assuming the retained state is pure.

**Source pointers:** Watrous §3.2.2 and §4.3.1; [affinity and environments](../science/converse.md#schmidt-affinity-and-discarded-environments); [general target application](../science/target_accuracy.md).

## M20 — Averaging yields the arbitrary-LOCC fidelity bound

**Phase:** Narrative/innovation.

**Central question:** How do branch constraints survive adaptivity, multiple successful outcomes and conditioning?

**Understanding target:** Obtain $`P_k\ge s(\sqrt{Q_k}-\sqrt{2\varepsilon})_+^2`$ from average tail monotonicity and the joint fidelity budget. Explain the role of every outcome, mixed retained successes and the stated trace-norm closure.

**Dependencies and story role:** M05, M06, M08, M09, M19. This extends a branch calculation to the whole allowed protocol class.

**Conceptual connection:** Success probability pays for the entanglement in accepted branches; conditioning does not remove that payment.

**Source pointers:** Watrous §6.1.2 and §6.2.1; [tail inequality and closure](../science/converse.md); [unequal-target use](../science/target_accuracy.md).

## M21 — Allocating product entries gives an exact tail operator

**Phase:** Narrative/innovation.

**Central question:** What replaces the uniform relation $`Q_{dk}=P_k`$ for unequal target probabilities?

**Understanding target:** Explain $`Q_k=\min_{k_1+\cdots+k_d=k}\sum_i\lambda_iP_{k_i}`$, with $`P_0=1`$ and nonnegative integer allocations. Construct the square-root operator with its zero coordinate fixed, and distinguish an exact top-k identity from a bound choosing one convenient allocation.

**Dependencies and story role:** M13, M20. This gives the nonlinear operator that carries all target information into the converse.

**Conceptual connection:** Merging weighted streams is equivalent to optimizing how many entries are removed from each stream.

**Source pointers:** Watrous §1.1.3 and §4.3.1 for ordered spectra; [tail allocation and operator](../science/target_accuracy.md).

## M22 — Contraction stability compares every approximate source with the optimum

**Phase:** Narrative/innovation.

**Central question:** Why must an accurate source retain the optimal exact tail to controlled precision?

**Understanding target:** Explain monotonicity and the one-sided $`\sqrt s`$ Lipschitz bound from the weighted Euclidean norm. Compare $`\sqrt P`$ with the exact fixed tail $`\sqrt R`$ to obtain $`P_k\ge(\sqrt{R_k}-\sqrt{2s\varepsilon}/(1-\sqrt s))_+^2`$.

**Dependencies and story role:** M14, M17, M20, M21. This is the load-bearing unequal-target approximate converse.

**Conceptual connection:** A uniform stability estimate replaces a rank-only geometric recurrence and preserves the full target-spectrum dependence.

**Source pointers:** Watrous §3.2 for fidelity conventions; [stability proof](../science/target_accuracy.md).

## M23 — The accuracy cutoff determines the divergent lower costs

**Phase:** Narrative/innovation.

**Central question:** Over how many ordered coefficients does fidelity force a significant tail?

**Understanding target:** Use $`R_k=\Theta(k^{-b_s})`$ and the stability estimate to locate $`k=\Theta(\varepsilon^{-1/b_s})`$. Sum the forced tails against passive energy increments to derive a logarithm at $`b_s=1/m`$ and the power $`\varepsilon^{-(1/(mb_s)-1)}`$ when $`b_s\lt 1/m`$. Retain degeneracies and fixed-parameter constants.

**Dependencies and story role:** M10, M11, M17, M22. This turns the general converse into quantitative initial-photon lower bounds.

**Conceptual connection:** The error budget sets a rank cutoff, while the oscillator density of states prices the probability that must persist below it.

**Source pointers:** Watrous §1.1.3 and §3.2 for spectral and distance foundations; [energy lower bounds](../science/target_accuracy.md); [spectral energy](../science/spectral_energy.md).

## M24 — Finite cutoffs attain accuracy without lowering success

**Phase:** Narrative/innovation.

**Central question:** How can an infinite-spectrum optimizer give a finite protocol at every positive error?

**Understanding target:** Keep the $`D`$ largest fixed-point coefficients, normalize by $`1-t`$ with $`t=R_D`$, and adjust only the root filter to retain probability exactly $`s`$. Explain the sorted product identity on entries $`2`$ through $`D`$, the omitted product mass $`b=(1-s)t/[s(1-t)]`$, and the exact-overlap bound $`1-F_{\rm joint}\le2b`$.

**Dependencies and story role:** M06, M13, M15, M16, M17. This constructs the finite upper bound under the same operational promises.

**Conceptual connection:** Truncation must preserve success and the complete joint reference, not only approximate the original source spectrum.

**Source pointers:** Watrous §2.3.2 and §3.2; [finite truncation and fidelity](../science/target_accuracy.md); [worked examples](WORKED_EXAMPLE.md).

## M25 — The complete target-dependent success-energy law

**Phase:** Narrative/innovation.

**Central question:** How do the arbitrary-protocol converse and finite construction match?

**Understanding target:** State convergence to the finite exact optimum below $`s_c`$, logarithmic growth at $`s_c`$, and the matched power with exponent $`a=1/(mb_s)-1`$ above $`s_c`$. Explain what is optimized over all allowed pure catalysts and LOCC and distinguish a matching order from an exact coefficient.

**Dependencies and story role:** M12, M18, M20, M22, M23, M24. This integrates both directions into the main approximation theorem.

**Conceptual connection:** The same optimal tail controls exact feasibility and the divergence class of accurate finite borrowing.

**Source pointers:** Watrous §6.2.1 for conversion foundations; [model and main results](../science/model.md); [full accuracy law](../science/target_accuracy.md).

## M26 — Uniform targets recover the original sharp statements

**Phase:** Narrative/innovation.

**Central question:** How can the general theorem be checked against the maximally entangled case?

**Understanding target:** Substitute $`\lambda_i=1/d`$ into the exponent equation to obtain $`b_s=\log(1/s)/\log d`$, $`s_c=d^{-1/m}`$ and $`a=\log(sd^{1/m})/\log(1/s)`$. Explain reduction of the word forest to geometric blocks and the one-mode exact formula $`E=s(d-1)/(1-ds)`$, including its restricted domain $`s\lt 1/d`$.

**Dependencies and story role:** M13, M15, M17, M18, M25. This verifies that the extension contains the established result without replacing it.

**Conceptual connection:** An exactly solvable specialization checks notation, limiting orders, physical normalization and proof compatibility.

**Source pointers:** Watrous §1.1.3 and §6.2.1; [uniform construction](../science/construction.md); [one-mode exact optimum](../science/exact_success.md); [Bell example](WORKED_EXAMPLE.md).

## M27 — Compactness identifies the optimal small-error limit

**Phase:** Narrative/innovation.

**Central question:** Why can catalysts chosen separately at each accuracy not beat the finite exact optimum in the limit?

**Understanding target:** Explain energy tightness of sorted spectra, preservation of normalized mass and passing fixed-index inequalities to a limit before nonnegative energy summation. Combine limiting exact feasibility with fixed-point majorization and lower semicontinuity to identify $`E_m(\varepsilon;s,\lambda)\to E_{\rm exact}`$ below threshold.

**Dependencies and story role:** M11, M14, M18, M20, M25. This completes subcritical optimization for accuracy-dependent catalysts.

**Conceptual connection:** Initial energy control prevents mass from escaping to arbitrarily high Fock levels during the limiting argument.

**Source pointers:** Watrous §1.1.3 and §3.2 for spectral and continuity foundations; [subcritical limit](../science/target_accuracy.md); [uniform limit](../science/exact_success.md).

## M28 — A complete physical account includes failure and implementation resources

**Phase:** Narrative/innovation.

**Central question:** What capability remains when all branches and charged resources are stated?

**Understanding target:** Follow both worked filters, their conditional fidelities, input inventories and local reindexing. Explain probability $`s^k`$ for $`k`$ exact successes, destructive failure, and increasing cutoff. Distinguish initial photons, modes, maximum occupied level, preparation complexity and local work.

**Dependencies and story role:** M01, M05, M12, M16, M24, M25, M26. This integrates the theorem into its operational meaning.

**Conceptual connection:** Accurate conditional return and bounded mean inventory coexist with eventual resource consumption and demanding local controls.

**Source pointers:** Watrous §2.3.2 and §6.1.2; [worked examples](WORKED_EXAMPLE.md); [interpretation](../science/interpretation.md); [model resource convention](../science/model.md).

## M29 — Attribution and scope locate the added scientific result

**Phase:** Narrative/innovation.

**Central question:** What changes after established conversion and oscillator tools are credited?

**Understanding target:** Separate inherited Schmidt-tail monotones, majorization-based stochastic conversion, root filters and infinite-dimensional phenomena from the optimal fixed spectrum, weighted counting, Rényi boundary and sharp accuracy law. Compare assumptions before transferring claims from thermal catalysis or distillation with fresh entangled resources.

**Dependencies and story role:** M08, M12, M14, M18, M20, M25, M27, M28. This places the completed account in its actual scientific context.

**Conceptual connection:** Shared mathematical ingredients do not make two operational tasks, charged resources or guarantees identical.

**Source pointers:** Watrous §6.1.2 and §6.2.1 for the common framework; [related work](../references/related_work.md); [interpretation](../science/interpretation.md); [exact spectrum proof](../science/target_spectrum.md) and [accuracy proof](../science/target_accuracy.md).

## M30 — Explain the full spectrum-dependent borrowing result

**Phase:** Narrative/innovation.

**Central question:** How do the task, optimizer, construction, converse and boundaries form one account?

**Understanding target:** State the pure-catalyst task at fixed $`m`$, $`\lambda`$ and $`s\lt 1`$ with conditional joint squared fidelity and destructive failure allowed. Connect the optimal fixed point, its explicit filter, weighted tail, Rényi threshold and matched approximation law to oscillator counting. Recover the uniform special case and retain limits on mixed inputs, deterministic success, changing parameters and implementation costs.

**Dependencies and story role:** M12–M29. This is the global synthesis of the project.

**Conceptual connection:** The complete target spectrum and physical mode density jointly determine when successful return costs finite, logarithmic or power-growing initial photons.

**Source pointers:** Watrous §3.2, §6.1.2 and §6.2.1; [model](../science/model.md); [scientific route](../science/README.md); [target spectra](../science/target_spectrum.md); [target accuracy](../science/target_accuracy.md); [verification boundaries](../verification/README.md).

