#!/usr/bin/env python3
"""Provisional Bayesian selector for daily-report inclusion probability."""

from __future__ import annotations

import argparse
import json
import math
import random
from pathlib import Path


FEATURE_PRIORS = {
    "landed_outcome": (1.10, 0.45),
    "quantified_evidence": (0.60, 0.40),
    "verified_operation": (0.90, 0.45),
    "closed_loop": (0.80, 0.45),
    "completed_fallback": (0.55, 0.40),
    "measured_funnel": (0.65, 0.45),
    "live_use": (0.75, 0.45),
    "pending_share": (-1.00, 0.45),
    "projected_value_share": (-0.65, 0.40),
    "verbosity_violation": (-0.85, 0.35),
    "core_overstatement": (-0.55, 0.40),
    "routine_volume_only": (-0.65, 0.40),
    "diffuse_task_list": (-0.55, 0.40),
    "unresolved_diagnosis": (-0.75, 0.40),
    "duplicated_content": (-1.10, 0.35),
}


def logistic(value: float) -> float:
    if value >= 0:
        z = math.exp(-value)
        return 1.0 / (1.0 + z)
    z = math.exp(value)
    return z / (1.0 + z)


def quantile(values: list[float], q: float) -> float:
    ordered = sorted(values)
    pos = (len(ordered) - 1) * q
    low = math.floor(pos)
    high = math.ceil(pos)
    if low == high:
        return ordered[low]
    return ordered[low] * (high - pos) + ordered[high] * (pos - low)


def load_payload(path: str | None) -> dict:
    if path:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    import sys

    return json.load(sys.stdin)


def validate_features(raw: dict) -> dict[str, float]:
    unknown = sorted(set(raw) - set(FEATURE_PRIORS))
    if unknown:
        raise ValueError(f"Unknown features: {', '.join(unknown)}")
    features = {name: float(raw.get(name, 0.0)) for name in FEATURE_PRIORS}
    invalid = {name: value for name, value in features.items() if not 0.0 <= value <= 1.0}
    if invalid:
        raise ValueError(f"Feature values must be within [0, 1]: {invalid}")
    return features


def estimate(payload: dict, draws: int, seed: int) -> dict:
    submissions = int(payload.get("actual_submissions", 43))
    quota = int(payload.get("quota", 3))
    if submissions <= quota or quota <= 0:
        raise ValueError("Require actual_submissions > quota > 0")

    features = validate_features(payload.get("features", {}))
    base_probability = quota / submissions
    base_logit = math.log(base_probability / (1.0 - base_probability))

    rng = random.Random(seed)
    probabilities = []
    for _ in range(draws):
        # The quota-derived base rate is fixed; uncertainty belongs to feature effects.
        log_odds = base_logit
        for name, value in features.items():
            mean, sd = FEATURE_PRIORS[name]
            log_odds += rng.gauss(mean, sd) * value
        probabilities.append(logistic(log_odds))

    estimate_value = sum(probabilities) / len(probabilities)
    return {
        "model_version": "provisional-bayes-v0.2",
        "probability_percent": round(estimate_value * 100, 2),
        "credible_interval_80_percent": [
            round(quantile(probabilities, 0.10) * 100, 2),
            round(quantile(probabilities, 0.90) * 100, 2),
        ],
        "base_rate_percent": round(base_probability * 100, 2),
        "actual_submissions": submissions,
        "quota": quota,
        "confidence": "low",
        "features": features,
        "warning": (
            "Exact model estimate, not a guaranteed real-world probability. "
            "Coefficient priors require calibration with complete same-day winner and non-winner data."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="UTF-8 JSON input; otherwise read stdin")
    parser.add_argument("--draws", type=int, default=30000)
    parser.add_argument("--seed", type=int, default=20260906)
    args = parser.parse_args()
    if args.draws < 1000:
        raise ValueError("draws must be at least 1000")
    print(json.dumps(estimate(load_payload(args.input), args.draws, args.seed), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
