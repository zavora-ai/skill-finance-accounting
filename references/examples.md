# Finance Skill Examples

## Example 1: "Invoice Acme Corp for their Pro plan"

**User says:** "Create an invoice for Acme Corp — Pro plan $500/month plus 5 extra users at $10 each"

**Tool calls:**
```
1. create_invoice(
     customer_id: "cust_acme",
     line_items: [
       {description: "Pro Plan - January 2025", quantity: 1, unit_price: 50000},
       {description: "Additional users", quantity: 5, unit_price: 1000}
     ],
     due_date: "2025-02-15",
     currency: "usd"
   )
   → {id: "inv_123", total: 55000, status: "unpaid"}
```

**Response:**
```
✅ Invoice created

**Invoice:** #123
**Customer:** Acme Corp
**Line Items:**
- Pro Plan - January 2025: $500.00
- Additional users (5 × $10): $50.00
**Total:** $550.00
**Due:** February 15, 2025

Would you like me to:
1. Send this invoice via email with a payment link?
2. Create a payment intent for instant collection?
```

## Example 2: "What invoices are overdue?"

**User says:** "Show me overdue invoices"

**Tool calls:**
```
1. list_invoices(status: "overdue")
   → [
       {id: "inv_100", customer: "Acme Corp", amount: 50000, due: "2024-12-01", days_overdue: 48},
       {id: "inv_108", customer: "TechCo", amount: 12000, due: "2025-01-01", days_overdue: 18},
       {id: "inv_110", customer: "StartupX", amount: 8500, due: "2025-01-05", days_overdue: 13}
     ]
```

**Response (uses aging-report.md template):**
```
## Accounts Receivable Aging

**Total Overdue:** $705.00 across 3 invoices

| Invoice | Customer | Amount | Days Overdue | Action |
|---------|----------|--------|-------------|--------|
| #100 | Acme Corp | $500.00 | 48 days 🚨 | Escalate to account manager |
| #108 | TechCo | $120.00 | 18 days | Send payment reminder |
| #110 | StartupX | $85.00 | 13 days | Send friendly reminder |

**Priority:** Acme Corp ($500 × 48 days = highest risk)

Recommended actions:
1. **Acme Corp** — 48 days overdue. Escalate to account manager. Consider late fee.
2. **TechCo** — Send firm reminder with payment link.
3. **StartupX** — Send friendly reminder (still within grace period).

Want me to send collection emails?
```

## Example 3: "How did we do this month?"

**User says:** "Give me the January P&L"

**Tool calls:**
```
1. get_profit_loss(period: "2025-01")
   → {revenue: 125000, cogs: 25000, gross_profit: 100000, opex: 65000, net_income: 35000}

2. get_cashflow(period: "2025-01")
   → {cash_in: 110000, cash_out: 72000, net: 38000, balance: 245000}
```

**Response:**
```
## January 2025 Financial Summary

### P&L
| | Amount |
|---|--------|
| Revenue | $1,250.00 |
| COGS | ($250.00) |
| **Gross Profit** | **$1,000.00** (80% margin) |
| Operating Expenses | ($650.00) |
| **Net Income** | **$350.00** (28% margin) |

### Cash Flow
| | Amount |
|---|--------|
| Cash In | $1,100.00 |
| Cash Out | ($720.00) |
| **Net Cash** | **$380.00** |
| **Cash Balance** | **$2,450.00** |

Revenue is strong. Note: $150 gap between revenue ($1,250) and cash in ($1,100) = uncollected invoices.
```
