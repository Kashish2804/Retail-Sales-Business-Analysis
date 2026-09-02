# Methodology

## Workflow
Business Problem → Dataset → Inspection → Cleaning → Transformation → KPIs →
Monthly / Category / Product / Regional / Customer / Profitability Analysis →
Dashboard → Insights → Recommendations → Report.

## Tools Used
- Python (pandas, numpy) — dataset generation, inspection, and cleaning logic
  (used here in place of manual spreadsheet cleaning steps; every decision is
  documented in `data_cleaning.md` exactly as it would be if done by hand in
  Excel/Google Sheets)
- Microsoft Excel (`.xlsx`, built with openpyxl, verified with LibreOffice
  recalculation) — all KPI, aggregation, and dashboard formulas
- Excel formulas: `SUMIFS`, `COUNTIFS`, `SUMPRODUCT`, `INDEX`/`MATCH`, `RANK`
- Excel charts: line chart (trend), column/bar charts (comparisons)

## Why formula-based summaries instead of native Excel PivotTables
The workbook uses `SUMIFS`/`COUNTIFS`-based summary tables rather than native
Excel PivotTable objects. Functionally these produce the same grouped
Sales/Profit/Orders/Quantity breakdowns a PivotTable would, but every value is
a transparent, auditable formula that recalculates automatically if the
Cleaned Data sheet changes — which also makes the logic easier to explain in
the video walkthrough. If preferred, these summary tables can be recreated as
native PivotTables by selecting the Cleaned Data range and inserting a
PivotTable per pivot listed in the project plan (Phase 13).

## KPI Definitions
| KPI | Formula |
|---|---|
| Total Sales | `SUM(Sales)` |
| Total Profit | `SUM(Profit)` |
| Total Orders | `COUNTA(Order ID)` |
| Total Quantity | `SUM(Quantity)` |
| Total Customers | Count of unique Customer IDs |
| Average Order Value | Total Sales ÷ Total Orders |
| Profit Margin % | Total Profit ÷ Total Sales |

## Data Cleaning
See `data_cleaning.md` for the full record-by-record log. Summary: started
with 2,233 raw rows; removed 25 exact duplicates, 11 rows with invalid/
unparseable dates, and 8 rows with invalid numeric values (non-positive
Quantity or Unit Price); standardized Category and Region spelling/casing;
filled missing Customer Name with "Unknown Customer" and missing Discount
with 0%. Final cleaned dataset: **2,189 records**.

## Analysis Scope
Monthly, Category, Product, Regional, Customer, and Profitability analysis —
each covered in its own workbook sheet with formula-driven aggregation and a
supporting chart where useful. Customer analysis is intentionally kept
beginner-level (unique customers, repeat vs one-time, top revenue
customers) — RFM segmentation and churn analysis are out of scope, reserved
for the Intermediate-level project.

## Dashboard
The Dashboard sheet is the first tab in the workbook. It contains:
- Six KPI cards (Total Sales, Total Profit, Total Orders, Total Customers,
  Average Order Value, Profit Margin %)
- Three dropdown filters (Year, Region, Category) that recompute the KPI
  cards live via `SUMPRODUCT` formulas
- Four charts: Monthly Sales & Profit trend, Sales & Profit by Category,
  Sales by Region, Top 10 Products by Sales

The filters affect the KPI cards; the charts reference the full cleaned
dataset (labelled clearly on the dashboard) so that trend shapes remain
comparable regardless of filter selection.
