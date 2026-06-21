# Odoo App Store — Lộ trình 180 ngày cho tài khoản mới

Ngày bắt đầu: 22/06/2026   |   Target: €200-800 MRR tại tháng 12/2026

---

## Tổng quan các Phase

| Phase | Thời gian | Mục tiêu chính | Checkpoint |
|-------|-----------|----------------|------------|
| 0 - Research | Ngày 1-14 | Chọn niche + học Odoo dev | Có niche cụ thể + module mẫu chạy được |
| 1 - Xây credibility | Ngày 15-45 | Ship 1 free module + OCA contribute | Free module live trên store, rating ≥ 4.0 |
| 2 - Module bán đầu tiên | Ngày 46-90 | Ship paid module đầu tiên | ≥ 1 purchase trong 30 ngày đầu |
| 3 - Marketing & vòng lặp | Ngày 91-135 | Tối ưu listing + ship module thứ 2 | ≥ 5 purchases, ≥ 2 reviews |
| 4 - Scale | Ngày 136-180 | Bundle + tự host portal | ≥ €400/tháng → quyết định tự host |

---

## Phase 0: Research & Nền tảng (Ngày 1-14)

### Tuần 1: Chọn niche (Ngày 1-7)

**Ngày 1-2: Phân tích thị trường** ✅ (22/06/2026)
- [x] Crawl Odoo App Store bằng Apify (apps.odoo.com) — export danh sách module, giá, purchases
- [x] Tính Estimated Revenue = price × purchases cho top module
- [x] Ghi lại: category nào có ít module nhưng purchases cao?
- [x] Đọc reviews của module top — feature gì bị than phiền nhiều?

**Ngày 3-4: Xác định niche** ✅ (22/06/2026)
- [x] Crawl data xong — top module: Shopify Connector (€403, ~€927K), Dashboard Ninja (€518, ~€1.58M)
- [x] Top tăng trưởng: Stock Card (+1.281M%), Accounting Reports (+2.484%), AI/MCP Server (+1.172%)
- [x] Đã analyze feature gap 11 AI modules đối thủ (xem bảng dưới)

  **Phân tích đối thủ — AI Reporting modules trên Odoo Store:**
  | Module | Giá | LoC | Mạnh | Yếu chết người |
  |--------|-----|-----|------|---------------|
  | Odoo AI Copilot Assistant | €199 | - | Full CRUD, multi-provider | Không focus reporting, no schedule |
  | AI Studio (erpblox) | Paid | - | Full suite, MCP, scheduled | Quá đồ sộ, learning curve cao |
  | AI Insight Assistant | Paid | 18K | Voice prompt, reasoning | Nặng, generic chatbot |
  | Claude AI Assistant | €29 | - | Cheap, multi-model | Basic, support kém |
  | AI Dynamic Report Gen | Free | 2.6K | Gemini, export | LGPL free, chỉ Gemini, buggy |
  | AI Copilot (setu) | Free | 6.7K | Charts, KPIs | Free, basic ko support |
  | AI Power Search | Free | 1.3K | NL search bar | Search only, ko generate |
  | Stock Card Report | - | - | +1.2M% growth | **Không AI, basic QWeb** |

  **Gap = không có module nào = AI Report Generator chuyên sâu + Inventory focus + CE tối ưu + Scheduled + Multi-export**

- [x] **Niche chính**: AI Inventory Report Generator cho Community Edition
- [x] **Niche dự phòng**: Advanced Portal Customization Tool (nếu AI fails)

  **Chiến lược sản phẩm:**
  ```
  Phase 1 → Free: Enhanced Stock Card Report (đáp ứng demand +1.2M%, build credibility)
  Phase 2 → Paid: AI Report Generator (natural language → Odoo data → table/chart/export)
  Phase 3 → Paid add-on: AI Scheduled Reports (daily/weekly auto email)
  Phase 4 → Suite: "AI Reporting Suite" bundle €299
  ```

**Ngày 5-7: Validate nhu cầu** ✅ (22/06/2026)
- [x] Search Google Trends — "Odoo AI Community Edition" trending 2026
- [x] Reddit r/Odoo — inventory report, deposit report, stock forecast là pain points thật
- [x] LinkedIn/Guides — "AI for Odoo Community Edition" guide xác nhận no AI for CE
- [x] **Quyết định: GO.** Niche = AI Inventory Report Generator cho Community Edition

**Checkpoint Phase 0a:**
```
[ ] Có niche cụ thể (ví dụ: "Odoo rental module cho thiết bị xây dựng")
[ ] Biết rõ ít nhất 3 đối thủ cạnh tranh trong niche
[ ] Biết rõ feature gap của họ (ít nhất 3 điểm yếu)
```

### Tuần 2: Học & thiết lập môi trường (Ngày 8-14)

**Ngày 8-10: Môi trường dev** ✅ (22/06/2026)
- [x] Docker 29.3.1 sẵn sàng
- [x] docker-compose.yml: Odoo 19.0 + PostgreSQL 16
- [x] Database `stock_card_dev` tạo thành công
- [x] `odoo scaffold test_module /mnt/extra-addons` hoạt động
- [x] Module install + upgrade qua CLI thành công
- [ ] VS Code: user tự cài sau

**Ngày 11-12: Odoo dev cơ bản**
- [ ] Tự build module "Library Management" đơn giản (model, view, menu, security)
- [ ] Push lên GitHub public
- [ ] Viết README.md cho module

**Ngày 13-14: Kiểm tra kỹ thuật**
- [ ] Đọc Odoo Vendor Guidelines (apps.odoo.com/apps/vendor-guidelines)
- [ ] Đọc Submit your Apps FAQ (apps.odoo.com/apps/faq)
- [ ] Tạo Odoo account + truy cập được App Dashboard

**Checkpoint Phase 0b:**
```
[ ] Odoo chạy local, scaffold module được
[ ] GitHub repo public, module cơ bản hoạt động
[ ] Đã đọc hết vendor guidelines
[ ] Biết chính xác license nào dùng cho free (AGPL-3) vs paid (OPL-1)
```

**METRICS THEO DÕI PHASE 0:**
| Metric | Target | Cảnh báo | Hành động nếu fail |
|--------|--------|----------|-------------------|
| Niche có Gap Score | ≥ 7/10 | < 5/10 | Đổi niche |
| Số đối thủ trong niche | 3-10 | > 20 | Cần niche hẹp hơn |
| Domain knowledge tự đánh giá | 7/10 | < 5/10 | Học thêm 1 tuần trước khi vào Phase 1 |

---

## Phase 1: Xây Credibility (Ngày 15-45)

### Tuần 3-4: Build free module (Ngày 15-28)

**Ngày 15-18: Code module free — Enhanced Stock Card Report**
- [ ] Product: module free báo cáo Stock Card Valuation nâng cao (hơn module +1.2M% kia)
- [ ] Features: multi-warehouse, date range filter, export PDF/Excel, beautiful chart
- [ ] License: AGPL-3 (free)
- [ ] Test kỹ: cài được trên Odoo clean, không crash
- [ ] Không hardcode path, không hardcode company info

**Ngày 19-20: Tối ưu presentation**
- [ ] Icon: 512×512px, PNG trong `static/description/icon.png`
- [ ] Cover banner: 1280×640px, đặt trong `images` key của manifest
- [ ] HTML description: dùng template từ apps.odoo.com (tối thiểu: tính năng, ảnh chụp màn hình, yêu cầu hệ thống)

**Ngày 21-24: Đăng ký repo**
- [ ] Push module lên GitHub public branch `19.0`
- [ ] Register repo tại apps.odoo.com → App Dashboard
- [ ] Scan repo — kiểm tra không có lỗi
- [ ] Nếu bị reject: sửa lỗi, scan lại

**Ngày 25-28: OCA contribution**
- [ ] Fork 1 repo OCA liên quan đến niche
- [ ] Fix 1 bug nhỏ hoặc thêm 1 test
- [ ] Tạo PR, respond review

### Tuần 5-6: Tạo visibility (Ngày 29-45)

**Ngày 29-35: Content marketing**
- [ ] Viết 1 blog post về niche (kèm link module free)
- [ ] Trả lời 5 câu hỏi trên r/Odoo (chất lượng, có ích)
- [ ] LinkedIn: update profile thành "Odoo [Niche] Developer"
- [ ] Tạo 1 video demo ngắn (3-5 phút) đăng YouTube

**Ngày 36-40: Thu thập feedback**
- [ ] Gửi module free cho 3-5 người dùng thử (Reddit, Odoo forum)
- [ ] Ghi nhận bug/feature request
- [ ] Fix bug, update module

**Ngày 41-45: Review & quyết định**
- [ ] Kiểm tra rating trên store (nếu có)
- [ ] Xem download count
- [ ] Quyết định: tiếp tục niche này hay pivot?

**METRICS THEO DÕI PHASE 1:**
| Metric | Target tuần 4 | Target tuần 6 | Hành động nếu fail |
|--------|---------------|---------------|-------------------|
| Free module downloads | ≥ 20 | ≥ 100 | Tăng content marketing |
| Module rating | ≥ 4.0 | ≥ 4.5 | Fix bug, cải thiện UX |
| OCA PR merged | - | ≥ 1 | Đọc contribution guide kỹ hơn |
| Số người dùng feedback | - | ≥ 3 | Chủ động reach out hơn |
| GitHub stars repo | ≥ 5 | ≥ 15 | Share lên dev groups |

**Pivot trigger:** Nếu < 20 downloads sau 45 ngày → niche không có demand hoặc presentation kém.
- Hành động: A/B test title/description, nếu vẫn không được → pivot niche.

---

## Phase 2: Module Bán Đầu Tiên (Ngày 46-90)

### Tuần 7-8: Build paid module (Ngày 46-60)

**Ngày 46-52: Code paid module — AI Report Generator**
- [ ] Product: AI Report Generator — gõ "top 10 products by profit margin" → AI query Odoo → table/chart/export
- [ ] Features: natural language input, multi-model (sales, stock, accounting), chart (bar/pie/line), export XLSX/PDF
- [ ] Tech: LLM API (OpenAI/Claude/Gemini) → ORM query → render
- [ ] License: OPL-1, giá: €149.00, currency: EUR
- [ ] Không require Studio, không require Enterprise
- [ ] HTML description chuyên nghiệp (có bảng so sánh với đối thủ, screenshots, demo video)
- [ ] Test trên Odoo 18 + 19
- [ ] Kiểm tra PEP8, security issues

**Ngày 53-55: License enforcement**
- [ ] Cơ bản: OPL-1 trong LICENSE file
- [ ] Nâng cao (tùy chọn): thêm license key check - validate domain khi module khởi động

**Ngày 56-60: Submit & review**
- [ ] Push lên GitHub (có thể private nếu paid, cấp quyền read cho user online-odoo)
- [ ] Register repo + scan
- [ ] Nếu reject: sửa trong 24h, rescan
- [ ] **KHÔNG** bán rẻ hơn trên website khác (vi phạm price parity rule)

### Tuần 9-12: Sales đầu tiên (Ngày 61-90)

**Ngày 61-70: Push marketing**
- [ ] Email outreach: 20 Odoo partner nhỏ trong niche
- [ ] LinkedIn: post case study
- [ ] Reddit: comment hữu ích, mention module khi phù hợp
- [ ] Xem xét Odoo Affiliate Program (10% referral, non-Partner cũng được)

**Ngày 71-80: Tối ưu conversion**
- [ ] A/B test giá: nếu €99 không ai mua → thử €49
- [ ] Thêm free trial version (base module free + paid features)
- [ ] Check Store Quality Score (5 criteria trên dashboard):
  - [ ] Icon?
  - [ ] Cover image?
  - [ ] License set?
  - [ ] Rating ≥ 3?
  - [ ] HTML description?

**Ngày 81-90: First purchase**
- [ ] Nếu có purchase → support ngay lập tức, xin review
- [ ] Nếu chưa có → review lại pricing, marketing, niche

**METRICS THEO DÕI PHASE 2:**
| Metric | Target | Cảnh báo | Hành động |
|--------|--------|----------|-----------|
| Purchase trong 30 ngày đầu | ≥ 1 | 0 → cuối tuần 12 | Giảm giá, đổi cách marketing, hoặc pivot |
| Store Quality Score | 5/5 | < 3/5 | Fix ngay theo hướng dẫn |
| Tỉ lệ view → purchase | > 1% | < 0.5% | Cải thiện description/screenshots |
| Support response time | < 24h | > 48h | Tự động hóa FAQ |
| Rating sau bán | ≥ 4.0 | < 3.5 | Fix bug, hỏi lý do |

**Pivot trigger cuối Phase 2:**
- Nếu 0 purchases sau 90 ngày: **pivot ngay**.
- Phân tích: sai niche? sai giá? sai marketing? Niche không có demand thật?
- Chuyển hướng: quay lại Phase 0 với niche khác, hoặc chuyển sang làm implementation consulting thay vì bán module.

---

## Phase 3: Marketing & Vòng lặp (Ngày 91-135)

### Tuần 13-15: Tối ưu & Ship module thứ 2 (Ngày 91-112)

**Ngày 91-98: Học từ dữ liệu**
- [ ] Phân tích: ai mua module? từ đâu? ngành gì?
- [ ] Feature request từ khách → ưu tiên phát triển
- [ ] Update module: fix bug, thêm tính năng được yêu cầu

**Ngày 99-105: Build module thứ 2 — AI Scheduled Reports**
- [ ] Product: AI Scheduled Reports add-on — schedule AI queries daily/weekly/monthly, auto-email PDF
- [ ] Chiến lược: **paid add-on** cho AI Report Generator (€79)
- [ ] Bundle: base (€149) + scheduler (€79) = suite €199 (tiết kiệm €29)
- [ ] Cross-sell tự nhiên: ai mua AI Report Gen sẽ cần scheduler
- [ ] Áp dụng kinh nghiệm từ module 1 (tránh sai lầm cũ)

**Ngày 106-112: Ship & cross-sell**
- [ ] Thêm "You may also like" trong description
- [ ] Discount bundle: mua 2 module giảm 15%

### Tuần 16-19: Tối ưu hóa (Ngày 113-135)

**Ngày 113-120: Vận hành**
- [ ] Thiết lập CI/CD: GitHub Actions tự động test + deploy
- [ ] Maintain cho nhiều version (18.0, 19.0)
- [ ] Update 2 tuần/lần nếu có bug

**Ngày 121-128: Revenue optimization**
- [ ] Nếu module 1 chạy tốt → tăng giá (€99 → €129)
- [ ] Nếu module 1 chạy yếu → bundle với module 2
- [ ] Thử Odoo IAP (In-App Purchase) — 25% commission, thấp hơn

**Ngày 129-135: Đánh giá giữa kỳ**

**METRICS THEO DÕI PHASE 3:**
| Metric | Target | Cảnh báo |
|--------|--------|----------|
| Tổng purchases (cả 2 module) | ≥ 5 | < 2 |
| Repeat purchase rate | ≥ 10% | < 5% |
| MRR (Monthly Recurring Revenue) | ≥ €100 | < €50 |
| Store Quality Score | 5/5 | < 4/5 |
| Số version hỗ trợ | ≥ 2 (18+19) | Chỉ 1 version |

**Decision point cuối Phase 3:**
- Nếu MRR ≥ €200 → tiếp tục Phase 4 (scale)
- Nếu MRR < €100 → cần pivot hoặc chấp nhận đây là side-income

---

## Phase 4: Scale (Ngày 136-180)

### Tuần 20-22: Xây portal riêng (Ngày 136-155)

**Ngày 136-145: Tự host distribution**
- [ ] Set up website + license key server
- [ ] Implement license validation (domain check, expiry)
- [ ] Import existing customers từ Odoo Store

**Ngày 146-150: Pricing restructure**
- [ ] Giữ giá Odoo Store bằng hoặc thấp hơn (vì price parity rule)
- [ ] Thêm subscription model trên portal riêng (€X/tháng thay vì one-time)
- [ ] Bundle support contract

**Ngày 151-155: Dual channel**
- [ ] Odoo Store = lead generation (giữ giá cao để không phá kênh partner)
- [ ] Portal riêng = direct sales (giữ 100% margin)

### Tuần 23-25: Mở rộng (Ngày 156-175)

**Ngày 156-165: Product line**
- [ ] Module thứ 3 (có thể là AI integration — hot trend 2026)
- [ ] Nếu có partner → offer white-label (họ bán lại dưới brand của họ)

**Ngày 166-175: Channel mở rộng**
- [ ] Viindoo Marketplace (hỗ trợ VND, cùng 30% commission)
- [ ] Gumroad (cho module Odoo, ít competition hơn)

### Tuần 26: Đánh giá tổng kết (Ngày 176-180)

**Ngày 176-180: Review 180 ngày**
- [ ] Tổng kết MRR, total revenue, total downloads
- [ ] ROI thời gian: số giờ bỏ ra / thu nhập
- [ ] Quyết định: full-time hay keep side-project?

**METRICS THEO DÕI PHASE 4:**
| Metric | Target | Cảnh báo |
|--------|--------|----------|
| MRR portal riêng | ≥ €200 | < €50 → giữ nguyên Odoo Store |
| Tổng MRR (store + portal) | ≥ €400 | < €200 |
| Số module đang bán | ≥ 3 | < 2 |
| Margin (portal vs store) | 100% vs 70% | - |
| Tỉ lệ churn | < 10%/tháng | > 20% → support issue |

---

## Bảng Dashboard (Check hàng tuần)

In ra hoặc copy vào file riêng, check mỗi Chủ nhật:

```
Tuần: ___

Downloads (free): ___ / target ___
Purchases (paid): ___ / target ___
MRR (€): ___ / target ___
Store Quality Score: __/5
Rating: ___
Số module trên store: ___
GitHub stars: ___

Vấn đề tuần này:
- [ ] Bug cần fix: ___
- [ ] Support ticket pending: ___
- [ ] Marketing đã làm: ___

Quyết định tuần tới:
_________________________________
```

---

## Chiến lược Pivot (khi metric fail)

| Tình huống | Diagnostic | Hành động |
|-----------|-----------|-----------|
| Downloads nhiều, purchases 0 | Giá quá cao, hoặc free module đã đủ tốt | Hạ giá, hoặc giới hạn tính năng free |
| Cả downloads lẫn purchases đều 0 | Sai niche, sai marketing | Pivot niche (Phase 0) |
| Có purchase, rating thấp | Bug, thiếu tính năng | Fix ngay, hỏi khách |
| Rating cao, ít purchase | Marketing yếu | Tăng content, outreach |
| Có purchase, không repeat | Module một lần, không có lý do mua thêm | Thêm subscription/add-on |
| Revenue ổn nhưng không scale được | Chạm trần niche | Mở rộng sang niche liên quan |

---

## Link hữu ích

- Submit module: https://apps.odoo.com/apps/upload
- Vendor Guidelines: https://apps.odoo.com/apps/vendor-guidelines
- FAQ: https://apps.odoo.com/apps/faq
- App Dashboard: https://apps.odoo.com/apps/dashboard
- Odoo Dev Docs: https://www.odoo.com/documentation/master/developer.html
- OCA GitHub: https://github.com/OCA
- Viindoo Marketplace: https://viindoo.com/vi/repo_upload
- Market intelligence (Apify): https://apify.com/foxpink/odoo-apps-market-intelligence
- Odoo Affiliate Program: https://www.odoo.com/affiliate (10% referral)
