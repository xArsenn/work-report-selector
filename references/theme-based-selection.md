# Theme-based selection regime

Use this reference for reports dated on or after 2026-09-17 or whenever leadership announces a named award theme.

## Confirmed regime boundary

Leadership completely changed the selection rule effective with the 2026-09-17 winner set. The official announcements for 2026-09-17 and 2026-09-18 both named `方法论沉淀奖` and supplied explicit winner reasons. The 2026-09-19 winner set continued within the same confirmed theme week and selected three reports that exposed concrete reusable methods. Freeze all earlier selection rules and probabilities as legacy evidence; do not use them as the current decision boundary.

`本周评选主题` confirms the theme for that week. It suggests that themes may rotate, but rotation is not yet confirmed. Always prefer the latest official theme. If the current theme is unavailable, ask for it and avoid a confident probability estimate.

## Selection order

Apply the new regime in this order:

1. **Theme gate:** does the report contain evidence directly relevant to the announced theme?
2. **Substance:** did real work, problem solving, or delivery occur?
3. **Proof:** was the method or result tested, used, compared, or otherwise verified?
4. **Transferability:** can the learning be reused by the author, team, or another case?
5. **Status precision:** are unfinished implementation and validation states preserved?

A strong operational result can fail the theme gate. A polished reflection can also fail when it merely renames ordinary work as a methodology without a real rule, artifact, mechanism, or validated learning.

## Current confirmed theme: 方法论沉淀奖

The strongest chain is:

`real problem or repeated task → cause/pattern → extracted method → validation → reusable scope or artifact`

Positive evidence includes:

- a rule, decision standard, cold-start logic, classification, or diagnostic sequence;
- an SOP, checklist, template, deployment script, monitoring rule, fallback, recovery mechanism, or anti-duplication control;
- a principle derived from a real failure and tied to a future operating decision;
- proof through real data, production use, regression tests, simulation, or repeated cases;
- a stated reuse audience or scenario.
- a named framework, standard, positioning model, evaluation method, or decision structure delivered as documents or review materials;
- management or stakeholder confirmation that the framework clarified a direction, relationship, division of responsibility, or implementation boundary.
- a cross-functional issue converted into an adopted owner, rule, AI tool, or durable company mechanism rather than merely handed off to another department.

Do not require a file or script when the reusable output is a genuine decision principle. Conversely, do not reward a generic sentence such as `以后加强复盘` or `形成方法论` without the method itself.

Deployment is not a universal gate for this theme. A concrete framework, standard proposal, evaluation method, or risk rule can pass when it is already documented and specific enough to guide later work, even if implementation remains pending. Preserve the status precisely: `方案已整理，待开发` is not `已上线`, but the documented method may still be a completed artifact.

Evidence strength for the current theme:

1. **Strongest:** named reusable method or artifact, real use or test, and a stated reuse scope.
2. **Competitive:** named framework, standard, checklist, or decision rule completed and reviewed or tied to a concrete problem, with implementation honestly pending.
3. **Weak:** ordinary work followed by a generic reflection or a promise to form a method later.

The 2026-09-18 set confirms four recurring method forms: a strategic framework, an operational mechanism or practice checklist, a task-decomposition or system-risk rule, and a standard display or evaluation scheme. Judge specificity and reuse value rather than requiring the same artifact type across roles.

The 2026-09-19 set adds three useful anchors: `规则对齐 → 存量保护 → 分批开发 → 数据验收` for controlled implementation; `核心不动、只换适配层` plus `旧版残留先清再合` for migration and conflict handling; and `自动登录 → 自动开票 → 发票汇总 → 邮件批量发送` for finance automation. Large metrics strengthen validation but are not mandatory when the artifact, stages, and reuse scope are explicit. Do not give maximum validation merely because a workflow is well named; distinguish tool completion from repeated real-operation proof.

The 2026-09-20 published winners add a same-day comparison: completed and tested settlement/invoicing flows, a validated question-order gate and fallback rule, and measured messaging/follow-up/monitoring outputs. A finance draft from that date contained a confirmed system-integration plan, assigned developers, a drafted service agreement, and completed funding transfers, but integration development and validation were still future steps. Treat `明确问题 → 确定方案 → 落实责任人` as useful coordination, not by itself a task-specific operating method or proof that automated invoicing worked through the new integration. The published notice did not include official selection reasons; this separator is an inference, not a confirmed gate. Do not infer that every winning report needs large test counts: direct finance operation, reconciled output, stakeholder acceptance, or a documented decision rule can also validate a method.

### Role-normalized examples

- **Finance:** unified tax or accounting definitions, reconciliation checklist, closing template, exception-routing rule, invoice-control SOP, or automation configuration guide.
- **HR/administration:** onboarding checklist, review standard, payroll exception rule, or cross-department handoff protocol.
- **Product/engineering:** development principle from user evidence, regression set, deployment script, failure-recovery mechanism, monitoring rule, or reusable architecture decision.
- **Growth/operations:** cold-start rule, channel decision logic, distribution diagnosis, experiment protocol, or repeatable acquisition workflow.
- **Legal:** clause standard, review checklist, case-response playbook, or risk-triage rule.

## Fact-preserving rewrite pattern

Use only when the source supports every link:

```text
今日成果：完成【真实工作/问题处理】，结果为【交付或状态】。
方法沉淀：基于【问题/重复场景】总结【具体规则、步骤、模板或机制】，经【数据、测试、实操或案例】验证，后续可用于【复用范围】。
```

If the method has not been formed, say `正在记录原因与排查步骤，待问题解决后沉淀配置清单`; do not present an intention as a completed methodology.

## Probability handling

Use `rule_regime: "theme"` and supply `selection_theme` to `scripts/bayesian_selection.py`. For the methodology theme, justify these features separately from ordinary result features:

- `theme_alignment`: direct fit to the official theme;
- `reusable_method`: specificity and usefulness of the extracted method;
- `method_validation`: evidence that the method works;
- `transferability`: clarity of future users or scenarios;
- `method_artifact`: strength of a concrete script, SOP, template, checklist, mechanism, or explicit principle;
- `one_off_result_only`: strong result with little theme-relevant learning;
- `unsupported_method_claim`: methodology language without supporting content.

The post-change model is provisional and has very-low confidence because only three complete winner sets and no full non-winner pool have been observed. Keep the quota prior visible, use the actual four-winner quota for 2026-09-18 only, and never carry a legacy posterior into the new regime.
