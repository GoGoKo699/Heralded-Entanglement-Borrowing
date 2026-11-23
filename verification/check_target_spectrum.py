"""Finite checks for borrowing a fixed, nonuniform pure target.

Exact rational tests compare the word forest with independent tensor sorting,
finite fixed-point iteration and top-k allocation. Decimal scaling diagnostics
retain their finite scope; they are not proofs of the infinite-rank law.
"""

from __future__ import annotations

import heapq
import itertools
import math
from decimal import Decimal as D
from fractions import Fraction as F


def decimal(value: F | int) -> D:
    if isinstance(value, F):
        return D(value.numerator) / D(value.denominator)
    return D(value)


def forest_prefix(target: tuple[F, ...], success: F, count: int) -> list[F]:
    """Largest count entries of the root-pruned word forest, with multiplicity."""
    root = (1 - success) / (1 - success * target[0])
    result = [root]
    queue: list[tuple[F, int]] = []
    serial = itertools.count()
    for value in target[1:]:
        heapq.heappush(queue, (-root * success * value, next(serial)))
    while len(result) < count:
        negative, _ = heapq.heappop(queue)
        value = -negative
        result.append(value)
        for factor in target:
            heapq.heappush(queue, (-value * success * factor, next(serial)))
    return result


def brute_forest(target: tuple[F, ...], success: F, depth: int) -> list[F]:
    """Enumerate every word through a depth, without heap recursion."""
    root = (1 - success) / (1 - success * target[0])
    values = [root]
    for length in range(1, depth + 1):
        for first in range(1, len(target)):
            for rest in itertools.product(range(len(target)), repeat=length - 1):
                value = root * success ** length * target[first]
                for symbol in rest:
                    value *= target[symbol]
                values.append(value)
    return sorted(values, reverse=True)


def tensor_sorted(source: list[F], target: tuple[F, ...]) -> list[F]:
    return sorted((p * value for p in source for value in target), reverse=True)


def map_f(source: list[F], target: tuple[F, ...], success: F) -> list[F]:
    output = [success * value for value in tensor_sorted(source, target)]
    output[0] += 1 - success
    return output


def tail(source: list[F], cutoff: int) -> F:
    return sum(source[cutoff:], F())


def allocations(total: int, parts: int, maximum: int):
    if parts == 1:
        if 0 <= total <= maximum:
            yield (total,)
        return
    for first in range(max(0, total - (parts - 1) * maximum), min(total, maximum) + 1):
        for rest in allocations(total - first, parts - 1, maximum):
            yield (first,) + rest


def majorized(left: list[F], right: list[F]) -> bool:
    """Exact finite ordinary majorization, padding zeros."""
    left, right = sorted(left, reverse=True), sorted(right, reverse=True)
    if sum(left) != sum(right):
        return False
    lp, rp = F(), F()
    for index in range(max(len(left), len(right))):
        lp += left[index] if index < len(left) else 0
        rp += right[index] if index < len(right) else 0
        if lp > rp:
            return False
    return True


def q_root(target: tuple[F, ...], success: F) -> D:
    """Solve sum_i (s lambda_i)^q=1 by high-precision bisection."""
    logs = [decimal(success * value).ln() for value in target]
    low, high = D(0), D(1)
    for _ in range(280):
        middle = (low + high) / 2
        if sum(((middle * value).exp() for value in logs), D(0)) > 1:
            low = middle
        else:
            high = middle
    return (low + high) / 2


def run_target_spectrum_checks(require, shown, stable_infidelity, fock_energy):
    records = []
    cases = [((F(9, 10), F(1, 10)), F(3, 5)),
             ((F(3, 5), F(3, 10), F(1, 10)), F(2, 5)),
             ((F(2, 5), F(2, 5), F(1, 5)), F(1, 2)),
             ((F(1, 2), F(1, 2)), F(3, 4))]
    for target, success in cases:
        raw = forest_prefix(target, success, 40)
        depth = 0
        root = raw[0]
        while root * success * target[1] * (success * target[0]) ** depth >= raw[-1]:
            depth += 1
        enumerated = brute_forest(target, success, depth)
        require(enumerated[:len(raw)] == raw,
                "heap word forest agrees with independent exhaustive word enumeration")
        require(sum(raw) < 1 and all(value > 0 for value in raw),
                "finite forest prefix has positive omitted mass")
        infinite_target_prefix = tensor_sorted(enumerated, target)[:len(raw)]
        require(infinite_target_prefix[0] == root * target[0],
                "largest infinite-target coefficient")
        require(infinite_target_prefix[1:] == [value / success for value in raw[1:]],
                "root-pruned multiset solves the nonroot fixed-point identity")
        require(root == 1 - success + success * infinite_target_prefix[0],
                "root solves the affine fixed-point identity")
        finite_cases = []
        for cutoff in (1, 2, 3, 7, 16, 33):
            prefix = raw[:cutoff]
            normalizer = sum(prefix)
            omitted = 1 - normalizer
            source = [value / normalizer for value in prefix]
            target_vector = tensor_sorted(source, target)
            require(target_vector[:cutoff] == [value / normalizer
                    for value in infinite_target_prefix[:cutoff]],
                    "top-R tensor coefficients survive normalized truncation, including tied cuts")
            root_filter = 1 - (1 - success) / source[0]
            require(0 <= root_filter <= 1, "arbitrary-target root filter is a contraction")
            success_diagonal = [root_filter] + [F(1)] * (cutoff - 1)
            failure_diagonal = [1 - root_filter] + [F()] * (cutoff - 1)
            require(all(a + b == 1 for a, b in zip(success_diagonal, failure_diagonal)),
                    "complete two-outcome diagonal instrument")
            accepted = [p * factor for p, factor in zip(source, success_diagonal)]
            failed = [p * factor for p, factor in zip(source, failure_diagonal)]
            require(sum(accepted) == success and sum(failed) == 1 - success,
                    "exact-s success and charged complementary failure")
            require(failed[0] == 1 - success and all(value == 0 for value in failed[1:]),
                    "failure branch is the product vacuum root")
            conditional = [value / success for value in accepted]
            moved = tail(target_vector, cutoff)
            formula_mass = (1 - success) * omitted / (success * normalizer)
            require(moved == formula_mass,
                    "omitted finite-target mass includes the factor 1-s")
            require(conditional[0] == target_vector[0] + moved
                    and conditional[1:] == target_vector[1:cutoff],
                    "successful output moves only the omitted target mass to its root")
            affinity = sum((decimal(p * q).sqrt() for p, q in
                            zip(conditional, target_vector)), D(0))
            error = stable_infidelity(target_vector[0], moved)
            require(abs((1 - affinity ** 2) - error) < D("1e-80"),
                    "joint squared fidelity agrees with the full vector overlap")
            require(0 < error <= 2 * decimal(moved),
                    "arbitrary-target squared joint infidelity bound")
            for k in sorted({1, cutoff // 2, cutoff, len(target_vector)}):
                if k == 0:
                    continue
                require(tail(source, k) >= success * tail(conditional, k),
                        "finite arbitrary-target instrument obeys average-tail monotonicity")
                lower = decimal(success) * max(D(0), decimal(tail(target_vector, k)).sqrt()
                                               - (2 * error).sqrt()) ** 2
                require(decimal(tail(source, k)) + D("1e-80") >= lower,
                        "finite arbitrary-target example obeys the Hellinger-tail inequality")
            energies = []
            for modes in (1, 2, 3):
                labels = sorted(sum(state) for state in itertools.product(
                    range(cutoff + 1), repeat=modes) if sum(state) <= cutoff)
                ordered = labels[:cutoff]
                require(ordered == [fock_energy(modes, j) for j in range(1, cutoff + 1)],
                        "independent Fock occupation enumeration gives the ordered passive energies")
                energy = 2 * sum((p * e for p, e in zip(source, ordered)), F())
                by_tails = 2 * sum(((ordered[k] - ordered[k - 1]) * tail(source, k)
                                    for k in range(1, cutoff)), F())
                require(energy == by_tails,
                        "nonuniform multimode passive energy equals its weighted tail sum")
                if cutoff <= 7:
                    alternative_min = min(sum((p * e for p, e in zip(source, assignment)), F())
                                          for assignment in set(itertools.permutations(ordered)))
                    require(energy == 2 * alternative_min,
                            "exhaustive basis assignments attain the decreasing-spectrum passive minimum")
                energies.append(shown(energy))
            finite_cases.append({"cutoff": cutoff, "success": str(sum(accepted)),
                                 "normalizer": shown(normalizer),
                                 "conditional_joint_infidelity": shown(error),
                                 "total_photons_modes_1_2_3": energies})
        records.append({"target": [str(value) for value in target], "s": str(success),
                        "exhaustive_word_depth": depth,
                        "ties_present": len(set(raw)) < len(raw),
                        "finite_instruments": finite_cases})

    # Independent finite iterates of F_s produce normalized spectra. No word
    # forest is used to compute them. Their top probabilities converge to it.
    iterations = []
    for target, success in cases[:3]:
        actual = [F(1)]
        other = [F(1, 2), F(1, 3), F(1, 6)]
        ideal = forest_prefix(target, success, 20)
        for step in range(1, 8):
            actual, other = map_f(actual, target, success), map_f(other, target, success)
            require(sum(actual) == 1 and sum(other) == 1,
                    "finite tensor-sort fixed-point iterates stay normalized")
            l1 = sum((abs((actual[j] if j < len(actual) else 0)
                          - (other[j] if j < len(other) else 0))
                      for j in range(max(len(actual), len(other)))), F())
            require(l1 <= success ** step,
                    "independent-start F_s iterations satisfy the l1 contraction bound")
            require(sum(abs(a - b) for a, b in zip(actual, ideal)) <= 2 * success ** step,
                    "finite F_s iteration agrees with the independent word-forest prefix")
            require(all(sum(actual[:k]) >= sum(ideal[:k])
                        for k in range(1, min(len(actual), len(ideal)) + 1)),
                    "pure-start fixed-point iterates majorize the ideal prefix")
        iterations.append({"target": [str(value) for value in target], "s": str(success),
                           "iterations": 7, "final_rank": len(actual),
                           "prefix_l1_difference": shown(sum(abs(a - b)
                                                             for a, b in zip(actual, ideal)))})

    # Check isotonicity on rational T-transforms and the min-allocation tail
    # identity independently of any forest construction.
    allocation_cases = 0
    for target, success in cases[:3]:
        sharp = [F(1, 2), F(1, 4), F(1, 8), F(1, 8)]
        mixed = sharp[:]
        mixed[0], mixed[-1] = ((2 * sharp[0] + sharp[-1]) / 3,
                               (sharp[0] + 2 * sharp[-1]) / 3)
        mixed.sort(reverse=True)
        require(majorized(mixed, sharp), "rational T-transform supplies the test majorization")
        require(majorized(map_f(mixed, target, success), map_f(sharp, target, success)),
                "F_s preserves the tested independent majorization")
        for source in (sharp, mixed):
            tensor = tensor_sorted(source, target)
            for k in range(len(tensor) + 1):
                best = min(sum((value * tail(source, allocated)
                                for value, allocated in zip(target, choice)), F())
                           for choice in allocations(k, len(target), len(source)))
                require(best == tail(tensor, k),
                        "exhaustive top-k allocation equals the directly sorted tensor tail")
                allocation_cases += 1

    # Uniform targets recover the existing parent-index construction exactly,
    # including truncations through tied blocks rather than only full levels.
    uniform_cases = []
    for rank, success in ((2, F(3, 4)), (3, F(2, 3)), (4, F(1, 2))):
        target = (F(1, rank),) * rank
        raw = forest_prefix(target, success, 80)
        recurrence = [raw[0]]
        for j in range(2, len(raw) + 1):
            recurrence.append(success / rank * recurrence[(j + rank - 1) // rank - 1])
        require(raw == recurrence, "uniform target forest equals the existing parent recurrence")
        q = q_root(target, success)
        known = D(rank).ln() / (D(rank).ln() - decimal(success).ln())
        require(abs(q - known) < D("1e-80"),
                "general spectrum counting root recovers the uniform-target exponent")
        uniform_cases.append({"rank": rank, "s": str(success), "q_s": shown(q)})

    threshold = (F(9, 10), F(1, 10))
    critical = F(5, 8)
    require(critical * threshold[0] == F(9, 16)
            and critical * threshold[1] == F(1, 16),
            "nonuniform one-mode critical weights have exact square roots 3/4 and 1/4")
    require(F(3, 4) + F(1, 4) == 1, "exact critical square-root equation")
    roots = [(success, q_root(threshold, success))
             for success in (F(1, 2), critical, F(3, 4))]
    require(roots[0][1] < D("0.5") and abs(roots[1][1] - D("0.5")) < D("1e-80")
            and roots[2][1] > D("0.5"),
            "strict nonuniform phase boundary distinguishes subcritical, critical and supercritical")
    require(critical > F(1, 2), "same-rank nonuniform target has a different exact success threshold")

    scaling = []
    for success, q in roots:
        raw = forest_prefix(threshold, success, 8192)
        samples = []
        for cutoff in (256, 1024, 4096, 8192):
            prefix = raw[:cutoff]
            mass = sum(prefix)
            omitted = 1 - mass
            # Use the unnormalized passive moment to separate the spectrum
            # tail diagnostic from the finite-catalyst normalization effect.
            energy = 2 * sum((j * p for j, p in enumerate(prefix)), F())
            samples.append({"cutoff": cutoff, "ideal_tail": shown(omitted),
                            "unnormalized_total_photons": shown(energy)})
        b = 1 / q - 1
        ratios = [decimal(1 - sum(raw[:cutoff])) * D(cutoff) ** b
                  for cutoff in (256, 1024, 4096, 8192)]
        require(max(ratios) / min(ratios) < D(2),
                "finite nonuniform tails corroborate the predicted counting power within a bounded factor")
        measured_tail = -(decimal(1 - sum(raw)) / decimal(1 - sum(raw[:1024]))).ln() / D(8).ln()
        require(abs(measured_tail - b) < D("0.08"),
                "finite nonuniform tail slope corroborates the predicted exponent")
        energies = [2 * sum((j * p for j, p in enumerate(raw[:cutoff])), F())
                    for cutoff in (256, 1024, 4096, 8192)]
        require(all(a < b for a, b in zip(energies, energies[1:])),
                "partial passive energies increase with the ideal cutoff")
        if success == critical:
            slope_first = (decimal(energies[1]) - decimal(energies[0])) / D(4).ln()
            slope_second = (decimal(energies[2]) - decimal(energies[1])) / D(4).ln()
            require(abs(slope_second / slope_first - 1) < D("0.05"),
                    "nonuniform critical passive energy is approximately linear in log cutoff")
        elif success > critical:
            measured_energy = (decimal(energies[-1]) / decimal(energies[1])).ln() / D(8).ln()
            require(abs(measured_energy - (1 - b)) < D("0.10"),
                    "finite supercritical energy growth corroborates the predicted cutoff power")
        else:
            increment_early = decimal(energies[1] - energies[0])
            increment_late = decimal(energies[2] - energies[1])
            require(increment_late < increment_early,
                    "nonuniform subcritical energy increments decline on geometric cutoffs")
        scaling.append({"target": [str(value) for value in threshold], "s": str(success),
                        "q_s": shown(q), "predicted_tail_power": shown(b),
                        "measured_tail_power_R1024_to_R8192": shown(measured_tail),
                        "samples": samples})

    return {"finite_instruments": records, "independent_fixed_point_iterations": iterations,
            "exhaustive_allocation_identities": allocation_cases,
            "uniform_special_cases": uniform_cases,
            "nonuniform_one_mode_critical_success": str(critical),
            "finite_scaling_diagnostics": scaling}
