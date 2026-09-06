# Bayesian probability model

Use this reference when the user asks for selection probability, Bayesian updating, or probability calibration.

## Separation from quality score

The 100-point rubric evaluates whether the report is well written. This model evaluates whether it is likely to be selected under the administrator's rules and fixed quota. Keep both outputs. Never convert points into probability, define a score-to-probability lookup table, or assume that a higher-quality report necessarily has higher selection probability.

Build probability from selection outcomes and rule features: confirmed constraints, patterns separating winners from non-winners, role, date, candidate pool, and quota. A quality dimension may be included only as a separately measured feature if historical data proves predictive value; never use the total score as the target or shortcut.

## Confirmed base rate

- Company headcount: 49.
- Core managers exempt from daily reports: 6.
- Nominal daily candidate pool: 43.
- Daily winners: 3.
- Exchangeable prior probability before report evidence: `p0 = 3 / 43 = 0.0698`.
- Prior odds: `O0 = 3 / 40 = 0.075`.
- Logistic intercept equivalent: `logit(p0) ≈ -2.59`.

If the actual number of submitted reports differs on a date, use `3 / actual_submissions` for that day's base rate. Never assume all 43 submitted when contrary data is supplied.

## Evidence update

For a simple auditable model:

`posterior odds = prior odds × BF1 × BF2 × ... × BFk`

`posterior probability = posterior odds / (1 + posterior odds)`

Estimate each Bayes factor from labeled historical reports by comparing how often a feature appears among winners versus non-winners from comparable daily pools. Useful features include landed outcome, quantified evidence, verification, problem closure, pending-state share, projected-value-only language, avoidable length, and role family.

Do not invent Bayes factors. Do not multiply highly overlapping features as though they were independent; use a Bayesian logistic model when sufficient data exists.

## Provisional executable model

Until full same-day candidate sets are available, use `scripts/bayesian_selection.py`. It centers the intercept on the confirmed quota base rate and assigns uncertain expert priors to selection-rule features. It uses deterministic Monte Carlo sampling and therefore returns a reproducible point estimate and 80% credible interval.

Input feature values range from 0 to 1:

- `landed_outcome`: strength of a result completed and usable today.
- `quantified_evidence`: strength of meaningful quantities or audit evidence.
- `verified_operation`: extent of testing, reconciliation, or operating verification.
- `closed_loop`: completeness of problem → action → verification.
- `completed_fallback`: strength of an implemented risk fallback.
- `measured_funnel`: completeness of planned → actual → outcome channel data.
- `live_use`: evidence that a tool or process is actually in use.
- `pending_share`: share of the report whose claimed results remain pending.
- `projected_value_share`: share of value statements that are future expectations only.
- `verbosity_violation`: degree of conflict with the confirmed short-report requirement.
- `core_overstatement`: degree to which a summary upgrades intermediate work.
- `routine_volume_only`: extent to which counts represent routine throughput without exceptional outcome, efficiency, accuracy, or closure.
- `diffuse_task_list`: extent to which many unrelated items lack one dominant result.
- `unresolved_diagnosis`: extent to which problems are identified or escalated but not corrected, mitigated, or verified.
- `duplicated_content`: degree of repeated report content, especially full-paragraph duplication.

Example input:

```json
{
  "actual_submissions": 43,
  "quota": 3,
  "features": {
    "landed_outcome": 0.8,
    "quantified_evidence": 0.7,
    "pending_share": 0.2,
    "verbosity_violation": 0.0
  }
}
```

Run with `python scripts/bayesian_selection.py --input input.json`. Unspecified features default to zero. Feature assignments must be justified from the report and shown to the user when they materially affect the result.

The current coefficients are prior assumptions informed by confirmed rules and the small labeled set; they are not learned stable effects. Replace them with posterior coefficients after sufficient full-pool data is collected.

## Preferred calibrated model

With enough labeled data, use hierarchical Bayesian logistic regression:

`logit(p_i) = alpha_day + alpha_role + beta · x_i`

- Center the overall intercept near `-2.59`, reflecting the confirmed 3-of-43 quota.
- Use regularizing zero-centered priors for feature coefficients so small samples do not create extreme effects.
- Include a date effect because each day's comparison pool differs.
- Include a role effect to avoid favoring functions with naturally larger activity counts.
- Train daily and weekly selection separately. Do not use the daily 3-of-43 prior for weekly reports unless the weekly quota and eligible pool are confirmed.

Because exactly three winners are chosen from the same pool, probabilities are competitive and not independent. When full same-day candidate sets become available, prefer a within-day ranking or conditional-choice model and normalize the expected winner count to approximately three.

## Minimum data record

For every candidate report, retain: date, daily/weekly type, role family, selected 0/1, actual candidate count, quota, length, landed outcome, quantified evidence, verification, problem closure, pending-state share, projected-value-only language, and any confirmed rule violations.

Positive examples alone cannot estimate selection probability. Collect non-winners from the same dates, ideally the full pool.

If company-wide non-winners cannot be obtained, use [partial-observation-model.md](partial-observation-model.md). Published winners estimate the winner profile; the user's own repeated outcomes calibrate the user's absolute probability; same-day winner-versus-user comparisons estimate relative rule match. Preserve the resulting user-specific scope and wider uncertainty.

## Output rules

- Always output the model's numeric point estimate when probability is requested.
- Also report its 80% credible interval, base rate, actual-submission assumption, confidence, and strongest positive and negative factors.
- Before empirical calibration, label the number `provisional-bayes-v0.2 / low confidence`. “Accurate” means reproducible under stated inputs, not guaranteed to equal the administrator's unknown decision probability.
- Once an empirical model is fitted, report its posterior mean and credible interval and replace the provisional coefficient priors.
- Keep quality score and selection probability side by side. Explain disagreements, such as `quality 88/100 but probability below baseline because the report violates the confirmed length preference and lacks the day's favored selection pattern`.
- Validate on later dates, not random rows from the same dates. Track calibration and Brier score.
- Clearly state that selection still depends on the competing reports and administrator judgment.

## Two-layer presentation

Always present the same calculation twice for different audiences.

### Core result for non-specialists

Keep this first and brief:

```text
日报质量：82/100
预计入选概率：12.46%
基础入选率：6.98%，当前高于基础水平
核心判断：有真实落地结果，但部分事项仍待审批。
```

Do not include credible-interval terminology, odds, coefficients, Bayes factors, or model mechanics in this layer.

### Professional result for the user

Show:

```text
模型：provisional-bayes-v0.2
候选池/名额：43/3
先验概率：6.98%
先验赔率：3:40
后验点估计：12.46%
80%可信区间：7.20%–19.85%
置信度：低
主要正向特征：...
主要负向特征：...
特征输入：...
```

Add one sentence: `80%可信区间描述模型对真实概率范围的不确定性，不表示有80%的入选机会。`

The headline probability in the core layer must equal the posterior point estimate in the professional layer. Use identical rounding. If the model is provisional, never omit the low-confidence label from the professional layer.
