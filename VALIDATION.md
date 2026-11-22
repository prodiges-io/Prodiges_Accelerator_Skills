# Validation record

**Prodiges Accelerator Skills · v1.0.0 · 21 November 2026**

## Completed checks

| Area | Result |
| --- | --- |
| Skill packaging structure | All four source skills passed the official skill-creator `quick_validate.py` check. |
| Frontmatter and naming | Each skill has the required `name` and `description`; source folder names and skill names were checked. |
| Internal resources | Markdown resource references resolve within their skill package. No required resource depends on another skill. |
| Codex UI metadata | Display metadata and explicit invocation prompts were checked against each skill. |
| Structured reports | All four JSON Schemas passed Draft 2020-12 schema validation. This checks schema validity, not every future model-generated report. |
| Launch task library | The review skill contains all 60 task templates, with stable L01–L60 identifiers. |
| Pricing calculator | The author completed 26 arithmetic and input-validation checks. A separate run checked the command-line examples, seasonal purchases without MRR, full-refund behavior, and rejection of non-finite values. |
| Skill behavior | Three independent scenario trials exercised all four skills with fictional startup situations. Findings are summarized below. |

## Behavioral trials

**Customer discovery:** A scenario combined supportive friends, an end user's problem, an uncertain buyer, and a possible existing alternative. The response kept validation provisional, distinguished buying roles and independent accounts, and proposed concrete research instead of inventing interviews or paid commitments.

**Competition and positioning:** A scenario supplied an annual, per-seat price with a minimum purchase, an unsupported competing price, and a prospect's migration concern. The response normalized the known price correctly, left the unsupported price unverified, treated manual work as a meaningful alternative, and avoided claiming an untested feature advantage.

**Offer/pricing and startup review:** A seasonal-pass scenario included two unequal cohorts, four purchases without customer linkage, reported checklist progress, untested refunds, and a possible document-access issue. The response combined the cohort counts correctly at 4/25, kept purchase value distinct from MRR, did not infer paid conversion, recommended resolving material blockers, and left mentor acceptance unclaimed.

These are qualitative checks on representative prompts. They do not establish a model-wide success rate, platform certification, or business validity for a real startup.

## Practical limits

- No live installation or end-to-end run was performed in the recipient's Claude Desktop, Codex, Gemini Apps, or Gemini CLI account.
- Official installation documentation was checked on 21 November 2026. Menus, rollout status, account permissions, and host capabilities may change.
- The legacy Gemini knowledge guides are a text adaptation. They do not install native skills or add tool capabilities.
- The pricing calculator assumes the documented model, including complete refunds at the supplied rate and one explicit service period. It is not an accounting or tax engine.
- Reports and task proposals do not prove customer demand, software readiness, compliance, or human approval.
- No messages were sent to founders or customers, no production prices were changed, and no external launch or paid campaign was performed as part of preparing this release.

## Distribution archive checks

All eight single-skill archives passed ZIP integrity checks. Claude archives contain one named skill folder; Gemini archives put `SKILL.md` directly at the archive root. The archived bytes match the source skill files, with no absolute paths, traversal paths, duplicate entries, hidden files, Python caches, or nested archives. The complete distribution archive is checked after assembly.
