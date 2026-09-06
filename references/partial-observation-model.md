# Partial-observation model

Use this reference because only the three daily winners are published; company-wide non-selected reports cannot be observed.

## Modeling target

Estimate `P(the user's report is selected today)` rather than claiming to model every employee or the full company decision boundary. The model can learn the published winner profile and the user's personal selection history, but missing company-wide negatives make population-level feature effects only partially identifiable.

## Daily data ledger

Record one prospective row per date before the result is known:

- date and rule-version identifier;
- the user's original and submitted report;
- the model's pre-result point estimate, interval, model version, and feature inputs;
- the user's eventual selected `1` or not selected `0` outcome;
- the three published winner reports and their role families;
- character count and any confirmed rule violations;
- nominal and, when known, actual candidate count and quota.

Never overwrite the pre-result prediction after observing the outcome. Store corrections as a new model version to prevent hindsight leakage.

## Three complementary components

### Published-winner profile

For each selection feature, maintain a beta posterior for its prevalence among published winners, for example:

`theta_f|winner ~ Beta(1 + winner_reports_with_f, 1 + winner_reports_without_f)`

This learns what winners commonly contain. It does not by itself estimate causal lift or selection probability because population negatives are missing.

### Personal longitudinal outcome model

Use the user's daily selected/non-selected outcomes as the only directly observed negative stream. Begin from the company base rate and shrink personal estimates toward it. Fit report features only with strong regularization; early personal data may contain few or no positive outcomes.

Treat the result as user-specific. Do not generalize the user's finance/admin pattern to other roles or all employees.

### Same-day pairwise comparison

On a day when the user is not selected, create three observed comparisons: each published winner outranks the user's report. Use these comparisons to learn relative rule match, such as whether the winners were shorter, more measurable, more closed, or more operationally verified.

These comparisons improve ranking signals but do not reveal the unobserved ordering of the other non-winners. Keep absolute probability anchored to the quota base rate and personal outcomes.

## Time and rule changes

Use prospective time-ordered updating. Recent evidence should matter more when administrator preferences change:

- maintain an explicit rule-version marker whenever leadership confirms a change;
- evaluate on later dates rather than randomly splitting reports from the same period;
- use gradual time decay or a state-space/random-walk coefficient model when enough data exists;
- never state fixed 14-day or 30-day weights as company rules unless empirically selected and validated.

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
