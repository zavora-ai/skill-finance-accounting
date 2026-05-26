# Finance Tool Sequences Reference

## Tool Inventory (mcp-finance, 14 tools)

| Tool | Risk | Revenue Impact |
|------|------|---------------|
| `list_invoices` | read | Track outstanding revenue |
| `get_invoice` | read | Invoice details |
| `create_invoice` | write | **DIRECT: Triggers collection** |
| `list_expenses` | read | Cost visibility |
| `create_expense` | write | Record costs |
| `list_accounts` | read | Chart of accounts |
| `get_account_balance` | read | Account balances |
| `list_transactions` | read | Bank activity |
| `create_journal_entry` | financial | Adjustments |
| `reconcile_transaction` | write | **Match payments to invoices** |
| `get_profit_loss` | read | Revenue reporting |
| `get_balance_sheet` | read | Financial position |
| `get_cashflow` | read | Cash visibility |
| `get_tax_summary` | read | Tax obligations |

## Sequence: Create & Send Invoice (Revenue Trigger)

```
1. create_invoice(
     customer_id: "cust_acme",
     line_items: [
       {description: "Pro Plan - January 2025", quantity: 1, unit_price: 50000},
       {description: "Additional users (5)", quantity: 5, unit_price: 1000}
     ],
     due_date: "2025-02-15",
     currency: "usd",
     tax_rate: 0,
     notes: "Net 30. Late fee: 1.5%/month after due date."
   )
   → {id: "inv_123", total: 55000, status: "unpaid"}

2. [Cross-MCP] PAYMENTS: create_checkout_intent(amount: 55000, reference: "inv_123")
   → {payment_url: "https://pay.company.com/pi_xyz"}

3. [Cross-MCP] EMAIL: email_send(
     to: "billing@acme.com",
     subject: "Invoice #123 — $550.00 due Feb 15",
     body: "Please find attached invoice. Pay online: [payment_url]"
   )
```

## Sequence: Collections Run (Revenue Recovery)

```
1. list_invoices(status: "overdue")
   → [
       {id: "inv_100", customer: "Acme", amount: 50000, days_overdue: 45},
       {id: "inv_105", customer: "TechCo", amount: 12000, days_overdue: 15}
     ]

2. Sort by: amount × days_overdue (priority score)
   → Acme: 50000 × 45 = 2,250,000 (highest priority)

3. For each overdue invoice:
   get_invoice(id: "inv_100") → full details with payment terms

4. [Cross-MCP] EMAIL: email_send(to: customer, subject: "Payment Reminder: Invoice #100 overdue")

5. [Cross-MCP] CRM: create_activity(type: "task", subject: "Collection: $500 overdue 45 days")
```

## Sequence: Auto-Reconciliation

```
1. list_transactions(account: "checking", status: "unreconciled")
   → [{id: "txn_abc", amount: 50000, description: "ACME CORP PAYMENT", date: "2025-01-18"}]

2. list_invoices(status: "unpaid", customer: "acme")
   → [{id: "inv_100", amount: 50000}]

3. reconcile_transaction(transaction_id: "txn_abc", reference_type: "invoice", reference_id: "inv_100")
   → {status: "reconciled", invoice_status: "paid"}
```

## Sequence: Monthly Financial Close

```
1. list_transactions(status: "unreconciled") → ensure all matched
2. get_profit_loss(period: "2025-01") → revenue, expenses, net income
3. get_balance_sheet(as_of: "2025-01-31") → assets, liabilities, equity
4. get_cashflow(period: "2025-01") → operating, investing, financing
5. get_tax_summary(period: "2025-Q1") → tax obligations
```
