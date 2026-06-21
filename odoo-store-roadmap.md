# Odoo Module Launch Framework

> Template để launch module trên Odoo App Store. Dùng lại cho mọi module.
> Mỗi module điền vào **Per-Module Log** ở cuối file.

---

## Mục lục
1. [Process Template — 4 Phase](#process-template--4-phase)
2. [Checklists theo Phase](#checklists-theo-phase)
3. [Dashboard Template](#dashboard-template)
4. [Pivot Triggers](#pivot-triggers)
5. [Quick Reference](#quick-reference)
6. [Per-Module Log](#per-module-log)

---

## Process Template — 4 Phase

| Phase | Mục tiêu | Checkpoint | Thời gian |
|-------|----------|------------|-----------|
| **0 - Nghiên cứu** | Chọn niche, học Odoo dev | Biết niche + gap, Odoo chạy local | ~14 ngày |
| **1 - Free module** | Ship free module + credibility | Live trên store, rating ≥ 4.0 | ~30 ngày |
| **2 - Paid module** | Ship paid module đầu tiên | ≥ 1 purchase trong 30 ngày đầu | ~45 ngày |
| **3 - Scale** | Tối ưu + ship module tiếp | ≥ €100 MRR | ~45 ngày |
| **4 - Exit/Full-time** | Portal riêng, dual channel | ≥ €400/tháng | ~45 ngày |

---

## Checklists theo Phase

### Phase 0: Nghiên cứu & Nền tảng

```markdown
**Nghiên cứu thị trường:**
- [ ] Crawl Odoo Store (Apify) → top module by revenue, growth rate
- [ ] Tính Estimated Revenue = price × purchases
- [ ] Xác định: category nào ít module nhưng purchases cao?
- [ ] Đọc reviews module top — feature gì bị than phiền?
- [ ] List 5-10 đối thủ trong niche tiềm năng
- [ ] Feature gap analysis: điểm yếu chết người của từng đối thủ
- [ ] Validate demand: Google Trends, Reddit, LinkedIn
- [ ] Decision: GO / NO-GO

**Môi trường dev:**
- [ ] Docker + Odoo 19 local
- [ ] Database test + login được
- [ ] `odoo scaffold` hoạt động
- [ ] Module install/upgrade qua CLI được
- [ ] Git repo public

**Học Odoo cơ bản (nếu chưa biết):**
- [ ] Build 1 module đơn giản: model (Char, Integer, Float, Date, Selection, Many2one)
  view (tree, form, search), menu, security
- [ ] Đọc Vendor Guidelines + FAQ
- [ ] Odoo account sẵn sàng
```

### Phase 1: Free Module (Xây credibility)

```markdown
**Build module:**
- [ ] Tên module: <module_name>
- [ ] Model(s) + relation + computed fields
- [ ] Views: tree, form, search, graph, pivot, kanban (nếu cần)
- [ ] Security: access rights, record rules
- [ ] License: AGPL-3 / LGPL-3
- [ ] Multi-version compatible (18.0 + 19.0)
- [ ] Không hardcode path/company
- [ ] Test: cài được trên Odoo clean, không crash

**Presentation:**
- [ ] Icon: 512×512 PNG tại `static/description/icon.png`
- [ ] Cover: 1280×640 PNG tại `images/main_screenshot.png`
- [ ] HTML description: `static/description/index.html`
  Template: features list, screenshots, usage guide, requirements, support link
- [ ] Manifest: `images` key, `license`, `version` đúng format

**Store submission:**
- [ ] Push lên GitHub branch `19.0`
- [ ] Grant `online-odoo` read access (nếu private repo)
- [ ] Register repo tại apps.odoo.com → App Dashboard
- [ ] Scan repo → fix lỗi nếu reject

**OCA contribution:**
- [ ] Fork 1 repo OCA liên quan đến niche
- [ ] Fix 1 bug nhỏ / thêm 1 test
- [ ] Tạo PR, respond review
```

### Phase 2: Paid Module (Revenue)

```markdown
**Build paid module:**
- [ ] Tên module: <module_name>
- [ ] Features cốt lõi (must-have), không feature creep
- [ ] License: OPL-1
- [ ] Giá: <price> EUR
- [ ] Currency: EUR (hoặc USD)
- [ ] Không require Studio, không require Enterprise
- [ ] Test: Odoo 18 + 19
- [ ] PEP8 + security check

**License enforcement:**
- [ ] OPL-1 trong LICENSE file
- [ ] (optional) License key check — validate domain

**Submit:**
- [ ] Push lên GitHub (private, grant online-odoo read)
- [ ] Register repo + scan
- [ ] KHÔNG bán rẻ hơn trên platform khác (price parity)

**Marketing:**
- [ ] HTML description chuyên nghiệp (bảng so sánh, screenshots)
- [ ] Email outreach: 20 Odoo partner nhỏ
- [ ] LinkedIn case study post
- [ ] Reddit: comment hữu ích
- [ ] Check Store Quality Score: icon, cover, license, rating ≥3, HTML

**Sales:**
- [ ] A/B test giá nếu cần
- [ ] Free trial version (base free + paid features)
- [ ] Support trong 24h, xin review
```

### Phase 3: Scale

```markdown
- [ ] Học từ dữ liệu: ai mua? từ đâu? feature request gì?
- [ ] Ship module thứ 2 (add-on / cross-sell)
- [ ] Bundle pricing: base + add-on = suite (tiết kiệm %)
- [ ] CI/CD: GitHub Actions tự động test
- [ ] Maintain multi-version
- [ ] Odoo IAP (25% commission vs 30%)
```

### Phase 4: Exit / Full-time

```markdown
- [ ] Tự host distribution portal + license key server
- [ ] Subscription model (€X/tháng)
- [ ] Dual channel: Odoo Store = lead gen, portal = direct (100% margin)
- [ ] Viindoo Marketplace (VND)
- [ ] Gumroad
- [ ] White-label cho partner
```

---

## Dashboard Template

```markdown
Tuần: ___
Module: <module_name>

Downloads (free): ___ / target ___
Purchases (paid): ___ / target ___
MRR (€): ___ / target ___
Store Quality Score: __/5
Rating: ___
GitHub stars: ___

Vấn đề:
- [ ] Bug cần fix: ___
- [ ] Support pending: ___
- [ ] Marketing đã làm: ___

Quyết định tuần tới: _______________
```

---

## Pivot Triggers

| Tình huống | Diagnostic | Hành động |
|-----------|-----------|-----------|
| Downloads nhiều, purchases 0 | Giá quá cao / free module đã đủ tốt | Hạ giá / giới hạn tính năng free |
| Cả downloads + purchases đều 0 | Sai niche / sai marketing | Pivot niche (Phase 0) |
| Có purchase, rating thấp | Bug / thiếu tính năng | Fix ngay, hỏi khách |
| Rating cao, ít purchase | Marketing yếu | Tăng content, outreach |
| Có purchase, không repeat | Thiếu lý do mua thêm | Thêm subscription/add-on |
| Revenue ổn, không scale | Chạm trần niche | Mở rộng niche liên quan |

---

## Quick Reference

| Rule | Chi tiết |
|------|----------|
| **Manifest name** | ≤ 25 ký tự, ko tên công ty |
| **Version format** | `19.0.1.0.0` (major.minor.bugfix) |
| **Free license** | AGPL-3 hoặc LGPL-3 |
| **Paid license** | OPL-1 |
| **License compat** | AGPL-3 → AGPL/GPL/LGPL; OPL-1 → LGPL/OPL-1 |
| **Min paid price** | €9 |
| **Store Score** | 5 criteria: icon, cover, license, rating ≥3, HTML desc |
| **Commission** | 30% regular, 25% IAP |
| **Payout** | SWIFT khi PO ≥ €400 |
| **Price parity** | Giá Odoo Store ≤ các platform khác |
| **Private repo** | Grant read to `online-odoo` GitHub user |
| **Description** | English, HTML, ko JS, ko link store khác |
| **Paid module** | OPL-1 required, có thể private repo |

---

## Per-Module Log

### Module A: AI Inventory Report Generator [CURRENT]

**Target:** €200-800 MRR tại tháng 12/2026
**Start:** 22/06/2026

#### Phase 0: Research ✅
- Niche: AI Inventory Report Generator cho Community Edition
- 11 đối thủ analyzed (xem bảng dưới)
- Gap: no module = NL query + Inventory focus + CE tối ưu + Scheduled + Multi-export
- Decision: **GO**

**Competitor analysis:**

| Module | Giá | LoC | Mạnh | Yếu chết người |
|--------|-----|-----|------|---------------|
| Odoo AI Copilot Assistant | €199 | - | Full CRUD, multi-provider | Không focus reporting, no schedule |
| AI Studio (erpblox) | Paid | - | Full suite, MCP, scheduled | Quá đồ sộ, learning curve cao |
| AI Insight Assistant | Paid | 18K | Voice prompt, reasoning | Nặng, generic chatbot |
| Claude AI Assistant | €29 | - | Cheap, multi-model | Basic, support kém |
| AI Dynamic Report Gen | Free | 2.6K | Gemini, export | LGPL free, chỉ Gemini, buggy |
| AI Copilot (setu) | Free | 6.7K | Charts, KPIs | Free, basic ko support |
| AI Power Search | Free | 1.3K | NL search bar | Search only, ko generate |
| Stock Card Report | - | - | +1.2M% growth | Không AI, basic QWeb |

**Product line:**
```
Phase 1 → Free: Enhanced Stock Card Report (đáp ứng demand +1.2M%)
Phase 2 → Paid: AI Report Generator (natural language → Odoo data → table/chart/export)
Phase 3 → Paid add-on: AI Scheduled Reports (daily/weekly auto email)
Phase 4 → Suite: "AI Reporting Suite" bundle €299
```

**Product-specific notes:**
- `stock_report` (`stock.card.wizard` + `stock.card.report.line`)
- Phải dùng `stock.group_stock_user` cho security
- Menu gắn dưới `stock.menu_warehouse_report`

#### Phase 1: Free Module — Enhanced Stock Card Report
**Code** ✅ (22/06):
- Wizard: date range, multi-product, multi-warehouse, category filter
- Running balance with valuation (incoming/outgoing qty × unit cost)
- Views: tree (multi_edit=0), graph (bar chart), pivot
- PDF QWeb report per-product with totals
- Menu: Inventory > Reporting > Stock Card Report

**Presentation** ✅ (22/06):
- Icon 512×512 at `static/description/icon.png`
- Cover 1280×640 at `images/main_screenshot.png`
- HTML description at `static/description/index.html`

**Store submission** ⏳:
- [ ] Branch 19.0 created on GitHub
- [ ] User tự register repo trên apps.odoo.com
- [ ] Scan + fix lỗi

#### Phase 2: Paid Module — AI Report Generator ⏳
*Chưa bắt đầu*

#### Phase 3-4: *Chưa bắt đầu*

---

### Module B: *TBD* (dùng template này khi bắt đầu module mới)

---

## Links

- Submit: https://apps.odoo.com/apps/upload
- Vendor Guidelines: https://apps.odoo.com/apps/vendor-guidelines
- FAQ: https://apps.odoo.com/apps/faq
- Dashboard: https://apps.odoo.com/apps/dashboard
- Odoo Dev Docs: https://www.odoo.com/documentation/master/developer.html
- OCA: https://github.com/OCA
- Viindoo: https://viindoo.com/vi/repo_upload
- Apify: https://apify.com/foxpink/odoo-apps-market-intelligence
- Affiliate: https://www.odoo.com/affiliate (10% referral)
