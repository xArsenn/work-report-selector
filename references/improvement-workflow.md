# Single-report diagnosis and improvement workflow

Use this reference whenever the user supplies one report and asks to 修改、优化、完善、润色、提高入选概率 or identify what is missing.

## 1. Build a fact ledger

Before rewriting, separate the source into:

- **Completed facts:** actions whose completion is explicit.
- **Metrics:** counts, amounts, ratios, time, quality, conversion, and before/after values.
- **Business effects:** effects explicitly stated or directly entailed by the facts.
- **Pending states:** in progress, submitted, awaiting acceptance, planned, blocked, or unverified.
- **Missing evidence:** useful facts that are not supplied.

Use the ledger internally. Do not overwhelm the user with it unless inconsistencies need resolution.

## 2. Diagnose by value chain

For every major item, test this chain:

`目标/问题 → 动作 → 产出 → 结果 → 经营价值 → 验证状态 → 下一步`

The report does not need every field for every item. Identify the one or two broken links that most limit its credibility or selection score.

Examples of targeted prompts:

- “这项优化前后分别耗时多少？是否已在生产环境验证？”
- “回款金额和到账状态是什么？如不便公开，可写区间或‘已到账’。”
- “230篇中通过质检、发布或带来有效线索的数量是多少？”
- “案件推进到了提交、受理还是开庭确认？下一节点和日期是什么？”

Ask or suggest no more than three items at once. Prioritize facts that change result closure, business value, or verifiability. Do not ask for numbers merely to decorate the report.

## 3. Forecast and choose robust edits

Read [rule-change-forecast.md](rule-change-forecast.md). Predict only directions relevant to the supplied report, then select edits that remain beneficial under both the current rubric and high-confidence forecast scenarios.

Examples:

- If volume inflation is likely to be tightened, connect production counts to quality, acceptance, use, or downstream results when those facts exist.
- If strategic alignment may gain weight, state the supported connection to a company priority without inventing leadership endorsement.
- If status verification may become a gate, preserve precise states and put verification next to the claimed result.
- If role normalization may increase, explain value relative to the employee's actual responsibilities instead of comparing raw totals across roles.

Do not optimize the rewrite around a low-confidence prediction when doing so makes it longer, less natural, or less truthful.

## 4. Produce two evidence levels only when useful

Always provide a **conservative revision** that uses only confirmed source facts and is ready to copy.

If missing facts materially limit the report, optionally add an **enhancement skeleton** using explicit placeholders. Never mix placeholders into the copy-ready version unless the user requests a fill-in template.

Preserve:

- Names, dates, quantities, scope, and causal claims exactly unless only formatting is changed.
- Distinctions among completed, launched, submitted, tested, partially completed, and planned.
- Honest target variance, including missed goals and unresolved blockers.

Improve:

- Lead with the day's most valuable completed outcome.
- Group minor actions under the outcome they support.
- Replace activity language with precise result language only when the source supports it.
- Put evidence next to the claim it proves.
- Connect outcomes to business value without unsupported monetary conversion.
- End with a concrete next action when one exists.
- Remove repetition, generic self-praise, and empty phrases.
- Remove unsupported decorative adverbials and modifiers. Prefer “完成27笔单据审核” over “高效完成27笔单据审核”, and “整理平台做账资料” over “有序整理平台全部做账资料”. Retain words such as “再次”“部分”“目前”“预计” when they accurately express sequence, scope, status, or uncertainty.

## 5. Score before and after

Use the daily rubric for daily reports and the weekly rubric for weekly reports. The revised score may rise for clearer structure and better use of existing evidence, but do not award points for placeholder content or unsupplied facts.

For weekly reports, additionally test whether the rewrite:

- Leads with one weekly core or the two most important outcome pillars.
- Aggregates repeated daily activity into cumulative scope or measurable change.
- Separates completed outcomes from validation, pending risks, and next-week continuation.
- Preserves reusable assets such as SOPs, regression sets, comparison tables, monitoring, fallback paths, automation, or documented protocols.

Explain score movement in two buckets:

- **Presentation gain:** existing facts became clearer, more concise, or easier to verify.
- **Substance still missing:** evidence the employee must truthfully supply before the substantive score can increase.

Avoid false precision. Scores are diagnostic estimates, not guarantees of selection.

After the current-rubric score, add a qualitative forecast stress-test:

- **Robust:** likely to remain strong under the high-confidence changes.
- **Sensitive:** one forecast change could materially weaken it; name the missing evidence.
- **Fragile:** depends heavily on wording, raw volume, or an unverified claim likely to be tightened.

Do not invent numerical future weights or a future score unless the user supplies a proposed rule set.

## 6. Recommended response shape

1. Verdict and original score.
2. Strongest point and up to three priority gaps.
3. Up to three relevant forecast directions with confidence and evidence.
4. Targeted completion prompts.
5. Copy-ready conservative revision.
6. Revised score, forecast stress-test, and what changed.
7. Optional enhancement skeleton only when missing facts are pivotal.

Keep advice specific to the supplied report. Do not return a generic daily-report lecture.
