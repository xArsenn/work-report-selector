# Partial-observation model

Use this reference because only the daily winner set is published; company-wide non-selected reports cannot be observed, and the published winner count may vary.

## Modeling target

Estimate `P(the user's report is selected today)` rather than claiming to model every employee or the full company decision boundary. The model can learn the published winner profile and the user's personal selection history, but missing company-wide negatives make population-level feature effects only partially identifiable.

## Daily data ledger

Record one prospective row per date before the result is known:

- date and rule-version identifier;
- the user's original and submitted report;
- the model's pre-result point estimate, interval, model version, and feature inputs;
- the user's eventual selected `1` or not selected `0` outcome;
- the three published winner reports and their role families;
- writing provenance when known: employee-authored, skill-assisted, or unknown;
- character count and any confirmed rule violations;
- nominal and, when known, actual candidate count and quota.

Never overwrite the pre-result prediction after observing the outcome. Store corrections as a new model version to prevent hindsight leakage.

Apply the same prospective ledger discipline to weekly reports. Record the exact reporting cutoff and do not credit a prior week for payroll, signature, deployment, payment, reconciliation, or savings completed afterward. Later closure belongs to the next weekly row even when it completes the prior week's plan.

Writing provenance prevents causal overclaiming. A skill-assisted winner validates that the submitted content matched that day's selection, but it does not prove the skill caused selection. An employee-authored winner is useful evidence that the same structural pattern occurs independently of the skill's wording. Never use authorship source as a favorable selection feature.

When a prospective estimate is badly miscalibrated, append the unchanged prediction, outcome, and scoring loss to the ledger. Any feature-definition or coefficient change must receive a new model version and apply only to later reports. With only a few personal outcomes, prefer conservative shrinkage toward the quota prior over fitting coefficients to explain the latest case.

## Three complementary components

### Published-winner profile

For each selection feature, maintain a beta posterior for its prevalence among published winners, for example:

`theta_f|winner ~ Beta(1 + winner_reports_with_f, 1 + winner_reports_without_f)`

This learns what winners commonly contain. It does not by itself estimate causal lift or selection probability because population negatives are missing.

Repeated winners from the same reporter are not independent observations. Track reporter identity, estimate recurring patterns within that reporter, and use partial pooling or diminishing contribution so one prolific winner cannot dominate the published-winner profile. When enough reporters exist, validate learned features by holding out whole reporters rather than random reports. Use a recurring winner as a structural benchmark, not as evidence that their name, department, vocabulary, or access to engineering-style metrics should raise another employee's probability.

### Personal longitudinal outcome model

Use the user's daily selected/non-selected outcomes as the only directly observed negative stream. Begin from the company base rate and shrink personal estimates toward it. Fit report features only with strong regularization; early personal data may contain few or no positive outcomes.

Treat the result as user-specific. Do not generalize the user's finance/admin pattern to other roles or all employees.

For weekly outcomes, compare at the project level before fitting features. Repeated daily completions inside one week are correlated and must not be treated as independent evidence. A finance portfolio with several unrelated deliverables is different from one central automation or control system reaching stable use.

### Same-day pairwise comparison

On a day when the user is not selected, create three observed comparisons: each published winner outranks the user's report. Use these comparisons to learn relative rule match, such as whether the winners were shorter, more measurable, more closed, or more operationally verified.

These comparisons improve ranking signals but do not reveal the unobserved ordering of the other non-winners. Keep absolute probability anchored to the quota base rate and personal outcomes.

## Time and rule changes

Use prospective time-ordered updating. Recent evidence should matter more when administrator preferences change:

- maintain an explicit rule-version marker whenever leadership confirms a change;
- evaluate on later dates rather than randomly splitting reports from the same period;
- use gradual time decay or a state-space/random-walk coefficient model when enough data exists;
- never state fixed 14-day or 30-day weights as company rules unless empirically selected and validated.

For the rule reset effective 2026-09-17, start a new theme-regime ledger. Do not decay or blend legacy coefficients into it. Record the official theme, official winner reasons, and whether the theme is later confirmed to rotate. A theme change creates a new context within the regime; retain shared evidence about theme matching but calibrate theme-specific features separately.

Record 2026-09-18 with an actual quota of four and base rate `4/43 = 9.30%`. Treat this as a period-specific observation, not proof that the default quota permanently changed from three. The second winner set strengthens the qualitative theme definition but still cannot identify coefficient sizes without same-day non-winners.

Record 2026-09-19 as the third complete winner set in the same confirmed theme week, using the default observed quota of three unless an official count changes it. Use its three method chains to refine feature-assignment anchors. Do not treat another winner-only set as evidence for increasing coefficient means.

For 2026-09-20, preserve the previously stated 49.77% estimate for the user's proposed daily draft and the published three-winner list, which did not include the user. The exact submitted text has not been confirmed, so do not enter this as a verified prospective prediction/outcome pair for that submitted report or calculate a formal Brier score until submission provenance is confirmed. Even if confirmed, one miss is a calibration warning, not enough to identify a causal feature effect. Review possible double-counting among `theme_alignment`, `reusable_method`, `method_artifact`, and `transferability` when one generic coordination sequence supplied all four scores; do not silently change the prior estimate or coefficient means.

## Calibration

Track Brier score, log loss, and calibration by probability band using only pre-result predictions. Because the data is personal and partially observed, also report the number of personal prediction days, personal wins, published winners observed, and current rule-version age.

Do not narrow the credible interval merely because many published winners were collected; personal negative and positive outcomes are what calibrate the user's absolute probability.

## Output limitations

Always state that:

- the estimate is for this user's report, not the whole company;
- the three published winners inform relative rule match;
- unobserved company non-winners prevent full decision-boundary recovery;
- confidence rises through prospective personal outcomes, not retrospective rewriting;
- the numeric estimate remains model-dependent and competitive because only three of the daily candidate pool are selected.
