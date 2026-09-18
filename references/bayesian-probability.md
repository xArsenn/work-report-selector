# Bayesian probability model

Use this reference when the user asks for selection probability, Bayesian updating, or probability calibration.

## Separation from quality score

The 100-point rubric evaluates whether the report is well written. This model evaluates whether it is likely to be selected under the administrator's rules and fixed quota. Keep both outputs. Never convert points into probability, define a score-to-probability lookup table, or assume that a higher-quality report necessarily has higher selection probability.

Build probability from selection outcomes and rule features: confirmed constraints, patterns separating winners from non-winners, role, date, candidate pool, and quota. A quality dimension may be included only as a separately measured feature if historical data proves predictive value; never use the total score as the target or shortcut.

## Confirmed base rate

- Default daily candidate pool: 43; daily winners: 3.
- Default weekly candidate pool: 43; weekly winners: 3.
- The user has confirmed these defaults apply unless a changed pool or quota is supplied.
- Exchangeable prior probability before report evidence for either type: `p0 = 3 / 43 = 0.0698`.
- Prior odds: `O0 = 3 / 40 = 0.075`.
- Logistic intercept equivalent: `logit(p0) ≈ -2.59`.

If the actual pool or quota differs for a period, use `actual quota / actual candidates` for that period's base rate. Daily and weekly models share the default prior but must retain separate feature calibration and outcome ledgers.

## Evidence update

For a simple auditable model:

`posterior odds = prior odds × BF1 × BF2 × ... × BFk`

`posterior probability = posterior odds / (1 + posterior odds)`

Estimate each Bayes factor from labeled historical reports by comparing how often a feature appears among winners versus non-winners from comparable daily pools. Useful features include landed outcome, quantified evidence, verification, problem closure, pending-state share, projected-value-only language, avoidable length, and role family.

Do not invent Bayes factors. Do not multiply highly overlapping features as though they were independent; use a Bayesian logistic model when sufficient data exists.

## Provisional executable model

Until full same-day candidate sets are available, use `scripts/bayesian_selection.py`. It centers the intercept on the confirmed quota base rate and assigns uncertain expert priors to selection-rule features. It uses deterministic Monte Carlo sampling and therefore returns a reproducible point estimate and 80% credible interval.

Input feature values range from 0 to 1:

- `landed_outcome`: strength of a result completed and usable today. A clearly verified user-visible or process before/after change can qualify even without a large numeric metric.
- `quantified_evidence`: strength of meaningful quantities or audit evidence.
- `verified_operation`: extent of testing, reconciliation, or operating verification. A scoped control check that finds no anomaly is valid verification when the checked population and result are explicit. Direct observation that an identified broken or limited behavior now works in a named scenario also counts.
- `closed_loop`: completeness of problem → action → verification.
- `completed_fallback`: strength of an implemented risk fallback.
- `measured_funnel`: completeness of planned → actual → outcome channel data.
- `live_use`: evidence that a tool or process is actually in use.
- `pending_share`: share of the report whose claimed results remain pending.
- `projected_value_share`: share of value statements that are future expectations only.
- `verbosity_violation`: degree of conflict with the confirmed short-report requirement.
- `core_overstatement`: degree to which a summary upgrades intermediate work.
- `routine_volume_only`: extent to which counts represent routine throughput without exceptional outcome, efficiency, accuracy, or closure.
- `diffuse_task_list`: extent to which many unrelated items lack one dominant result. Multiple defects or sub-deliverables within one named project are not diffuse merely because they appear as separate numbered items.
- `unresolved_diagnosis`: extent to which problems are identified or escalated but not corrected, mitigated, or verified.
- `duplicated_content`: degree of repeated report content, especially full-paragraph duplication.
- `dominant_outcome`: strength of one central result that compresses the day and clearly outranks routine supporting work.
- `thin_completion_evidence`: extent to which completed administrative outputs lack scale, reconciliation, acceptance, decision use, live operation, or a resolved exception.

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

Two regimes are available. `legacy-bayes-v0.7` preserves the pre-2026-09-17 model for historical reports. `provisional-theme-bayes-v1.0` starts a new model after leadership's rule reset and adds theme-alignment features. It has very-low confidence because only one complete post-change winner set is available. Never blend a legacy posterior into the theme regime.

Assign evidence features conservatively:

- A deliverable marked complete but lacking scale, reconciliation, acceptance, use, or effect should not receive strong `quantified_evidence`, `verified_operation`, `closed_loop`, or `live_use` values merely because it has a date or named object.
- `landed_outcome` measures usable result state; `dominant_outcome` measures whether one result is distinctive enough to organize the day. They are related but not interchangeable.
- Use `thin_completion_evidence` when completion is real but the report does not expose why it mattered or how it was checked. Do not relabel completed work as pending.
- Assign `verified_operation` from the scope and result of a check, not only from defects found. `约50人、10家公司、复核暂无差异` is stronger evidence than an unscoped claim such as `检查无误`.
- Assign `verified_operation` when a named broken or limited behavior is shown to work after the change in a specific scenario, even if no test count is available. Do not award it for generic claims such as `体验已优化`.
- Assign `diffuse_task_list` by project and outcome coherence. Four fixes to one product can form one dominant outcome; four unrelated administrative errands usually cannot.
- For daily reports, role-level value coherence also matters. Several finance items across accounting, invoicing, and cash control may receive low `diffuse_task_list` when one verified result anchors the day and every item has a precise state. Do not extend this exception to an unstructured list of routine errands.
- A tested fix may remain strong while deployment is pending when the report clearly distinguishes `测试通过` from `已上线`. Do not treat pending deployment as live use.
- When one result is closed and verified but another item is only partly tested, score each item separately. The closed result may support `dominant_outcome`; it does not erase `pending_share` or convert the partial item into `landed_outcome`.
- Assign `verified_operation` strongly for an end-to-end workflow checked through actual operation when the scope and observed result are explicit.
- Assign `landed_outcome` to the exact confirmed finance node. A 39,000-yuan transfer to a named account for loan repayment is a landed transfer; it is not a completed loan repayment unless deduction or settlement is confirmed.
- Do not use department, AI vocabulary, or a recurring winner's identity as a positive input.

For weekly reports, apply these additional assignment rules:

- Set `report_type` to `weekly` in the script input. Use `daily` for daily reports; omission defaults to `daily` for backward compatibility.
- Give strong `landed_outcome` only when the central weekly project reached actual use, payment, acceptance, reconciliation, production operation, or a decision-ready state within the reporting cutoff.
- Give strong `live_use` only when the report shows real operating behavior. Publication plus testing, an MVP awaiting integration, funds prepared for a later payment, or a quote awaiting signature is not strong live use.
- Give strong `dominant_outcome` only when one project or at most two connected pillars organize the week's evidence. A list of unrelated policies, reports, payments, limits, negotiations, and reconciliations remains diffuse even when individually complete.
- Assign `pending_share` by the importance of unfinished nodes, not by item count. If the central automation, payment, contract, or reconciliation is pending, its weight is large.
- Never use results completed after the weekly cutoff to raise prior-week features. Preserve the original prediction and record the later result in the next reporting period.

For theme-regime reports, read [theme-based-selection.md](theme-based-selection.md), set `rule_regime` to `theme`, and provide the official `selection_theme`. Theme features measure rule match; ordinary result features remain supporting evidence. A missing current theme prevents a confident selection estimate.

## Preferred calibrated model

With enough labeled data, use hierarchical Bayesian logistic regression:

`logit(p_i) = alpha_day + alpha_role + beta · x_i`

- Center the overall intercept near `-2.59`, reflecting the confirmed 3-of-43 quota.
- Use regularizing zero-centered priors for feature coefficients so small samples do not create extreme effects.
- Include a date effect because each day's comparison pool differs.
- Include a role effect to avoid favoring functions with naturally larger activity counts.
- Account for repeated reports from the same person with a reporter-level random effect or equivalent cluster shrinkage. This controls correlation; do not use reporter identity itself as a favorable feature when estimating another employee's probability.
- Train daily and weekly selection separately. Both currently use the confirmed 3-of-43 default prior, but their feature effects and outcome histories must not be pooled blindly.

Because exactly three winners are chosen from the same pool, probabilities are competitive and not independent. When full same-day candidate sets become available, prefer a within-day ranking or conditional-choice model and normalize the expected winner count to approximately three.

## Minimum data record

For every candidate report, retain: date, daily/weekly type, role family, selected 0/1, actual candidate count, quota, length, landed outcome, quantified evidence, verification, problem closure, pending-state share, projected-value-only language, and any confirmed rule violations.

Positive examples alone cannot estimate selection probability. Collect non-winners from the same dates, ideally the full pool.

If company-wide non-winners cannot be obtained, use [partial-observation-model.md](partial-observation-model.md). Published winners estimate the winner profile; the user's own repeated outcomes calibrate the user's absolute probability; same-day winner-versus-user comparisons estimate relative rule match. Preserve the resulting user-specific scope and wider uncertainty.

## Output rules

- Always output the model's numeric point estimate when probability is requested.
- Also report its 80% credible interval, base rate, actual-submission assumption, confidence, and strongest positive and negative factors.
- For legacy reports, label the number `legacy-bayes-v0.7 / low confidence`. For post-change reports, label it `provisional-theme-bayes-v1.0 / very-low confidence`. “Accurate” means reproducible under stated inputs, not guaranteed to equal the administrator's unknown decision probability.
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
模型：provisional-theme-bayes-v1.0
规则版本：theme
评选主题：方法论沉淀奖
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
