# Finance Cross-MCP Workflows (Revenue Acceleration)

## Finance + Payments + Email: Invoice-to-Cash Pipeline

### Create invoice → Collect immediately
```
FINANCE: create_invoice(customer: "acme", line_items: [...], due_date: "2025-02-15") → {id: "inv_123", total: 55000}
PAYMENTS: create_checkout_intent(amount: 55000, currency: "usd", reference: "inv_123", idempotency_key: "checkout_inv_123")
PAYMENTS: attach_payment_evidence(payment_id: "pi_xyz", evidence_type: "invoice", reference: "inv_123")
EMAIL: email_send(to: "billing@acme.com", subject: "Invoice #123 — $550.00", body: "Pay online: [link]")
CRM: create_activity(type: "email", subject: "Invoice #123 sent to Acme Corp")
```
**Revenue impact:** Reduces DSO by enabling instant payment at invoice delivery.

## Finance + CRM: Deal Closed → Auto-Invoice

### CRM deal closes → Generate invoice automatically
```
CRM: move_deal_stage(id: "d_123", stage: "Closed Won")
CRM: get_deal(id: "d_123") → {value: 75000, customer: "cust_acme", name: "Enterprise Annual"}
FINANCE: create_invoice(
  customer_id: "cust_acme",
  line_items: [{description: "Enterprise Plan - Annual", quantity: 1, unit_price: 75000}],
  due_date: "2025-02-15"
)
PAYMENTS: create_checkout_intent(amount: 75000, reference: "inv_new")
EMAIL: email_send(to: customer_email, subject: "Welcome! Invoice for Enterprise Plan")
```
**Revenue impact:** Zero delay between deal close and invoice — no revenue leakage.

## Finance + Banking: Auto-Reconciliation

### Bank deposit arrives → Match to invoice → Mark paid
```
BANKING: list_transactions(account: "checking", since: "yesterday") → [{amount: 55000, description: "ACME CORP"}]
FINANCE: list_invoices(status: "unpaid", customer: "acme") → [{id: "inv_123", amount: 55000}]
FINANCE: reconcile_transaction(transaction_id: "txn_abc", reference_type: "invoice", reference_id: "inv_123")
CRM: create_activity(type: "note", subject: "Payment received: $550 from Acme Corp")
```
**Revenue impact:** Real-time revenue recognition, accurate cash position.

## Finance + Slack: Collections Alerts

### Daily overdue alert
```
FINANCE: list_invoices(status: "overdue") → [{customer: "Acme", amount: 50000, days: 45}, ...]
SLACK: send_message(channel: "#finance-ops", text: "💰 *Daily Collections*\n\n*Overdue: $1,250.00 across 3 invoices*\n• Acme Corp: $500 (45 days) 🚨\n• TechCo: $450 (30 days) ⚠️\n• StartupX: $300 (15 days)\n\nTotal AR: $5,000 | DSO: 38 days")
```

## Finance + Notifications: Payment Received

### Customer pays → Notify team
```
FINANCE: reconcile_transaction(...) → invoice marked paid
NOTIFICATIONS: notification_send(recipient: account_owner, channel: "push", title: "💰 Payment Received", body: "$550 from Acme Corp (inv_123)")
```

## Full Revenue Cycle (6 MCP servers)

```
1. CRM: Deal closes → trigger invoicing
2. FINANCE: Create invoice with line items
3. PAYMENTS: Create payment intent with link
4. EMAIL: Send invoice with payment link
5. BANKING: Monitor for incoming payment
6. FINANCE: Reconcile payment to invoice
7. CRM: Log payment received
8. SLACK: Notify team of collection
```
