# Offer and pricing method

## Decision order

Define the customer's desired outcome and the service needed to deliver it. Choose a measurable charging unit, then the payment model, package, limits, and test price. Compare alternatives using the customer's context. A low competitor price does not establish the same delivery costs, customer segment, quality, or included service.

For B2B, identify the user, champion, budget owner, approver, procurement constraints, implementation effort, and renewal trigger. For B2C, distinguish user and payer, purchase occasion, ease of understanding, self-service first value, cancellation or expiry, and any seasonal cadence. A subscription, pass, or credits model remains a hypothesis until supported by customer behavior.

Make the initial offer concrete: customer; outcome; included product and service; scope; exclusions; customer inputs; support; usage limits; delivery period; price and tax presentation; trial/pilot terms; cancellation/expiry; and what happens afterward. Avoid promising a business result the startup cannot control.

## Evidence and tests

Use evidence for the question it can answer. Existing spending suggests a budget context. An interview reports a person's experience. A response to a specific offer provides more relevant price evidence than a general survey about an imagined tool. A payment is a commercial observation for that buyer and offer. Continued use or renewal adds evidence about delivered value. Record cancellations and negative evidence as well.

Do not extrapolate a few interviews into a conversion rate for the market. If sequential price tests use different traffic sources or seasons, record confounding factors. Do not claim statistical significance without an appropriate design, sample, and calculation. State numeric experiment targets as founder-defined or proposed thresholds.

## Calculator input

Use a JSON object with `currency` and a nonempty `scenarios` array. Each scenario has:

| Field | Meaning |
| --- | --- |
| name | Unique scenario label |
| model | `recurring`, `pass`, `one_time`, or `credits` |
| period_label | Human description of the complete analysis/service period |
| period_months | Positive number of months represented by that period |
| customers | Nonnegative whole count of purchasing customers for that period |
| price_per_customer | Positive total package price per customer for that period |
| price_includes_tax | Whether the input price includes the supplied tax |
| tax_rate | Supplied fractional rate, e.g. 0.20; verify separately |
| refund_rate | Expected fraction of complete customer purchases refunded, 0 to 1 |
| payment_fee_rate | Supplied fractional processor rate applied to initial gross customer charges |
| payment_fee_fixed | Supplied fixed processor fee per initial transaction |
| transactions_per_customer | Positive whole count of transactions collecting the total period price |
| processor_fees_returned_on_refund | Whether both modeled percentage and fixed original fees are returned proportionally for refunded purchases |
| refund_fee_per_refunded_transaction | Additional refund handling fee; use zero if absent |
| variable_costs_per_customer | Named nonnegative delivery costs per purchasing customer for the full period |
| fixed_costs_per_period | Nonnegative costs independent of customer count in the same period |

All monetary values use the same currency. Cost inputs should use the economically borne cost, consistently reflecting any recoverable taxes; determine that treatment with the responsible professional. Zero means an explicit assumption, not missing information. Do not use the calculator until required values are supplied or clearly labeled scenarios.

Use separate scenarios when fee schedules, tax rates, or refund treatment differ. `transactions_per_customer` affects fixed processing fees; it does not multiply the already-total period price. The model treats refunds as complete customer purchases and applies the same refund fraction to their associated transactions. It is not a partial-refund or accounting recognition engine.

The example fixture is entirely illustrative. Its prices, costs, rates, and counts are not current vendor rates, legal advice, a tax determination, or a suggested SaaS price.

## Formulas

Let `N` be customers, `P` the input period price, `t` tax rate, `r` refund rate, `k` transactions per customer, `f` percentage fee, `b` fixed fee, `q` extra refund fee, `V` total variable delivery cost per customer, `F` period fixed costs, and `m` period months.

- If price includes tax: gross price `G = P`; price excluding tax `X = P / (1 + t)`.
- If price excludes tax: `X = P`; gross price `G = P × (1 + t)`.
- Initial customer cash: `N × G`.
- Expected customer refunds: `N × G × r`.
- Modeled net sales excluding tax: `N × X × (1 − r)`.
- Tax remaining in customer cash: `N × (G − X) × (1 − r)`.
- Original processor fees: `N × G × f + N × k × b`.
- Net processor fees: original fees, multiplied by `(1 − r)` only if the input says both original fee components are returned, plus `N × k × r × q`.
- Variable delivery costs: `N × V`, including modeled refunded customers.
- Contribution: net sales excluding tax minus processor fees minus variable delivery costs.
- Contribution margin: contribution divided by positive net sales; undefined when net sales are zero.
- Result after modeled fixed costs: contribution minus `F`.
- Break-even customers: round up `F / contribution per customer` when per-customer contribution is positive; otherwise undefined. This assumes constant unit economics and excludes unmodeled costs.
- Normalized net sales per month: period net sales divided by `m`, regardless of business model.
- Contracted monthly recurring value excluding tax: `N × X / m` only for the `recurring` model. This is an illustrative normalization of stated recurring contracts, not observed company MRR. A refund alone does not specify cancellation, so it does not reduce this figure automatically.

Do not label normalized revenue from a pass or one-time sale as MRR. Cash collected upfront, period modeled net sales, accounting revenue recognition, and recurring contract value are different concepts. Keep their labels explicit. Do not infer LTV or a sustainable acquisition budget from a short pilot without retention and delivery-cost evidence.

## Sensitivity and checks

Vary customers, price, usage cost, support effort, refund rate, and frequency in explicit scenarios. Keep a common horizon for direct comparisons. Monthly normalization helps reveal periods but does not make a seasonal product's demand or cost pattern comparable to a recurring product automatically.

Record unmodeled costs such as acquisition, salaries, implementation, disputes, currencies, and other taxes. Reconcile any market data and customer evidence separately from this arithmetic. Review whether lower retention, heavier usage, or support effort would change the proposed limits or price.
