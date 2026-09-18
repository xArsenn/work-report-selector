# Theme-based selection regime

Use this reference for reports dated on or after 2026-09-17 or whenever leadership announces a named award theme.

## Confirmed regime boundary

Leadership completely changed the selection rule effective with the 2026-09-17 winner set. The official announcement named `方法论沉淀奖` as that week's theme and supplied three winners plus explicit reasons. Freeze all earlier selection rules and probabilities as legacy evidence; do not use them as the current decision boundary.

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

Do not require a file or script when the reusable output is a genuine decision principle. Conversely, do not reward a generic sentence such as `以后加强复盘` or `形成方法论` without the method itself.

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

The post-change model is provisional and has very-low confidence because only one complete winner set and no full non-winner pool have been observed. Keep the quota prior visible and never carry a legacy posterior into the new regime.
