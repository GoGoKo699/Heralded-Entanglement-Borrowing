#!/usr/bin/env python3
"""Deterministic finite checks of the heralded borrowing construction.

Only the Python standard library is used. These calculations test explicit
states and instruments; they do not prove the universal LOCC converse.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


getcontext().prec = 100
D = Decimal
ASSERTIONS = 0


def require(condition: bool, explanation: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(explanation)


def dec(value: Fraction | int | Decimal) -> Decimal:
    if isinstance(value, Fraction):
        return D(value.numerator) / D(value.denominator)
    return D(value)


def close(actual: Decimal, expected: Decimal, message: str,
          tolerance: Decimal = D("1e-75")) -> None:
    require(abs(actual - expected) <= tolerance * max(D(1), abs(expected)),
            f"{message}: {actual} versus {expected}")


def shown(value: Fraction | int | Decimal) -> str:
    converted = dec(value)
    return "0.000000000000E+0" if converted == 0 else format(converted, ".12E")


def geometric_sum(ratio: Fraction, length: int) -> Fraction:
    """Sum ratio**ell for ell=1,...,length, including ratio=1."""
    if ratio == 1:
        return Fraction(length)
    return ratio * (1 - ratio ** length) / (1 - ratio)


def tree_vector(d: int, success: Fraction, level: int) -> list[Fraction]:
    """Build p by its parent relation, independently of block sums."""
    cutoff = d ** level
    root = (1 - success) / (1 - success / d)
    raw = [root]
    for j in range(2, cutoff + 1):
        parent = (j + d - 1) // d
        raw.append(success / d * raw[parent - 1])
    normalizer = sum(raw, Fraction())
    return [value / normalizer for value in raw]


def target_vector(p: list[Fraction], d: int) -> list[Fraction]:
    return [value / d for value in p for _ in range(d)]


def tail(vector: list[Fraction], k: int) -> Fraction:
    return sum(vector[k:], Fraction())


def stable_infidelity(q_root: Fraction, moved_mass: Fraction) -> Decimal:
    """Evaluate 1-F without subtracting two nearly equal unit numbers.

    With x=q_root+b, 1-sqrt(F)=x-sqrt(q_root*x)
    =b*x/(x+sqrt(q_root*x)). Return h*(2-h).
    """
    a, b = dec(q_root), dec(moved_mass)
    x = a + b
    h = b * x / (x + (a * x).sqrt())
    return h * (2 - h)


def single_mode_aggregate(d: int, success: Fraction,
                          level: int) -> dict[str, Fraction | Decimal]:
    """Block moments without allocating the exponentially large vector."""
    root = (1 - success) / (1 - success / d)
    z = root * (1 + Fraction(d - 1, d) * geometric_sum(success, level))
    energy = (root * Fraction(d - 1, d)
              * (Fraction(d + 1, d) * geometric_sum(d * success, level)
                 - geometric_sum(success, level)) / z)
    q_root = root / z / d
    moved_mass = root * Fraction(d - 1, d) * success ** level / z
    return {"normalizer": z, "energy": energy, "q_root": q_root,
            "moved_mass": moved_mass,
            "infidelity": stable_infidelity(q_root, moved_mass)}


def fock_energy(modes: int, index: int) -> int:
    """Energy of the index-th Fock state, index starting at one."""
    low, high = -1, 1
    while math.comb(high + modes, modes) < index:
        high *= 2
    while high - low > 1:
        middle = (low + high) // 2
        if math.comb(middle + modes, modes) >= index:
            high = middle
        else:
            low = middle
    return high


def fock_energy_sum(modes: int, count: int) -> int:
    """Sum the first count energies by exact degeneracy counting."""
    if count == 0:
        return 0
    last = fock_energy(modes, count)
    if last == 0:
        return 0
    below = math.comb(last - 1 + modes, modes)
    complete_sum = modes * math.comb(last + modes - 1, modes + 1)
    return complete_sum + last * (count - below)


def mode_aggregate(modes: int, d: int, success: Fraction,
                   level: int) -> Fraction:
    root = (1 - success) / (1 - success / d)
    z = root * (1 + Fraction(d - 1, d) * geometric_sum(success, level))
    energy = Fraction()
    previous_count = 1
    for ell in range(1, level + 1):
        count = d ** ell
        shell_energy = (fock_energy_sum(modes, count)
                        - fock_energy_sum(modes, previous_count))
        energy += 2 * root * (success / d) ** ell * shell_energy
        previous_count = count
    return energy / z


def minimum_modes(d: int, success: Fraction) -> int:
    modes = 1
    while d * success ** modes >= 1:  # Strict finite-energy inequality.
        modes += 1
    return modes


def check_explicit_instruments() -> list[dict[str, object]]:
    cases = [(2, Fraction(1, 4), 0), (2, Fraction(1, 4), 5),
             (2, Fraction(1, 2), 6), (2, Fraction(3, 4), 6),
             (3, Fraction(1, 3), 4), (3, Fraction(2, 3), 4)]
    records = []
    for d, success, level in cases:
        p = tree_vector(d, success, level)
        q = target_vector(p, d)
        cutoff = len(p)
        require(sum(p) == 1 and sum(q) == 1, "source and target normalization")
        require(all(p[j] >= p[j + 1] for j in range(cutoff - 1)),
                "Schmidt coefficients must be sorted")
        root_filter = 1 - (1 - success) / p[0]
        require(0 <= root_filter <= 1, "root filter is a contraction")
        accepted = [p[0] * root_filter] + p[1:]
        require(sum(accepted) == success, "physical success probability is s")
        require(p[0] * (1 - root_filter) == 1 - success,
                "failure is the vacuum root and consumes the source")
        r = [value / success for value in accepted]
        require(sum(r) == 1, "conditional success spectrum is normalized")
        require(r[1:] == q[1:cutoff], "all nonroot accepted amplitudes match")
        b = tail(q, cutoff)
        require(r[0] == q[0] + b, "target tail is moved to the root")

        # This full vector overlap tests the quotient/remainder indexing.
        affinity = sum((dec(x * y).sqrt() for x, y in zip(r, q)), D(0))
        direct_error = 1 - affinity * affinity
        error = stable_infidelity(q[0], b)
        close(error, direct_error, "stable formula agrees with full overlap")
        require(0 < error <= 2 * dec(b), "conditional error bound")
        energy = 2 * sum((j * value for j, value in enumerate(p)), Fraction())
        target_index_energy = 2 * sum(
            (j * value for j, value in enumerate(q)), Fraction())
        require(target_index_energy == d * energy + d - 1,
                "passive index identity includes both oscillator factors")
        aggregate = single_mode_aggregate(d, success, level)
        require(energy == aggregate["energy"], "vector and block energies agree")
        require(b == aggregate["moved_mass"], "vector and block target tails agree")
        close(error, aggregate["infidelity"], "vector and block errors agree")

        # The unconditioned output includes the destructive failure branch.
        unconditional_fidelity = dec(success) * (1 - error) + dec((1 - success) * q[0])
        require(1 - unconditional_fidelity + D("1e-75") >= error,
                "unconditional fidelity includes the failed trials")
        if cutoff > 1:
            require(1 - unconditional_fidelity > error,
                    "success-conditioned error must not be called unconditional")
        require(1 - unconditional_fidelity >= dec((1 - success) * (1 - q[0])),
                "failure contribution is charged in an unconditioned record")

        tested_tails = sorted({1, cutoff // 2, cutoff, d * cutoff})
        for k in tested_tails:
            if k == 0:
                continue
            pk, qk, rk = tail(p, k), tail(q, k), tail(r, k)
            require(pk >= success * rk, "finite instrument's average-tail monotonicity")
            lower = dec(success) * max(D(0), dec(qk).sqrt() - (2 * error).sqrt()) ** 2
            require(dec(pk) + D("1e-75") >= lower,
                    "finite example satisfies the Hellinger-tail bound")
        if cutoff > 1:
            # A local isometry tags root/rest with environment overlap 99/100.
            # Discarding that environment gives a genuinely mixed retained state.
            root_overlap = dec(r[0] * q[0]).sqrt()
            rest_overlap = affinity - root_overlap
            mixed_error = error + D("0.02") * root_overlap * rest_overlap
            require(mixed_error > error, "discarded local record lowers target fidelity")
            for k in tested_tails:
                if k == 0:
                    continue
                lower = dec(success) * max(
                    D(0), dec(tail(q, k)).sqrt() - (2 * mixed_error).sqrt()) ** 2
                require(dec(tail(p, k)) + D("1e-75") >= lower,
                        "mixed retained example satisfies the complete-branch bound")

        records.append({"d": d, "s": str(success), "L": level,
                        "cutoff": cutoff, "energy": shown(energy),
                        "success": str(sum(accepted)), "conditional_infidelity": shown(error),
                        "unconditional_infidelity": shown(1 - unconditional_fidelity)})
    return records


def check_asymptotic_regimes() -> dict[str, object]:
    sub = single_mode_aggregate(2, Fraction(1, 4), 120)
    exact_limit = Fraction(1, 2)
    close(dec(sub["energy"]), dec(exact_limit), "subcritical energy approaches sharp limit",
          D("1e-35"))
    require(sub["energy"] < exact_limit, "finite cutoff lies below its exact-return limit")

    critical = []
    for d in (2, 3):
        a = single_mode_aggregate(d, Fraction(1, d), 100)
        b = single_mode_aggregate(d, Fraction(1, d), 200)
        slope = (dec(b["energy"]) - dec(a["energy"])) / 100
        close(slope, D(d - 1) / d, "critical energy grows linearly with shell count",
              D("1e-25"))
        critical.append({"d": d, "energy_per_extra_shell": shown(slope),
                         "L200_error": shown(b["infidelity"])})

    supercritical = []
    for d, success in ((2, Fraction(3, 4)), (3, Fraction(2, 3))):
        a = single_mode_aggregate(d, success, 100)
        b = single_mode_aggregate(d, success, 200)
        measured = (dec(b["energy"]) / dec(a["energy"])).ln() / (
            a["infidelity"] / b["infidelity"]).ln()
        predicted = dec(d * success).ln() / (-dec(success).ln())
        close(measured, predicted, "energy/error slope has the claimed full power",
              D("1e-12"))
        require(abs(measured - predicted / 2) > D("0.1"),
                "squared fidelity must not halve the exponent")
        supercritical.append({"d": d, "s": str(success),
                              "predicted_exponent": shown(predicted),
                              "measured_exponent_L100_to_L200": shown(measured),
                              "L200_energy": shown(b["energy"]),
                              "L200_error": shown(b["infidelity"])})
    tiny = single_mode_aggregate(2, Fraction(1, 4), 400)
    require(D(0) < tiny["infidelity"] < D("1e-200"),
            "stable infidelity remains nonzero far below unit-roundoff")
    return {"subcritical_limit": str(exact_limit),
            "subcritical_L120_energy": shown(sub["energy"]),
            "critical": critical, "supercritical": supercritical,
            "stable_L400_infidelity": shown(tiny["infidelity"])}


def check_fock_counting_and_passivity() -> dict[str, object]:
    counts = []
    for modes in range(1, 5):
        max_photons = 6
        enumerated = sorted(sum(state) for state in itertools.product(
            range(max_photons + 1), repeat=modes) if sum(state) <= max_photons)
        require(len(enumerated) == math.comb(max_photons + modes, modes),
                "enumerated cumulative Fock degeneracy equals binomial count")
        for photons in range(max_photons + 1):
            require(enumerated.count(photons) == math.comb(photons + modes - 1, modes - 1),
                    "energy shell degeneracy")
        for index, photons in enumerate(enumerated, 1):
            require(fock_energy(modes, index) == photons,
                    "inverse cumulative Fock indexing")
        require(fock_energy_sum(modes, len(enumerated)) == sum(enumerated),
                "closed Fock energy sum agrees with enumeration")
        p = tree_vector(2, Fraction(3, 4), 5)
        energies = [fock_energy(modes, j) for j in range(1, len(p) + 1)]
        passive = 2 * sum((e * x for e, x in zip(energies, p)), Fraction())
        reversed_basis = 2 * sum((e * x for e, x in zip(reversed(energies), p)), Fraction())
        require(reversed_basis >= passive, "tested nonpassive basis costs at least passive energy")
        # An explicit real unitary rotation of the first and final basis states:
        # cos(theta)=3/5, sin(theta)=4/5. Its energy penalty is exact.
        penalty = 2 * Fraction(16, 25) * (p[0] - p[-1]) * (energies[-1] - energies[0])
        require(penalty > 0, "local basis rotation cannot reduce the passive minimum")
        by_tails = 2 * sum(((energies[k] - energies[k - 1]) * tail(p, k)
                            for k in range(1, len(p))), Fraction())
        require(by_tails == passive, "degenerate-spectrum summation by parts")
        require(mode_aggregate(modes, 2, Fraction(3, 4), 5) == passive,
                "mode block formula agrees with explicit energy assignment")
        counts.append({"modes_per_party": modes, "states_through_6_photons": len(enumerated),
                       "test_source_total_photons": shown(passive),
                       "rotated_basis_total_photons": shown(passive + penalty)})
    for d, success, level in ((2, Fraction(1, 4), 120),
                              (2, Fraction(3, 4), 160),
                              (3, Fraction(1, 3), 100)):
        require(mode_aggregate(1, d, success, level)
                == single_mode_aggregate(d, success, level)["energy"],
                "one-mode Fock sum matches independently derived affine-energy formula")
    return {"enumeration": counts}


def check_fixed_mode_regimes() -> dict[str, object]:
    critical = []
    for modes, d in ((2, 4), (3, 8)):
        success = Fraction(1, 2)
        a, b = mode_aggregate(modes, d, success, 40), mode_aggregate(modes, d, success, 80)
        measured = (dec(b) - dec(a)) / 40
        alpha = D(1) / modes
        root = dec((1 - success) / (1 - success / d))
        predicted = (2 * root * (D(math.factorial(modes)).ln() * alpha).exp()
                     * D(modes) / (modes + 1)
                     * (1 - (-(1 + alpha) * D(d).ln()).exp()))
        close(measured, predicted, "critical multimode shell slope from density of states",
              D("1e-10"))
        critical.append({"modes_per_party": modes, "d": d, "s": str(success),
                         "predicted_energy_per_extra_shell": shown(predicted),
                         "measured_L40_to_L80": shown(measured)})

    modes, d, success = 2, 4, Fraction(3, 4)
    ea, eb = mode_aggregate(modes, d, success, 100), mode_aggregate(modes, d, success, 200)
    da = single_mode_aggregate(d, success, 100)["infidelity"]
    db = single_mode_aggregate(d, success, 200)["infidelity"]
    measured = (dec(eb) / dec(ea)).ln() / (da / db).ln()
    predicted = (D(d).ln() / modes + dec(success).ln()) / (-dec(success).ln())
    close(measured, predicted, "multimode energy/error exponent", D("1e-10"))
    bounded_a = mode_aggregate(2, 4, Fraction(1, 4), 100)
    bounded_b = mode_aggregate(2, 4, Fraction(1, 4), 120)
    close(dec(bounded_a), dec(bounded_b), "subcritical multimode energy is convergent",
          D("1e-25"))

    thresholds = []
    for target_dimension, chance, expected in ((2, Fraction(1, 2), 2),
                                               (2, Fraction(9, 10), 7),
                                               (4, Fraction(1, 2), 3),
                                               (8, Fraction(1, 2), 4)):
        obtained = minimum_modes(target_dimension, chance)
        require(obtained == expected, "minimum-mode count respects the strict threshold")
        require(target_dimension * chance ** obtained < 1,
                "chosen mode count lies strictly below critical success")
        require(obtained == 1 or target_dimension * chance ** (obtained - 1) >= 1,
                "one fewer mode is critical or supercritical")
        thresholds.append({"d": target_dimension, "s": str(chance),
                           "minimum_modes_per_party": obtained})
    return {"critical": critical,
            "supercritical_two_mode_predicted_exponent": shown(predicted),
            "supercritical_two_mode_measured_exponent": shown(measured),
            "subcritical_two_mode_L120_energy": shown(bounded_b),
            "minimum_modes": thresholds}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-expected", action="store_true",
                        help="replace the expected numerical summary after reviewing a scientific change")
    args = parser.parse_args()
    results = {"schema_version": 1,
               "explicit_instruments": check_explicit_instruments(),
               "single_mode_regimes": check_asymptotic_regimes(),
               "fock_counting_and_passivity": check_fock_counting_and_passivity(),
               "fixed_mode_regimes": check_fixed_mode_regimes()}
    expected_path = Path(__file__).with_name("expected_results.json")
    if args.write_expected:
        expected_path.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    else:
        expected = json.loads(expected_path.read_text(encoding="utf-8"))
        require(results == expected, "numerical summary differs from the reviewed expected results")
    print(json.dumps({"status": "passed", "finite_assertions": ASSERTIONS,
                      "groups": list(results.keys())[1:],
                      "expected_results": expected_path.name,
                      "scope": "Explicit finite examples and asymptotic construction checks; not a proof of the universal LOCC bound."},
                     indent=2))


if __name__ == "__main__":
    main()
