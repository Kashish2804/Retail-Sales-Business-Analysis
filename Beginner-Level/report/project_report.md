---
title: "Retail Sales & Business Performance Analysis"
subtitle: "Beginner-Level Data Analyst Internship Project"
---

# 1. Introduction
This report documents a Beginner-Level Data Analyst internship project that
analyzes a retail/e-commerce sales dataset and converts raw transactional
data into KPIs, trend analysis, visualizations, a spreadsheet dashboard, and
business recommendations.

# 2. Business Problem
**Main question:** How is the retail business performing, and which
products, categories, and regions are driving revenue and profit — and
where are the opportunities for improvement?

Thirteen supporting questions guided the analysis, covering total revenue
and profit, order and customer counts, average order value, monthly
performance, category and product performance, regional performance, and
customer contribution. The full list is in `documentation/methodology.md`.

# 3. Dataset Description
A synthetic retail dataset was generated to mirror a realistic e-commerce
export — this is explicitly disclosed, as no real transactional data was
used. It spans **January 2024 to March 2025** (15 months), with 2,233 raw
transaction records across 5 categories (Electronics, Furniture, Clothing,
Home & Kitchen, Stationery), 4 regions (North, South, East, West), and 386
unique customers.

# 4. Data Cleaning
The raw export contained realistic data-quality issues: duplicate rows,
missing values, inconsistent category/region spelling, invalid dates, and
a small number of invalid numeric entries. Each issue was inspected,
documented, and resolved:

- **25** exact duplicate rows removed
- **11** rows with invalid/unparseable dates removed
- **8** rows with invalid numeric values (Quantity or Unit Price ≤ 0) removed
- Category and Region spelling/casing standardized
- **44** missing Customer Name values filled with "Unknown Customer" (row kept — still a valid transaction)
- **66** missing Discount values filled with 0% (no discount recorded = no discount applied)

Final cleaned dataset: **2,189 records**. Full documentation:
`documentation/data_cleaning.md`.

# 5. Methodology
Workflow: Business Problem → Dataset → Inspection → Cleaning →
Transformation → KPIs → Monthly/Category/Product/Regional/Customer/
Profitability Analysis → Dashboard → Insights → Recommendations → Report.

Derived columns added during transformation: Year, Month, Month Number,
Year-Month, Profit Margin %, Order Value.

All KPIs and analysis tables were built as live Excel formulas
(`SUMIFS`, `COUNTIFS`, `SUMPRODUCT`, `INDEX`/`MATCH`) referencing the
Cleaned Data sheet directly, so the workbook recalculates automatically if
the underlying data changes.

# 6. KPI Definitions
| KPI | Definition | Value |
|---|---|---|
| Total Sales | Sum of all Sales | ₹91,12,531 |
| Total Profit | Sum of all Profit | ₹22,05,548 |
| Total Orders | Count of Order IDs | 2,189 |
| Total Quantity Sold | Sum of Quantity | 3,029 |
| Total Customers | Unique Customer IDs | 386 |
| Average Order Value | Total Sales ÷ Total Orders | ₹4,163 |
| Profit Margin % | Total Profit ÷ Total Sales | 24.2% |
| Top Category (Sales) | — | Electronics |
| Top Product (Sales) | — | Bluetooth Speaker |
| Best Region (Sales) | — | North |

# 7. Analysis
**Monthly:** October 2024 and November 2024 were the two strongest months
(₹8.37L and ₹7.43L in sales); January was consistently the weakest month
in both years, consistent with a festive-season demand pattern.

**Category:** Electronics led in sales (₹27.68L) but had the lowest margin
(10.1%). Stationery had the smallest sales base (₹9.07L) but the highest
margin (48.6%) — a clear demonstration that sales volume and profitability
do not move together.

**Product:** Bluetooth Speaker was the top seller by revenue but returned a
below-average 9.9% margin. USB-C Charger was weak on both sales and margin
(3.2%) — the only product weak on both dimensions simultaneously.

**Regional:** All four regions performed within a narrow band; North led
narrowly on both sales and margin. East had a smaller customer base rather
than a profitability problem.

**Customer:** 314 of 386 customers (81%) were repeat buyers. Revenue was
not concentrated — the top customer contributed under 2% of total sales.

**Profitability:** Discount depth was directly correlated with declining
margin, turning negative (-0.6%) at the 30% discount tier.

# 8. Dashboard Explanation
The workbook's `Dashboard` sheet (first tab) presents six KPI cards (Total
Sales, Total Profit, Total Orders, Total Customers, Average Order Value,
Profit Margin %), three dropdown filters (Year, Region, Category) that
recompute the KPI cards live, and four charts: a monthly Sales & Profit
trend line, a Category Sales & Profit comparison, a Regional Sales
comparison, and a Top 10 Products by Sales bar chart.

# 9. Key Findings
1. Electronics drives the most revenue but returns the lowest margin of any category.
2. High sales does not equal high profit — confirmed directly by category ranking.
3. October–November is a clear seasonal sales peak.
4. Discounting above 20% consistently erodes profit margin; 30% is unprofitable on average.
5. USB-C Charger underperforms on both sales and margin.
6. Bluetooth Speaker, the top seller, is a below-average earner.
7. Regional performance is balanced — no underperforming region.
8. 81% of customers are repeat buyers — retention appears to be the stronger revenue driver.
9. Revenue is not concentrated in a small number of customers.
10. Furniture and Home & Kitchen offer the best balance of sales volume and margin.

Full detail with evidence: `documentation/insights.md`.

# 10. Recommendations
1. Cap routine promotional discounts at 20%.
2. Review Electronics pricing and cost structure.
3. Reassess USB-C Charger's place in the catalog.
4. Shift incremental marketing/inventory investment toward Furniture and Home & Kitchen.
5. Plan inventory and staffing ahead of the October–November peak.
6. Build a retention program around the existing repeat-customer base.
7. Investigate the one-time-buyer segment to understand non-return reasons.

Full detail with supporting evidence: `documentation/recommendations.md`.

# 11. Conclusion
The business shows healthy overall profitability (24.2% margin) on a loyal,
well-distributed customer base. However, performance is uneven beneath the
surface: the top category and top product by revenue are both
below-average earners, and heavy discounting is actively destroying margin
at the highest tiers. The recommendations in this report are aimed
directly at these gaps — correcting margin erosion, rebalancing category
investment, and reinforcing the retention pattern that already drives most
of the business.

---
*Dataset is synthetic and was generated for this project; all figures are
internally consistent and traceable to the accompanying Excel workbook.*
