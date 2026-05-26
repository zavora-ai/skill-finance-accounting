#!/usr/bin/env python3
"""
Invoice Calculator & Validator
Calculates totals, tax, and validates invoice before creation.
Usage: python calculate_invoice.py '{"line_items": [{"description": "...", "quantity": 1, "unit_price": 5000}], "tax_rate": 0.16}'
"""
import json
import sys
from datetime import datetime, timedelta

def calculate_invoice(data: dict) -> dict:
    line_items = data.get("line_items", [])
    tax_rate = data.get("tax_rate", 0)
    currency = data.get("currency", "usd")
    terms_days = data.get("terms_days", 30)

    result = {"valid": True, "errors": [], "computed": {}}

    # Validate line items
    if not line_items:
        result["valid"] = False
        result["errors"].append("At least one line item required")
        return result

    subtotal = 0
    computed_items = []
    for i, item in enumerate(line_items):
        if not item.get("description"):
            result["errors"].append(f"Line {i+1}: description required")
            result["valid"] = False
        qty = item.get("quantity", 1)
        price = item.get("unit_price", 0)
        if price <= 0:
            result["errors"].append(f"Line {i+1}: unit_price must be positive (in minor units)")
            result["valid"] = False
        line_total = qty * price
        subtotal += line_total
        computed_items.append({**item, "line_total": line_total})

    tax_amount = int(subtotal * tax_rate)
    total = subtotal + tax_amount
    due_date = (datetime.now() + timedelta(days=terms_days)).strftime("%Y-%m-%d")

    result["computed"] = {
        "line_items": computed_items,
        "subtotal": subtotal,
        "tax_rate": tax_rate,
        "tax_amount": tax_amount,
        "total": total,
        "currency": currency,
        "due_date": due_date,
        "terms": f"Net {terms_days}",
        "display_total": f"{total / 100:.2f}" if currency != "jpy" else str(total),
    }

    # Sanity checks
    if total > 10000000:  # > $100k
        result["computed"]["warning"] = "Large invoice (> $100k) — verify with user"
    if total < 100:  # < $1
        result["computed"]["warning"] = "Very small invoice (< $1) — verify intended"

    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python calculate_invoice.py \'{"line_items": [...], "tax_rate": 0.16}\'')
        sys.exit(1)
    data = json.loads(sys.argv[1])
    print(json.dumps(calculate_invoice(data), indent=2))
