# Thirty milestones for heralded entanglement borrowing

This is a common understanding map for the project. Its single educational anchor is John Watrous, *The Theory of Quantum Information* (2018). The [Watrous bridge](WATROUS_BRIDGE.md) identifies the verified sections, translates notation and supplies the steps from the book's finite-dimensional framework to this oscillator problem.

The map has **12 background/preliminary milestones** and **18 narrative/innovation milestones**. The background builds from the physical carriers and individual quantum operations to the complete task and resource model. The narrative builds explicit state and filter components, develops the converse from a branch to an arbitrary protocol, and combines both routes into the energy and mode laws. This allocation reflects the project's connection between stochastic entanglement conversion and oscillator density of states.

Watrous's fidelity function is the unsquared root fidelity. The project's $`F_{\rm joint}`$ is its square. Oscillator counting, infinite-dimensional extensions and the optimized success–energy law are supplied by the project and its research-level references; the textbook is not credited with those results.

## M01 — The shared oscillator reservoir

**Phase:** Background/preliminaries.

**Central question:** What physical systems supply the entanglement, and which initial inventory is charged?

**Understanding target:** Identify the known pure catalyst, its $`m`$ oscillator modes at each party, the common frequency and the total initial mean photon number $`E(C)`$. Distinguish a mode count from a photon count.

**Dependencies and story role:** None. This fixes the physical objects before introducing their mathematical description.

**Conceptual connection:** A bipartite quantum state becomes a physical resource once its carriers and energy convention are specified.

**Source pointers:** Watrous §1.1.3, “Operator decompositions and norms,” for the finite-dimensional spectral language; [model: states and inventory](../science/model.md#states-and-physical-inventory); [spectral energy: Fock counting](../science/spectral_energy.md#fock-counting).

## M02 — Schmidt probabilities describe shared pure entanglement

**Phase:** Background/preliminaries.

**Central question:** Which part of a pure bipartite state is unchanged by a local change of basis?

**Understanding target:** Read a Schmidt decomposition, distinguish amplitudes $`\sqrt{p_j}`$ from probabilities $`p_j`$, and recognize that the two reduced states have the same nonzero spectrum. Explain why sorting that spectrum does not specify the physical oscillator basis.

**Dependencies and story role:** M01. This introduces the spectrum that will connect entanglement conversion to energy.

**Conceptual connection:** Local basis choices change the energy assigned to a spectrum while preserving its pure-state entanglement data.

**Source pointers:** Watrous §1.1.3, Schmidt decompositions; [spectral energy: passive Schmidt assignment](../science/spectral_energy.md#passive-schmidt-assignment); [exact-success spectrum](../science/exact_success.md#1-exact-conversion-with-finite-mean-energy).

## M03 — A maximally entangled target and a product reference

**Phase:** Background/preliminaries.

**Central question:** How is adding a $`d`$-level maximally entangled target represented in a Schmidt spectrum?

**Understanding target:** Explain the uniform target probabilities $`1/d`$, the tensor-product reference $`|C\rangle\otimes|\Phi_d\rangle`$, and the multiplication of finite Schmidt rank by $`d`$. Keep target preparation and catalyst return in the same reference state.

**Dependencies and story role:** M02. This specifies the entanglement that must appear on success.

**Conceptual connection:** Tensor products translate a physical output promise into a change of ordered probability data.

**Source pointers:** Watrous §1.1.3 and §6.2.1, “Entanglement transformation”; [model: target state](../science/model.md#states-and-physical-inventory); [spectral energy: product identity](../science/spectral_energy.md#one-mode-product-identity).

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

**Source pointers:** Watrous §6.1.2, “Separable maps and the LOCC paradigm”; [model: operations and heralding](../science/model.md#operations-heralding-and-return); [interpretation: failure](../science/interpretation.md#what-happens-on-failure).

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

**Source pointers:** Watrous §1.1.3 for ordered spectral notation; the oscillator counting derivation is local: [spectral energy: Fock counting](../science/spectral_energy.md#fock-counting); [mode threshold: counting states](../science/mode_threshold.md#1-counting-low-energy-oscillator-states).

## M11 — Passive assignment and the tail-energy identity

**Phase:** Background/preliminaries.

**Central question:** What is the least initial photon inventory compatible with a given Schmidt spectrum?

**Understanding target:** Explain why larger probabilities occupy lower Fock energies in the minimum-energy assignment. Interpret the exact identity $`\sum_j e_jp_j=\sum_k(e_{k+1}-e_k)P_k`$, including energy degeneracies.

**Dependencies and story role:** M02, M08, M10. This joins the spectral entanglement description to the charged physical resource.

**Conceptual connection:** Rearrangement bounds the inventory in arbitrary Schmidt bases; summation by parts expresses that inventory using the same tails that LOCC constrains.

**Source pointers:** Watrous §1.1.3 and §4.3.1 for the finite spectral foundations; [passive Schmidt assignment](../science/spectral_energy.md#passive-schmidt-assignment); [tail energy identity](../science/spectral_energy.md#tail-energy-identity).

## M12 — The complete optimization and its limits

**Phase:** Background/preliminaries.

**Central question:** Which task does $`E_m(\varepsilon;s,d)`$ optimize?

**Understanding target:** Assemble a known pure catalyst, fixed $`m,d,0\lt s\lt 1`$, a success-conditioned joint fidelity promise, unrestricted failure and the initial photon objective. Explain the order “fix the parameters, then send $`\varepsilon`$ to zero,” and separate finite mean energy from finite support.

**Dependencies and story role:** M01–M11. This integrates the background into the precise research question.

**Conceptual connection:** State conversion, physical density of states and conditional error become one resource optimization with explicit quantifiers.

**Source pointers:** Watrous §2.3.2, §3.2 and §6.1.2 for the underlying language; [model: optimization](../science/model.md#optimization-and-limiting-convention); [model: scope](../science/model.md#scope-and-attribution).

## M13 — Adding the target replicates every Schmidt probability

**Phase:** Narrative/innovation.

**Central question:** Why does a maximally entangled target relate tails at indices $`k`$ and $`dk`$?

**Understanding target:** Derive $`q_j=p_{\lceil j/d\rceil}/d`$ and $`Q_{dk}=P_k`$. Explain the factor $`d`$ as the target's uniform Schmidt multiplicity.

**Dependencies and story role:** M03, M08, M12. This identifies the local spectral mechanism used by both proof routes.

**Conceptual connection:** The tensor-product output promise becomes an exact relation across rank scales.

**Source pointers:** Watrous §1.1.3 and §6.2.1; [converse: target spectrum](../science/converse.md); [spectral energy: product identity](../science/spectral_energy.md#one-mode-product-identity).

## M14 — A self-similar spectrum balances the replicated target

**Phase:** Narrative/innovation.

**Central question:** Which source probabilities can reproduce themselves after target replication and a successful filter?

**Understanding target:** Explain the decreasing block spectrum $`p_j=A(s/d)^{\lceil\log_d j\rceil}`$, its block multiplicities and its normalization for every $`s\lt 1`$. Distinguish normalization from finite mean energy.

**Dependencies and story role:** M02, M10, M13. This constructs the first attaining object.

**Conceptual connection:** The probability reduction $`s`$ compensates the target's multiplicity $`d`$ through a geometric distribution over rank scales.

**Source pointers:** Watrous §1.1.3 for Schmidt notation; [construction: normalized spectrum](../science/construction.md#1-a-normalized-self-similar-spectrum); [exact-success source](../science/exact_success.md#1-exact-conversion-with-finite-mean-energy).

## M15 — One root filter announces exact success probability

**Phase:** Narrative/innovation.

**Central question:** How does the self-similar spectrum turn a local filter into the required stochastic transformation?

**Understanding target:** Explain why attenuating only the vacuum/root amplitude produces the replicated spectrum with probability exactly $`s`$. Account for the complementary branch, which leaves a separable vacuum.

**Dependencies and story role:** M04, M05, M14. This turns the spectral design into an allowed local instrument.

**Conceptual connection:** The spectrum identity $`p=(1-s)\delta_1+s q`$ encodes the complete success-and-failure balance without making the initial catalyst mixed.

**Source pointers:** Watrous §2.2.2 and §2.3.2; [exact filter and outcomes](../science/exact_success.md#1-exact-conversion-with-finite-mean-energy); [construction: filter](../science/construction.md#3-a-root-only-filter-with-exact-success-probability).

## M16 — Local reindexing produces a returned catalyst and target

**Phase:** Narrative/innovation.

**Central question:** How does a replicated Schmidt spectrum become the desired physical product state?

**Understanding target:** Follow the quotient-and-remainder map from one Fock index to a catalyst index and target label. Explain joint decoupling and why the exact infinite-dimensional isometry needs a legitimate local dilation.

**Dependencies and story role:** M03, M05, M13, M15. This completes the exact successful transformation.

**Conceptual connection:** A sorted-spectrum construction acquires a concrete output register structure through local isometries.

**Source pointers:** Watrous §2.2.2 for isometric dilations; [exact conversion and local dilation](../science/exact_success.md#local-dilation); [finite reindexing](../science/construction.md#4-local-reindexing-and-exact-fidelity).

## M17 — Finite truncation preserves the success promise

**Phase:** Narrative/innovation.

**Central question:** How can the construction use finite Fock support without silently changing its promised success probability?

**Understanding target:** Explain the cutoff $`D=d^L`$, the omitted source mass $`t_L`$ and renormalization. Identify why the root filter is adjusted so that success remains exactly $`s`$ after truncation.

**Dependencies and story role:** M06, M14, M15, M16. This makes every positive-error upper bound finite.

**Conceptual connection:** Finite approximation must preserve the operational success requirement as well as approximate the desired state.

**Source pointers:** Watrous §2.3.2 and §3.2; [construction: finite cutoff](../science/construction.md#2-a-finite-cutoff-and-a-physical-catalyst); [adjusted root filter](../science/construction.md#3-a-root-only-filter-with-exact-success-probability); [worked example](WORKED_EXAMPLE.md).

## M18 — The omitted target tail determines the joint fidelity

**Phase:** Narrative/innovation.

**Central question:** Where does the finite construction's return error reside?

**Understanding target:** Explain that the successful spectrum agrees with the desired spectrum at indices $`2,\ldots,D`$, while omitted target mass $`b_L`$ moves to the root. Relate the resulting exact overlap to $`1-F_L=O_{s,d}(s^L)`$.

**Dependencies and story role:** M06, M07, M13, M17. This supplies the accuracy estimate for the upper bound.

**Conceptual connection:** A controlled spectral discrepancy gives an explicit joint return guarantee for the entire retained output.

**Source pointers:** Watrous §3.2; [construction: exact fidelity](../science/construction.md#4-local-reindexing-and-exact-fidelity); [worked example](WORKED_EXAMPLE.md).

## M19 — A successful branch cannot hide its required Schmidt tail

**Phase:** Narrative/innovation.

**Central question:** How does an accurate successful branch force a minimum amount of entanglement in its complete state?

**Understanding target:** Combine Schmidt affinity, tail coarse graining and a purification of discarded environments. Explain why a potentially entangled environment cannot reduce the required tail below that of the desired retained target.

**Dependencies and story role:** M07, M08, M09, M13. This develops the local geometric step of the converse.

**Conceptual connection:** Fidelity to the retained pure reference constrains the entanglement spectrum even when the retained success state is mixed.

**Source pointers:** Watrous §3.2.2 and §4.3.1; [converse: affinity and environments](../science/converse.md#schmidt-affinity-and-discarded-environments).

## M20 — Averaging gives a bound for every allowed protocol

**Phase:** Narrative/innovation.

**Central question:** How do branch constraints survive adaptive LOCC and conditioning on success?

**Understanding target:** Combine average Schmidt-tail monotonicity with the average fidelity budget to obtain $`P_k\ge s(\sqrt{Q_k}-\sqrt{2\varepsilon})_+^2`$. Explain why this covers several successful outcomes, mixed retained states and the specified closure of LOCC.

**Dependencies and story role:** M05, M06, M08, M09, M19. This lifts a branch argument to the complete protocol class.

**Conceptual connection:** The success probability pays for the entanglement carried by accepted branches; conditioning does not remove that cost.

**Source pointers:** Watrous §6.1.2 and §6.2.1 for finite-dimensional LOCC foundations; [converse: averaging](../science/converse.md#averaging-the-successful-branches); [infinite outcomes and closure](../science/converse.md#infinite-outcomes-and-closure); [inherited infinite-dimensional conversion results](../references/related_work.md).

## M21 — The target creates a seeded geometric tail recurrence

**Phase:** Narrative/innovation.

**Central question:** Why must a source spectrum carry weight at successively larger rank scales?

**Understanding target:** Use $`Q_{dk}=P_k`$ in the universal inequality and identify a nonzero seed from $`q_1\le1/d`$. Explain the recurrence for $`\sqrt{P_{d^\ell}}`$ and the meaning of its additive error term.

**Dependencies and story role:** M13, M20. This converts the general converse into a scale-by-scale constraint.

**Conceptual connection:** Reproducing the catalyst while adding a target links one rank scale to the next, with success probability setting the retained fraction.

**Source pointers:** Watrous §3.2 and §6.2.1 for the ingredients; [converse: geometric recurrence](../science/converse.md#a-geometric-tail-recurrence).

## M22 — Fixed accuracy determines how many scales are forced

**Phase:** Narrative/innovation.

**Central question:** How far can the converse recurrence be iterated before the allowed error dominates?

**Understanding target:** Explain why the accumulated square-root error permits tails of order $`s^\ell`$ through $`L_\varepsilon=\log(1/\varepsilon)/\log(1/s)+O_{s,d}(1)`$. Keep the squared-infidelity convention and fixed-$`s`$ limiting order intact.

**Dependencies and story role:** M06, M07, M12, M21. This identifies the effective range needed for the asymptotic lower bound.

**Conceptual connection:** A local fidelity budget becomes a global number of unavoidable rank scales; replacing the convention by a different error parameter changes the comparison.

**Source pointers:** Watrous §3.2 for fidelity conventions; [converse: recurrence cutoff](../science/converse.md#a-geometric-tail-recurrence); [model: limiting convention](../science/model.md#optimization-and-limiting-convention).

## M23 — Rank scales become a geometric photon sum

**Phase:** Narrative/innovation.

**Central question:** How do the forced tails and the attaining spectrum translate into the same physical inventory?

**Understanding target:** Combine $`e_j=\Theta_m(j^{1/m})`$ with block mass of order $`s^\ell`$. Explain the shared sum $`\sum_{\ell\le L}(sd^{1/m})^\ell`$ in the lower and upper bounds, including why energy degeneracies do not invalidate the lower bound.

**Dependencies and story role:** M10, M11, M14, M18, M22. This joins the construction and converse through the physical density of states.

**Conceptual connection:** Entanglement conversion controls tail weight; oscillator counting determines the energy paid for that weight.

**Source pointers:** Watrous §1.1.3 and §4.3.1 for spectral foundations; [spectral energy: geometric blocks](../science/spectral_energy.md#geometric-index-blocks); [construction: photon inventory](../science/construction.md#5-photon-inventory-and-the-three-regimes); [converse: energy lower bounds](../science/converse.md#energy-lower-bounds-for-a-fixed-number-of-modes).

## M24 — The matched success–energy phase law

**Phase:** Narrative/innovation.

**Central question:** Why do bounded, logarithmic and power-law photon costs occur at different fixed success probabilities?

**Understanding target:** Interpret $`g=sd^{1/m}`$, the critical value $`s_c=d^{-1/m}`$ and the exponent $`a_m=\log(g)/\log(1/s)`$. Explain what is matched over all allowed protocols and distinguish an asymptotic order from an exact coefficient.

**Dependencies and story role:** M12, M18, M20, M22, M23. This assembles the main approximation theorem.

**Conceptual connection:** Convergence or divergence of one geometric resource sum changes the energy cost's divergence class.

**Source pointers:** Watrous §6.2.1 as conversion background; [model: success–energy law](../science/model.md#the-successenergy-law); [mode threshold: approximate costs](../science/mode_threshold.md#3-the-same-counting-law-determines-approximate-costs).

## M25 — Exact finite-energy return has a strict mode threshold

**Phase:** Narrative/innovation.

**Central question:** When does finite mean energy permit exact joint return, and how many modes are needed?

**Understanding target:** Combine the infinite-support construction with the zero-error converse to establish $`s\lt d^{-1/m}`$. Explain the strict integer condition $`m>\log d/\log(1/s)`$ and why equality belongs to the divergent-energy boundary.

**Dependencies and story role:** M12, M16, M21, M23, M24. This turns the phase law into an exact feasibility and mode-count statement.

**Conceptual connection:** The same density-of-states mechanism determines both approximation costs and the possibility of exact finite-energy return.

**Source pointers:** Watrous §6.2.1 for the conversion framework; [exact success: finite energy](../science/exact_success.md#2-when-the-exact-catalyst-has-finite-energy); [mode threshold: exact return](../science/mode_threshold.md#2-exact-return-forces-tails-at-every-rank-scale); [minimum mode count](../science/mode_threshold.md#4-the-minimum-number-of-modes-for-exact-finite-energy-return).

## M26 — One oscillator gives a sharp exact energy budget

**Phase:** Narrative/innovation.

**Central question:** Why can the one-mode exact budget be determined beyond its asymptotic order?

**Understanding target:** Use the affine identity $`\mu(q)=d\mu(p)+(d-1)/2`$ and average tail monotonicity to derive the energy–success constraint. Explain how the self-similar construction saturates it, giving $`E_1(0;s,d)=s(d-1)/(1-ds)`$ for $`s\lt 1/d`$.

**Dependencies and story role:** M08, M11, M13, M15, M25. This identifies the special exact statement supported by the one-mode spectrum.

**Conceptual connection:** A precise relation between rank and photon number strengthens a matching-order result into an exact optimal budget.

**Source pointers:** Watrous §6.2.1 for finite-dimensional pure-state conversion foundations; [one-mode product identity](../science/spectral_energy.md#one-mode-product-identity); [sharp exact bound](../science/exact_success.md#3-a-sharp-one-mode-bound-for-every-energy-budget).

## M27 — Compactness controls catalysts that change with accuracy

**Phase:** Narrative/innovation.

**Central question:** Why does the sharp zero-error one-mode budget also determine the optimal small-error limit?

**Understanding target:** Explain bounded-moment tightness, preservation of normalized spectral mass and the order of passing fixed-tail inequalities to a limit before summing them. Distinguish this argument from setting the error to zero for one fixed catalyst.

**Dependencies and story role:** M11, M12, M20, M26. This completes the one-mode optimization when the chosen source may depend on the requested accuracy.

**Conceptual connection:** Energy control prevents probability mass from escaping to arbitrarily high Fock levels during the limit.

**Source pointers:** Watrous §1.1.3 and §3.2 for spectral and continuity foundations; the compactness argument is supplied locally: [sharp positive-error limit](../science/exact_success.md#4-the-sharp-positive-error-limit); [converse: subcritical limit](../science/converse.md#the-sharp-one-mode-subcritical-limit).

## M28 — Return on success, consumption on failure and growing support

**Phase:** Narrative/innovation.

**Central question:** What physical capability does the result provide once every branch and resource qualifier is retained?

**Understanding target:** Account for repeated exact successes with probability $`s^k`$, catalyst destruction on failure and finite-error cutoff growth. Distinguish initial mean photons, physical modes, largest occupied Fock level, preparation complexity and control work.

**Dependencies and story role:** M01, M05, M12, M15, M17, M24, M25, M26. This integrates the theorem into a complete operational interpretation.

**Conceptual connection:** Small mean inventory and accurate conditional return are compatible with rare high-energy components and eventual resource consumption.

**Source pointers:** Watrous §2.3.2 and §6.1.2 for instruments and LOCC; [interpretation: failure](../science/interpretation.md#what-happens-on-failure); [finite approximations and implementation resources](../science/interpretation.md#finite-approximations-and-implementation-resources); [construction: cutoff](../science/construction.md#6-the-cutoff-remains-a-resource).

## M29 — Credit the conversion tools and isolate the added conclusion

**Phase:** Narrative/innovation.

**Central question:** What remains after the closest established conversion mechanisms are credited?

**Understanding target:** Separate inherited Schmidt-tail monotones, stochastic root filters and infinite-dimensional conversion phenomena from the optimized energy threshold, critical logarithm and matching power exponent. Compare the task with thermal catalysis and catalytic distillation supplied with fresh resources without transferring their claims between models.

**Dependencies and story role:** M08, M09, M12, M20, M24, M27, M28. This locates the completed contribution within its actual scientific context.

**Conceptual connection:** A shared mathematical foundation does not identify the charged resource, supplied inputs or output guarantee of two different tasks.

**Source pointers:** Watrous §6.1.2 and §6.2.1 for the common finite-dimensional framework; [related work](../references/related_work.md); [interpretation: established conversion theory](../science/interpretation.md#relation-to-established-conversion-theory); [model: scope and attribution](../science/model.md#scope-and-attribution).

## M30 — Explain the complete result at its supported scope

**Phase:** Narrative/innovation.

**Central question:** How do the physical task, two proof routes and final limitations form one scientific account?

**Understanding target:** State the pure-catalyst, fixed-$`m,d,s\lt 1`$ task with conditional joint squared fidelity and destructive failure allowed. Explain how the explicit spectrum/filter and arbitrary-LOCC converse match through the oscillator density of states, identify the exact one-mode result, and retain the boundaries on mixed catalysts, changing parameters and implementation cost.

**Dependencies and story role:** M12–M29. This is the global synthesis of the project, with no additional unannounced prerequisite or claim.

**Conceptual connection:** The contribution is a success-dependent physical inventory law: a fixed number of modes determines when accurate joint return costs bounded, logarithmic or power-growing initial energy.

**Source pointers:** Watrous §3.2, §6.1.2 and §6.2.1 as the selected foundations; [scientific model and results](../science/model.md); [scientific reading route](../science/README.md); [physical interpretation](../science/interpretation.md); [verification boundaries](../verification/README.md).

