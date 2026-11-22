---
name: prodiges-offer-pricing
description: Design and review a startup's commercial offer, pricing model, packages, usage limits, and validation experiment using customer evidence and delivery costs. Use for SaaS pricing, founding customer offers, paid pilots, subscriptions, credits, seasonal passes, and one-time products in B2B or B2C. Produce explicit assumptions, reproducible scenarios, and mentor decisions; do not treat a pricing proposal as proven willingness to pay or change live prices.
---

# Prodiges Offer and Pricing

## Start with the brief and evidence

Read [evidence and working rules](references/evidence-and-working-rules.md). Reuse relevant supplied material and preserve the user's language, constraints, currencies, and established decisions. Use [the startup brief](assets/startup-brief.template.yaml) only to collect missing context; accept equivalent prose, files, or structured data. Ask only questions that change the recommendation. If essential inputs are absent, produce a provisional offer and a specific data collection plan.

Separate the end user, payer, buyer, and approver. Record B2B versus B2C, target geography, customer stage, current alternatives, the purchase trigger, and how frequently value occurs. Distinguish a new recommendation from an existing committed customer entitlement.

Use supplied evidence identifiers such as E001. Identify each material statement as observed, supplied, inferred, or an assumption. Do not invent interviews, conversion rates, competitor prices, market averages, taxes, or payment fees. Verify current external facts against primary sources when browsing is available. If unavailable, mark them unverified and state what would resolve them.

## Work through the decision

1. **Define the offer.** Specify target customer, desired outcome, included capabilities and service, exclusions, onboarding, support, customer responsibilities, usage boundaries, and delivery period. Test whether the promise is credible with available resources.
2. **Choose a charging unit and frequency.** Compare meaningful units such as account, seat, usage, transaction, credits, or supported outcome. Use a subscription when continuing value supports it. Consider a seasonal pass or one-time purchase for occasional value. Record measurability, predictability, controllability, and misuse exposure of the unit.
3. **Select simple packaging.** Begin with one intelligible paid offer; add tiers only when distinct needs or costs justify them. Define limits and upgrade triggers. Treat free access, trials, and pilots as explicit experiments with costs, eligibility, end conditions, and a conversion path.
4. **Model economics.** Read [the economics method](references/pricing-method.md). Use an explicit common analysis period and low, typical, and heavy usage scenarios. Separate fixed costs from per-customer delivery costs, tax from sales, gross cash from net sales, and recurring contract value from one-time or seasonal sales. Include AI/API, hosting, storage, payment, refund, and support assumptions without double counting.
5. **Assess commercial evidence.** Examine current customer spending, alternatives, purchase authority, responses to concrete prices, paid commitments, and subsequent use. Explain conflicting evidence and sample limitations. A competitor price or customer compliment cannot establish willingness to pay for this offer.
6. **Recommend an offer and price hypothesis.** State the recommended model, package, price range or exact test price, currency, tax basis, period, limits, support scope, and assumptions. Show one or two relevant alternatives and conditions that would change the recommendation. If costs or customer data cannot support a precise price, provide scenarios rather than false precision.
7. **Design the next experiment.** Define eligible customer segment, offer shown, comparable acquisition context, primary outcome, observation period, decision owner, budget, and continue/change/stop criteria. Predefine the criteria as proposed targets, not industry benchmarks. For small samples, prioritize recorded objections, actual decisions, and further learning over statistical claims. Record legal or billing questions for the responsible specialist.
8. **Prepare implementation and review tasks.** Identify required changes to landing-page terms, checkout, entitlements, cancellation/expiry, invoices, support, and measurement. Flag dependent work after a segment or offer change. Draft tasks; do not alter prices, make purchases, publish offers, or contact customers without the user's explicit request and available authorization.

## Calculate when useful

Run `python3 scripts/pricing_calculator.py assets/pricing-scenarios.example.json` only as an illustrative demonstration. Replace the fixture with actual input assumptions for a recommendation. Paths are relative to this skill's folder. The calculator requires Python 3 and only the standard library; it reads a JSON file and prints JSON without network access or modifying the input.

Use it for explicit period-level sales and contribution calculations. All costs and customer counts apply to the full stated service period. Include full variable delivery costs for refunded customers unless evidence supports another assumption. The model assumes complete refunds at the supplied rate; use a different documented model for partial refunds, mixed tax rates, staged usage, chargebacks, or complex revenue recognition.

If execution is unavailable, apply the formulas in the reference with an available calculator, expose the calculation steps, and label arithmetic not independently checked. Never claim the bundled script ran when it did not.

## Deliver the result

Use [the report template](assets/offer-pricing-report.template.md), adapting its length to the request. Include:

- Recommendation and the decision needed from the founder or mentor.
- Offer card and customer/usage assumptions.
- Evidence ledger, contradictions, and missing inputs.
- Comparable pricing and cost scenarios with units and periods.
- Sensitivities, limits, and consequences of heavy usage.
- Validation experiment and specific next tasks with owners, dependencies, deliverables, and completion criteria.

For structured export, follow [the output contract](references/output-contract.md); preserve its evidence and task identifiers. Keep the readable recommendation available even when JSON is requested. Offer a draft decision for mentor review without declaring market validation, product-market fit, or legal compliance.

Map relevant work to launch tasks L16–L25 and L39–L43 where the supplied program uses those identifiers. Do not imply that a generated document completes the associated field experiment.

## Check the work

Confirm that the offer matches the selected customer and value frequency; the charging unit is understandable; every price has currency, tax basis, and period; scenarios use compatible units; refunds and fees are modeled once; AI and support costs are explicit; free access has a cost limit; and the next experiment can disprove the recommendation. Preserve existing customer commitments until a separate authorized change is made.
