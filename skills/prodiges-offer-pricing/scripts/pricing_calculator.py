#!/usr/bin/env python3
"""Calculate explicit, illustrative period-level pricing scenarios from JSON.

Usage: python3 pricing_calculator.py input.json
No network access; reads only the selected JSON file and writes only to stdout.
See references/pricing-method.md for assumptions and limitations.
"""
import json
import sys
from decimal import Decimal, DecimalException, ROUND_CEILING, ROUND_HALF_UP
from pathlib import Path

ZERO = Decimal("0")
ONE = Decimal("1")
REQUIRED = {
    "name", "model", "period_label", "period_months", "customers",
    "price_per_customer", "price_includes_tax", "tax_rate", "refund_rate",
    "payment_fee_rate", "payment_fee_fixed", "transactions_per_customer",
    "processor_fees_returned_on_refund", "refund_fee_per_refunded_transaction",
    "variable_costs_per_customer", "fixed_costs_per_period",
}


def number(value, label, *, positive=False, integer=False, fraction=False):
    if isinstance(value, bool) or not isinstance(value, (int, float, str, Decimal)):
        raise ValueError(label + " must be a finite number")
    try:
        result = Decimal(str(value))
    except DecimalException:
        raise ValueError(label + " must be a finite number") from None
    if not result.is_finite() or result < ZERO or (positive and result <= ZERO):
        raise ValueError(label + " must be finite and " + ("positive" if positive else "nonnegative"))
    if integer and result != result.to_integral_value():
        raise ValueError(label + " must be a whole number")
    if fraction and result > ONE:
        raise ValueError(label + " must be between 0 and 1")
    return result


def boolean(value, label):
    if type(value) is not bool:
        raise ValueError(label + " must be true or false")
    return value


def label(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(field + " must be a nonempty string")
    return value.strip()


def amount(value):
    if value is None:
        return None
    return format(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), "f")


def ratio(value):
    if value is None:
        return None
    return format(value.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP), "f")


def calculate(scenario):
    if not isinstance(scenario, dict):
        raise ValueError("Each scenario must be an object")
    missing = REQUIRED - set(scenario)
    unknown = set(scenario) - REQUIRED
    if missing or unknown:
        raise ValueError("Scenario fields: missing=" + ",".join(sorted(missing)) + "; unknown=" + ",".join(sorted(unknown)))
    name = label(scenario["name"], "name")
    model = scenario["model"]
    if model not in {"recurring", "pass", "one_time", "credits"}:
        raise ValueError("model must be recurring, pass, one_time, or credits")
    period = label(scenario["period_label"], "period_label")
    months = number(scenario["period_months"], "period_months", positive=True)
    customers = number(scenario["customers"], "customers", integer=True)
    price = number(scenario["price_per_customer"], "price_per_customer", positive=True)
    includes_tax = boolean(scenario["price_includes_tax"], "price_includes_tax")
    tax = number(scenario["tax_rate"], "tax_rate", fraction=True)
    refunds = number(scenario["refund_rate"], "refund_rate", fraction=True)
    fee_rate = number(scenario["payment_fee_rate"], "payment_fee_rate", fraction=True)
    fee_fixed = number(scenario["payment_fee_fixed"], "payment_fee_fixed")
    transactions = number(scenario["transactions_per_customer"], "transactions_per_customer", positive=True, integer=True)
    returned = boolean(scenario["processor_fees_returned_on_refund"], "processor_fees_returned_on_refund")
    refund_fee = number(scenario["refund_fee_per_refunded_transaction"], "refund_fee_per_refunded_transaction")
    fixed_costs = number(scenario["fixed_costs_per_period"], "fixed_costs_per_period")
    components = scenario["variable_costs_per_customer"]
    if not isinstance(components, dict) or not components:
        raise ValueError("variable_costs_per_customer must be a nonempty object; use an explicit zero component if appropriate")
    variable_unit = ZERO
    checked_components = {}
    for key, value in components.items():
        key = label(key, "Variable cost name")
        checked_components[key] = number(value, "variable_costs_per_customer." + key)
        variable_unit += checked_components[key]
    gross_price = price if includes_tax else price * (ONE + tax)
    price_ex_tax = price / (ONE + tax) if includes_tax else price
    collected = customers * gross_price
    customer_refunds = collected * refunds
    net_sales = customers * price_ex_tax * (ONE - refunds)
    net_tax = customers * (gross_price - price_ex_tax) * (ONE - refunds)
    original_fee_unit = gross_price * fee_rate + transactions * fee_fixed
    retained_fee_unit = original_fee_unit * (ONE - refunds if returned else ONE)
    additional_refund_fee_unit = transactions * refunds * refund_fee
    processor_fee_unit = retained_fee_unit + additional_refund_fee_unit
    processor_fees = customers * processor_fee_unit
    variable_costs = customers * variable_unit
    contribution_unit = price_ex_tax * (ONE - refunds) - processor_fee_unit - variable_unit
    contribution = net_sales - processor_fees - variable_costs
    break_even = int((fixed_costs / contribution_unit).to_integral_value(rounding=ROUND_CEILING)) if contribution_unit > ZERO else None
    warnings = [
        "All inputs are scenario assumptions; verify their sources separately.",
        "Variable delivery costs cover every purchasing customer, including modeled refunded purchases.",
        "Complete-purchase refunds are modeled; no partial-refund, chargeback, or revenue-recognition logic is included.",
        "Acquisition and other unlisted costs are excluded. Break-even assumes constant unit economics.",
    ]
    if net_sales == ZERO:
        warnings.append("Net sales are zero, so contribution margin is undefined.")
    if model != "recurring":
        warnings.append("Monthly normalization of this nonrecurring model is not MRR.")
    return {
        "name": name,
        "model": model,
        "period_label": period,
        "period_months": str(months),
        "customers": int(customers),
        "gross_price_per_customer": amount(gross_price),
        "price_per_customer_ex_tax": amount(price_ex_tax),
        "initial_customer_cash": amount(collected),
        "expected_customer_refunds": amount(customer_refunds),
        "customer_cash_after_refunds": amount(collected - customer_refunds),
        "net_tax_in_customer_cash": amount(net_tax),
        "modeled_net_sales_ex_tax": amount(net_sales),
        "original_processor_fees": amount(customers * original_fee_unit),
        "returned_original_processor_fees": amount(customers * original_fee_unit * refunds if returned else ZERO),
        "additional_refund_fees": amount(customers * additional_refund_fee_unit),
        "net_processor_fees": amount(processor_fees),
        "variable_cost_components_per_customer": {key: amount(value) for key, value in checked_components.items()},
        "variable_delivery_costs": amount(variable_costs),
        "contribution": amount(contribution),
        "contribution_per_customer": amount(contribution_unit),
        "contribution_margin": ratio(contribution / net_sales) if net_sales > ZERO else None,
        "fixed_costs_per_period": amount(fixed_costs),
        "result_after_modeled_fixed_costs": amount(contribution - fixed_costs),
        "break_even_customers_at_constant_unit_economics": break_even,
        "normalized_net_sales_per_month": amount(net_sales / months),
        "contracted_monthly_recurring_value_ex_tax": amount(customers * price_ex_tax / months) if model == "recurring" else None,
        "warnings": warnings,
    }


def calculate_document(document):
    if not isinstance(document, dict) or set(document) != {"currency", "scenarios"}:
        raise ValueError("Input must contain exactly currency and scenarios")
    currency = label(document["currency"], "currency")
    scenarios = document["scenarios"]
    if not isinstance(scenarios, list) or not scenarios:
        raise ValueError("scenarios must be a nonempty array")
    results = [calculate(s) for s in scenarios]
    if len({s["name"] for s in results}) != len(results):
        raise ValueError("Scenario names must be unique")
    return {"calculation_version": "1.0.0", "currency": currency, "rounding": "Amounts round to 2 decimals only after calculation; no payment-processor rounding is simulated.", "scenarios": results}


def reject_constant(value):
    raise ValueError("Nonfinite JSON number is not allowed: " + value)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 pricing_calculator.py input.json", file=sys.stderr)
        return 2
    try:
        path = Path(sys.argv[1])
        if path.stat().st_size > 1048576:
            raise ValueError("Input exceeds the 1 MiB limit")
        with path.open(encoding="utf-8") as source:
            document = json.load(source, parse_float=Decimal, parse_constant=reject_constant)
        print(json.dumps(calculate_document(document), ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, TypeError, DecimalException) as exc:
        print("Invalid input: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
