# Comprehensive daily-report template

Use this reference when the user asks for a 日报模板 or when a daily-report rewrite needs a completeness check. The template is an evidence-collection framework, not a mandatory company form. Preserve the shortest submitted version that still carries the decisive evidence.

For reports in the post-2026-09-17 theme regime, also read [theme-based-selection.md](theme-based-selection.md). Add a theme section only when supported by real facts; never manufacture a methodology to match the award.

## Two-stage method

1. Build the complete fact sheet internally: object, scope, action, result, verification, value, status, and next node.
2. Submit only the fields that contain real information. Group related subproblems under one project and remove repeated summaries, generic value claims, and empty sections.

## Copy-ready adaptable template

```text
日报（YYYY.MM.DD）｜姓名

今日核心：完成【核心对象】从【原状态/问题】到【当前结果】，通过【测试、核对、数据或验收】确认【结果】；【关键未完节点】待【时间或条件】完成。

一、今日完成

1. 【核心成果】
针对【目标/问题】，完成【动作或交付物】，覆盖【人数、金额、主体、门店、项目或数据范围】；经【测试/核对/验收】确认【结果】，当前状态为【已发布/已上线/已提交/待部署】，下一节点为【具体行动；没有则删除】。

2. 【问题解决或风险控制】
发现【问题/风险】，定位原因为【已确认根因】；通过【解决动作】完成处理，经【验证方式】确认【修复结果/暂无异常/风险已控制】。

3. 【业务、成本或效率成果】
完成【事项】，实现【到账、降费、额度增加、时间缩短、步骤减少、数据修正或风险控制结果】；未闭环部分为【准确状态】，预计【时间/条件】进入【下一节点】。

4. 【其他成果；可选】
完成【事项】，涉及【范围/数量】，结果为【可验证状态】。

二、问题与风险（没有独立决策价值则删除）

【问题/风险】：目前【准确状态】，影响【对象/范围】；已采取【临时措施/解决方案】，待【负责人、时间或外部条件】完成闭环。

三、反思与改进（没有实质内容则删除）

今日发现【具体方法、流程或判断问题】；后续通过【可执行措施】验证效果或避免重复发生。

四、下一步计划（正文已有明确下一节点时可删除）

1. 【对象】：完成【具体动作】，以【发布、到账、验收、数据一致或测试通过】为完成标准。
2. 【对象】：解决【具体问题】，预计【日期/条件】形成【交付结果】。
3. 【对象】：跟进【待办事项】，确认【金额、审批、上线状态或下一节点】。
```

## Result-pattern library

Choose the pattern that fits the evidence; do not force every item into the same sentence.

### Delivery

`完成【交付物】，覆盖【范围/数量】，经【验证】确认【结果】，已【发布/交付/上线】。`

### Problem closure

`发现【问题】，定位根因为【原因】，通过【动作】完成修复，经【测试/核对】确认【结果】。`

### Control and risk

`完成【明确范围】核查，结果为【无差异/发现X项异常】；已采取【措施】，控制【具体风险】。`

A no-anomaly result is meaningful only when the checked scope and method are explicit.

### Observable before/after behavior

`原来【旧行为/限制】，现已【新行为/能力】；经【场景/范围】验证【可观察结果】，尚待【未测场景；没有则删除】。`

Use this when large metrics are unavailable but a user, system, or process behavior changed visibly. `体验优化` is not enough; name what could not be done before and what now works.

### Partial progress

`目标为【目标值】，目前完成【实际值/比例】；差距为【差额】，原因是【已确认原因】，预计【时间】完成下一节点。`

### Methodology-theme evidence

`基于【真实问题/重复场景】，形成【具体规则、SOP、模板、脚本、检查清单或原则】，经【数据/实操/测试/案例】验证，可复用于【对象或场景】。`

If the method is still being formed, preserve that state: `已记录【原因/排查步骤】，待问题解决并验证后沉淀为【清单/SOP】。`

A completed method artifact may also be a positioning framework, standard display scheme, evaluation method, requirement-decomposition structure, or configuration-consistency rule. When implementation is pending, write both states: `已完成【框架/标准/规则】并经【会议/评审/分析】确认，后续按该方法推进【开发/配置/应用】。` Do not upgrade the later implementation to completion.

## Evidence checklist

For each major item, retain the strongest available fields:

- **Object:** the named thing handled.
- **Scope:** people, amount, entities, stores, cases, records, or coverage.
- **Result:** the outcome produced today.
- **Verification:** test, reconciliation, acceptance, live data, or scoped no-anomaly check.
- **Status:** completed, tested, published, submitted, pending deployment, or awaiting approval.
- **Value:** revenue, cash, cost, efficiency, accuracy, compliance, or risk control.
- **Next node:** owner, date or acceptance condition for unfinished work.

Normally one item needs only the three to five fields that materially prove it. Do not lengthen a report to fill empty fields.

## Role-specific evidence

- **Finance:** amount, entity count, reconciliation differences, corrected accounts, cash status, tax conclusion, cost saving, or control coverage.
- **HR and administration:** headcount, entity count, review result, employee questions, approval node, document count, or omission prevention.
- **Product and engineering:** user-visible defect, root cause, fix, test count, release state, failure disclosure, or deployment dependency.
- **Operations and growth:** planned volume, actual volume, completion rate, leads, conversion, cost, collection, or corrective action.
- **Legal:** contract count, case state, submission or acceptance, risk point, mitigation, or next legal node.

## Compression and status rules

- Lead with one dominant outcome. A second clause may name the most important pending dependency.
- Group multiple defects or deliverables under one named project when they serve the same outcome. Item count alone does not create diffusion.
- A tested fix may still say `待部署`; this honest state can remain competitive. Never upgrade it to `已上线`.
- A scoped check with `暂无差异` is a verified result; an unscoped `检查无误` is weak.
- A directly observed behavior change can be verification without a large metric when the old limitation, new behavior, and tested scenario are explicit.
- An end-to-end workflow checked through actual operation can be verification when the report names the process and observed result; prefer this over a generic `核对无问题`.
- One verified core can support several clearly bounded next-stage items. Not every item must close on the same day.
- Several items can remain concise and competitive when they form one role-coherent value path, such as finance cash control plus invoicing and accounting accuracy. Group by value path and keep one dominant verified result.
- A completed transfer is a landed transfer, not automatically a completed repayment. Preserve the exact node unless receipt, deduction, acceptance, or settlement is confirmed.
- One fully closed sub-result may anchor another partially tested item, but every remaining test, deployment, approval, or submission state must stay visible.
- Mention future strategic value only as support for a same-day delivered result; never use it in place of present evidence.
- Reflection and next-day plans are optional. Remove them when they repeat the body or add no decision value.
- Remove decorative modifiers such as `高效、积极、有序、全面推进` unless a supported comparison gives them meaning.
- Keep the submitted report as short as the evidence permits. No exact character cap is confirmed.
