# Prodiges Accelerator Skills

**Version 1.0.0 · Installation guidance checked 21 November 2026**

Four reusable skills help founders turn their startup context into customer research, competitive positioning, an offer and pricing experiment, and a practical launch plan. Each skill works independently and can respond in English or French. The pack contains methodology and templates; founders supply their own startup evidence.

**Extract the complete bundle first. For a platform's single-skill upload, choose one ZIP from `claude-zips/` or `gemini-zips/`, then repeat for the other skills.** The complete bundle is a distribution archive, not one installable skill. The two ZIP layouts contain the same skill resources, arranged for each platform's importer.

## 1. Choose a skill

| Skill | Use it to produce | Useful input |
| --- | --- | --- |
| `prodiges-customer-discovery` | Initial customer choice, user/buyer map, interview plan or evidence synthesis, and the next validation experiment | Startup brief, interview notes, current customer workflow |
| `prodiges-competition-positioning` | Alternatives matrix, comparable pricing, switching analysis, positioning hypothesis, and claims that need proof | Target customer, market, competitors, supplied sources or browsing access |
| `prodiges-offer-pricing` | Offer card, charging model, pricing scenarios, delivery economics, and a bounded price test | Customer evidence, offer constraints, costs, usage assumptions |
| `prodiges-startup-review` | Tailored launch backlog, weekly review, readiness assessment, and next three actions | Current stage, task updates, deliverables, metrics, mentor decisions |

The review skill includes **60 launch task templates** covering customer discovery, competition, offer, pricing, product delivery, operations, billing, website messaging, acquisition, LinkedIn where relevant, launch, and learning. It selects work appropriate to the startup's stage instead of requiring every founder to complete all tasks in order.

## 2. What is in the bundle

- `skills/`: four complete skill folders, each containing `SKILL.md` and its supporting resources.
- `claude-zips/`: four separate ZIPs, each with one named skill folder containing `SKILL.md`.
- `gemini-zips/`: four separate ZIPs, each with `SKILL.md` directly at the archive root.
- `templates/startup-brief.template.yaml`: an optional input template. Ordinary text is equally acceptable.
- `gemini-legacy/`: instructions and flattened knowledge guides for accounts that still use Gems.
- `VALIDATION.md`: completed checks and practical limits.
- `manifest.json`: release information and file hashes.

Each skill includes its own evidence rules, output template, startup brief, and structured report schema. There are no mandatory cross-skill dependencies. The pricing skill also includes an offline Python calculator and fictional input examples.

## 3. Install in Claude Desktop or Claude

1. Open **Customize → Skills**.
2. Choose **+ → Create skill → Upload a skill**.
3. Upload a ZIP from `claude-zips/`, such as `prodiges-customer-discovery.zip`.
4. Enable it, then repeat for the remaining skills you want.

Enable code execution and file creation where required by your account. Each ZIP contains one folder whose name matches the skill, with `SKILL.md` inside it. Ask Claude to use the skill by name and provide the startup context. Interface availability can depend on your account and administrator settings.

Official instructions: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## 4. Install in Codex

Extract the complete bundle. Copy the four folders inside `skills/` into either:

- **User scope:** `~/.agents/skills/`, to make them available across projects.
- **Project scope:** `.agents/skills/` inside the project, to keep them with that project.

Preserve the folder structure. For example, the customer skill should be at `~/.agents/skills/prodiges-customer-discovery/SKILL.md`. Keep any existing unrelated skills. If a folder with the same name already exists, compare versions before replacing it.

Use Codex's skill picker or explicitly invoke a skill:

```text
$prodiges-customer-discovery
Use the startup brief below to recommend an initial customer segment,
prepare discovery interviews, and identify the next three actions.
Distinguish assumptions from evidence.
```

Check the available-skills list after installation. The optional `agents/openai.yaml` files provide Codex display metadata; the main workflow remains in `SKILL.md`.

Official instructions: [Build skills](https://learn.chatgpt.com/docs/build-skills).

## 5. Install in Gemini Apps

For an account with **Skills**, open **Customize → Skills → Create → Upload**. Select a ZIP from `gemini-zips/`, such as `prodiges-customer-discovery-gemini.zip`, review it, and create the skill. Repeat for the others. These ZIPs place `SKILL.md` directly at the archive root, as Google's transfer guide requires. You can also upload the complete named folder from `skills/`. Use `/` or the updated `@` picker to select a skill in chat.

The files in this pack use text, Markdown, YAML, JSON, Python, and small SVG icons. The calculator does not access the internet. Available browsing and execution capabilities still depend on the Gemini environment; uploading a script is not proof that it ran.

Google is transitioning Gems to Skills. Its published schedule starts with personal accounts for adults in November 2026, with work and school account transitions in 2027. If your account still shows Gems, follow `gemini-legacy/INSTRUCTIONS.txt` to create one Gem per skill using the matching instructions and knowledge guide.

Official instructions: [Create and manage skills](https://support.google.com/gemini/answer/17094296), [Transfer skills from other platforms](https://support.google.com/gemini/answer/18977944), and [Gems transition](https://support.google.com/gemini/answer/18560919).

## 6. Install in Gemini CLI

Gemini CLI recognizes skill folders in `~/.gemini/skills/` and the shared `~/.agents/skills/` location, as well as their project equivalents. If you already copied the pack to `.agents/skills/` for Codex, use that shared location rather than maintaining another copy unnecessarily.

Alternatively, from the extracted bundle directory, install each folder:

```sh
gemini skills install ./skills/prodiges-customer-discovery --scope user
gemini skills install ./skills/prodiges-competition-positioning --scope user
gemini skills install ./skills/prodiges-offer-pricing --scope user
gemini skills install ./skills/prodiges-startup-review --scope user
```

Use `/skills reload` in an existing session, then check `/skills list`. Request the relevant skill by name in your prompt.

Official instructions: [Gemini CLI agent skills](https://geminicli.com/docs/cli/skills/).

## 7. Start with one startup

Supply the startup's name or internal identifier, customer and geography, stage, product idea, current offer, available evidence, constraints, and the decision needed. Say which facts are uncertain. Use a separate conversation or project for each startup.

Start with the review skill if you need to decide what to work on:

```text
Use prodiges-startup-review for the startup described below.
Adapt the launch task library to our stage. Give me the next milestone,
the next three actions with owners and completion criteria, and the
evidence a mentor should review. Leave unknowns explicit.
```

For a founder who needs discovery in French:

```text
Utilise prodiges-customer-discovery et réponds en français.
Voici notre idée, les clients envisagés et les notes disponibles : [...].
Sépare les faits, les hypothèses et les contradictions. Propose un premier
segment, un guide d'entretien et trois prochaines actions vérifiables.
```

A useful progression is customer discovery, competition and positioning, offer and pricing, then review. Run research in parallel where appropriate. Pass the relevant reports and evidence to the next skill; the pack does not create automatic synchronization between applications.

For pricing, provide currency, tax basis, service period, customer count, expected usage, payment/refund assumptions, and full-period delivery costs. The supplied calculator examples are fictional demonstrations. Replace them with startup-specific inputs before drawing a commercial conclusion.

## 8. Use it across your accelerator

Give each founder the clean release ZIP and this guide. Keep the reusable skill files free of startup-specific customer lists, private interviews, account credentials, and mentor notes. Store those inputs and resulting reports in that startup's authorized workspace.

Ask founders to submit the recommendation, evidence ledger, uncertainties, and next actions with each milestone. Mentors can then review the evidence and record their actual decisions. A polished report does not establish customer demand, completed execution, or milestone acceptance.

For a later SaaS integration, each skill includes `assets/report.schema.json` and a shared output contract. Request structured JSON when you need a predictable handoff. The proposed schema covers evidence, recommendations, tasks, mentor review, and artifacts; it is not a connection to your accelerator SaaS. Your application will still need authenticated storage, validation, access controls, and an explicit workflow for accepting updates.

Publish future pack versions with a version identifier and a brief explanation of changes. Ask founders to keep their working reports outside installed skill folders so that updating the methodology does not overwrite their work.

## 9. What has and has not been verified

The four skill structures, resource links, metadata, report schemas, calculator, and representative responses have been checked. See `VALIDATION.md` for detail. They have **not been installed and exercised in your actual Claude, Codex, or Gemini accounts**. Models can interpret instructions differently, and available tools vary. Use the first real startup case to confirm the workflow and output quality in your chosen environment.

Current external claims need source verification. Without browsing, the skills work from supplied material and identify what remains unverified. They can propose experiments, draft tasks, and prepare decisions; the founders and mentors remain responsible for conducting the work and making business decisions.
