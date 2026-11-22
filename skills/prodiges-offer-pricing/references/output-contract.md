# Output and handoff contract

## Default human deliverable
Write a useful report in the user's language, with:
1. Startup and scope, source period, and current decision.
2. Main recommendation with reasoning and evidence IDs.
3. Skill-specific analysis and alternatives.
4. Evidence register and material assumptions.
5. Missing information, contradictory findings, and decisions for the founder or mentor.
6. Proposed next actions with owner, deliverable, dependencies, evidence required, and acceptance criteria.

Never report a proposed activity as completed. A report may be ready to review while its business hypotheses remain unvalidated. Put methodology limitations next to the claims they affect.

## Optional JSON output
When the user requests JSON, SaaS import, or a machine-readable handoff, also produce valid JSON using assets/report.schema.json. Omit Markdown fences in a saved .json file. Do not output comments, NaN, Infinity, invented timestamps, or invented source locations.
Use schema_version "1.0". Read the schema before generating or validating JSON. This is a portable proposed data contract, not an existing Prodiges API.
Use null for unknown identifiers, dates, or owners. Use empty arrays where there are no evidence records or tasks. Use a source file and a page/section/row locator for local evidence; use an actual URL for web evidence. Avoid inaccessible session-specific citation tokens in exported JSON.
Use the actual runtime date if available, otherwise null. Do not claim structural validation unless a parser/schema validator was run successfully.

Top-level fields:
- schema_version, skill_name, startup_id, generated_at, language, summary.
- recommendations: claim, rationale, evidence_ids, status (proposed/supported/needs_validation).
- evidence: id, type, claim, locator, source_date, observed_at, assessment, limitations.
- assumptions and open_questions: arrays of strings.
- next_tasks: id, title, owner, due_date, depends_on, deliverable, acceptance_criteria, evidence_required, status.
- mentor_review: status (not_requested/proposed/needs_review/human_accepted/changes_requested), questions, decision, reviewer, reviewed_at.
- artifacts: title, format, location; list only outputs actually created or supplied.

The strings generated_at, source_date, observed_at, due_date, and reviewed_at may contain ISO dates or timestamps; keep unknowns null. Human_accepted requires a recorded human review in the supplied evidence, with reviewer and reviewed_at populated. Otherwise use proposed or needs_review. Preserve supplied task IDs; new local task IDs can use T001, T002. Catalog-linked task IDs use L01 through L60.

## Quality check
Check that every evidence_ids entry resolves to an included record; every task dependency resolves to an included task or a named existing external task; the startup identity is consistent; supplied data is not silently replaced by assumptions; currencies and periods match; and human acceptance has not been inferred from AI approval.

