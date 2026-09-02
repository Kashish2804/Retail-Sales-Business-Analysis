# Retail Sales & Business Performance Analysis Dashboard

## Project Overview
This project analyzes a retail/e-commerce sales dataset and converts raw
transactional data into KPIs, trend analysis, visualizations, and a
spreadsheet dashboard, ending in business-oriented insights and
recommendations. It was built to satisfy the Beginner-Level requirements of
a Data Analyst internship, focused on descriptive analytics and spreadsheet
analysis (no machine learning or predictive modeling).

## Business Problem
How is the retail business performing, which products, categories, and
regions are driving revenue and profit, and where are there opportunities
for improvement? See `documentation/methodology.md` for the full set of
supporting questions this project answers.

## Dataset
- **Source:** Synthetic — generated to mirror a realistic retail/e-commerce
  export. This is explicitly disclosed; no real transactional or customer
  data was used.
- **Records:** 2,233 raw rows → 2,189 after cleaning
- **Time period:** January 2024 – March 2025 (15 months)
- **Key columns:** Order ID, Order Date, Customer ID/Name, Region, City,
  Category, Sub-Category, Product Name, Quantity, Unit Price, Discount,
  Sales, Profit, Payment Method
- **Business context:** 5 product categories, 4 regions, 386 unique
  customers, 5 payment methods

## Objectives
- Clean and validate a raw transactional dataset
- Calculate core business KPIs (Sales, Profit, Orders, AOV, Margin, etc.)
- Analyze performance across time, category, product, region, and customer
- Build a clean, filterable Excel dashboard
- Translate findings into evidence-based business recommendations

## Tools Used
- Microsoft Excel (`.xlsx`) — KPI formulas, aggregation tables, charts,
  dashboard with dropdown filters
- Spreadsheet formulas: `SUMIFS`, `COUNTIFS`, `SUMPRODUCT`, `INDEX`/`MATCH`
- Python (pandas) — used to generate the synthetic dataset and to perform/
  document the cleaning steps

## Data Cleaning
Started with 2,233 raw records. Removed 25 exact duplicates, 11 rows with
invalid dates, and 8 rows with invalid numeric values. Standardized
Category and Region spelling/casing. Filled missing Customer Name and
Discount values rather than dropping those rows. Final dataset: 2,189
records. Full log: `documentation/data_cleaning.md`.

## KPIs
Total Sales, Total Profit, Total Orders, Total Quantity Sold, Total
Customers, Average Order Value, Profit Margin %, Top Category, Top Product,
Best Region — all calculated with live formulas in `KPIs` sheet of the
workbook. See `documentation/methodology.md` for exact formulas.

## Analysis
- **Monthly:** Sales/Profit/Orders trend across 15 months; clear Oct–Nov
  seasonal peak, January low
- **Category:** Sales, Profit, and Margin by category — reveals a
  high-sales/low-margin pattern in Electronics
- **Product:** Top 10 by Sales, Top 10 by Profit, bottom performers
- **Regional:** Sales/Profit/Orders by region — North leads, but all four
  regions are closely matched
- **Customer:** Unique customers, repeat vs one-time buyers, top 10 by
  revenue
- **Profitability:** Category-level Sales Rank vs Margin Rank comparison,
  discount-tier impact on margin

## Dashboard
The `Dashboard` sheet (first tab) includes 6 KPI cards, 3 dropdown filters
(Year / Region / Category) that recompute the KPI cards live, and 4 charts
(monthly trend, category comparison, regional comparison, top products).

## Key Insights
See `documentation/insights.md` for all 10 insights. Highlights:
- Electronics drives the most revenue but has the lowest profit margin
  (10.1%) of any category
- Discounts above 20% consistently erode margin; the 30% tier is
  unprofitable on average (-0.6% margin)
- October–November is a clear seasonal sales peak
- 81% of customers are repeat buyers — retention, not acquisition, appears
  to be the stronger driver of this business

## Recommendations
See `documentation/recommendations.md` for all 7 recommendations, each
linked to a specific finding. Highlights: cap standard discounts at 20%,
review Electronics pricing/cost structure, shift incremental investment
toward Furniture and Home & Kitchen, and build a retention program around
the existing repeat-customer base.

## Conclusion
The business is generating healthy overall profitability (24.2% margin) on
a loyal, non-concentrated customer base, but revenue and profit are not
evenly distributed — the top-selling category and product are also the
least profitable, and heavy discounting is actively destroying margin at
the highest tiers. The recommendations above target these gaps directly.

## Project Structure
```
retail-sales-business-analysis/
├── README.md
├── data/
│   ├── raw/raw_data.csv
│   └── cleaned/cleaned_data.csv
├── analysis/
│   └── excel/Retail_Sales_Analysis.xlsx
├── dashboard/
│   └── screenshots/
├── documentation/
│   ├── data_cleaning.md
│   ├── methodology.md
│   ├── insights.md
│   └── recommendations.md
├── report/
│   └── project_report.pdf
└── presentation/
    ├── Retail_Sales_Analysis_Presentation.pptx
    └── project_summary.md
```
