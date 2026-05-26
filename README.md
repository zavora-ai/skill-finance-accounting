# Finance & Accounting Skill (Revenue Operations)

> Accelerate cash collection — create invoices instantly, track overdue payments, auto-reconcile bank deposits, and give leadership real-time financial visibility via QuickBooks, Xero, or local ledger.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--finance-green)](https://github.com/zavora-ai/mcp-finance)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## Revenue Impact

This skill directly accelerates revenue by:
- **Invoicing immediately** when deals close (zero delay = faster collection)
- **Flagging overdue invoices** daily with prioritized collection actions
- **Auto-reconciling** bank deposits to invoices (real-time revenue recognition)
- **Creating payment links** alongside invoices (reduce friction to pay)

| Workflow | Revenue Impact | Tool Calls |
|----------|---------------|-----------|
| Invoice & Collect | **Direct** — starts collection clock | 1-3 |
| Collections | **Recovery** — recovers overdue revenue | 2-4 |
| Reconciliation | **Recognition** — confirms revenue received | 2-3 |
| Financial Reporting | **Visibility** — enables decisions | 2-4 |

## Installation

```bash
git clone https://github.com/zavora-ai/skill-finance-accounting.git \
  ~/.skills/skills/finance-accounting
```

## Requirements

**Required:** `mcp-finance` (QuickBooks, Xero, or local ledger)

**Revenue-accelerating combos:**
- `mcp-payments` — instant payment links on invoices
- `mcp-email` — deliver invoices immediately
- `mcp-banking` — auto-reconcile incoming deposits
- `mcp-crm` — trigger invoicing on deal close

## Folder Structure

```
finance-accounting/
├── SKILL.md                       # Main skill
├── scripts/
│   └── calculate_invoice.py       # Invoice total/tax calculator
├── assets/
│   ├── aging-report.md            # AR aging template
│   └── financial-summary.md       # P&L/cash flow template
├── references/
│   ├── tool-sequences.md          # 14 tools with revenue impact tags
│   ├── cross-mcp-workflows.md     # 6-server revenue pipeline
│   └── examples.md                # Invoice, collections, reporting
├── README.md
└── LICENSE
```

## The Revenue Pipeline (6 MCP Servers)

```
CRM deal closes → FINANCE creates invoice → PAYMENTS creates payment link
→ EMAIL delivers to customer → BANKING detects deposit → FINANCE reconciles
```

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0

---

Part of the [ADK-Rust Enterprise](https://enterprise.adk-rust.com) skills ecosystem. Built with ❤️ by [Zavora AI](https://zavora.ai)

## Success Criteria

| Metric | Target |
|--------|--------|
| Invoice speed | Same-day invoicing on deal close |
| Collection rate | Overdue flagged within 24h |
| Reconciliation | 95%+ transactions matched |
