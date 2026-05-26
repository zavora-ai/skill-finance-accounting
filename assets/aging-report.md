# Accounts Receivable Aging Report

---

## AR Aging — {date}

**Total Outstanding:** ${total_outstanding}
**Total Overdue:** ${total_overdue} ({overdue_pct}% of outstanding)

### Aging Summary

| Bucket | Count | Amount | % of Total |
|--------|-------|--------|-----------|
| Current (not due) | {count} | ${amount} | {pct}% |
| 1-30 days overdue | {count} | ${amount} | {pct}% |
| 31-60 days overdue | {count} | ${amount} | {pct}% |
| 61-90 days overdue | {count} | ${amount} | {pct}% |
| 90+ days overdue | {count} | ${amount} | {pct}% |

### Top Overdue Invoices (Action Required)

| Invoice | Customer | Amount | Days Overdue | Action |
|---------|----------|--------|-------------|--------|
| {inv_id} | {customer} | ${amount} | {days} | {recommended_action} |

### Revenue at Risk

- **30-day forecast impact:** ${amount} if not collected
- **Customers with multiple overdue:** {count} ({list})
- **Recommended write-offs (90+ days):** ${amount}

### Collection Actions Taken

| Date | Customer | Invoice | Action | Result |
|------|----------|---------|--------|--------|
| {date} | {customer} | {inv_id} | {reminder/call/escalation} | {pending/paid/no_response} |

---

*Generated from mcp-finance | {timestamp}*
