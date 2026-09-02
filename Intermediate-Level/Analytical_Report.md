# Superstore Sales Analysis — Analytical Report

## 1. Executive Summary

This project analyzes a retail transactions dataset (798 customers, 9,800 orders, 3 years:
2023–2025) to understand customer behaviour, revenue drivers, product performance, seasonal
trends, and regional differences.

**Most important findings:**
- Revenue is heavily concentrated: the top 10% of customers generate **30.7%** of total revenue.
- Repeat customers dominate the business — they make up the large majority of the customer base
  and account for **99.9%** of total revenue, averaging **$42,033** in lifetime revenue versus
  **$2,687** for one-time buyers.
- **Technology** is the leading category by revenue ($21.7M), while **Art** supplies is the
  weakest sub-category ($208K).
- Revenue grew sharply from 2023 to 2024 (+196%) and then leveled off in 2025 (+5.7%), with
  **20.5%** of annual revenue landing in November–December.
- **East** is the strongest region ($8.85M) and **Central** the weakest ($7.50M).
- **21.1%** of customers have been inactive for 180+ days, representing **$3.36M** in
  historical revenue at risk of not repeating.

**Most important recommendations:** protect top-decile customers with a retention program,
launch a targeted re-engagement campaign for high-value inactive customers, check category
profit margins before further investment, investigate the Central region's underperformance,
and plan inventory/marketing around the Nov–Dec seasonal peak.

## 2. Business Context

The dataset represents order-line-level transactions for a multi-category retailer (Furniture,
Office Supplies, Technology) selling to Consumer, Corporate, and Home Office segments across
four US regions. The business question addressed: **where is revenue coming from, which
customers and products drive it, and where are the risks and opportunities?**

## 3. Dataset Overview

- **Size:** 13,855 raw rows → 13,753 rows after cleaning (16 → 17 columns; one flag column added)
- **Time period:** January 2023 – December 2025
- **Key entities:** 798 customers, 9,800 orders, 3 product categories / 13 sub-categories, 4 regions
- **Fields:** Order/Ship dates, Customer ID/Name, Segment, Region, City, Category, Sub-Category,
  Product Name, Quantity, Discount, Sales, Profit
- **Limitations:** This is a synthetic dataset generated to mirror a realistic retail schema
  (see Section 9). Absolute dollar figures are illustrative; the analytical method transfers
  directly to a real dataset with the same structure.

## 4. Data Preparation

| Issue | Treatment | Why |
|---|---|---|
| Inconsistent `Category`/`Region` text (casing, spacing, abbreviations, e.g. `WEST`, `Centrl`) | Standardized via mapping to canonical labels | Needed for correct grouping — 12 raw variants collapsed into 3 categories / 4 regions |
| `Order Date`/`Ship Date` stored as mixed-format strings | Parsed with `pd.to_datetime(..., format='mixed')` | Required for any time-based analysis |
| `Quantity` mixed numeric/text (`"5 units"`) | Stripped suffix, coerced to numeric | Needed for correct aggregation |
| 102 exact duplicate rows | Dropped | Likely double-logged transactions; exact dupes add no information |
| 55 negative `Quantity` values | Converted to absolute value | Negative units sold is not physically meaningful; sign-flip is the more plausible explanation than deletion |
| 42 zero-`Sales` rows | Flagged (`Is_Zero_Sales`), kept but excluded from revenue calculations | Likely void/cancelled records; excluding without deleting preserves the row for order/count-level context |
| Missing `Ship Mode` (137) | Filled with the overall mode | Small fraction; mode is a reasonable default |
| Missing `City` (207) | Filled with `"Unknown"` | Region (coarser geography) remains intact; can't be reliably inferred |
| Missing `Discount` (278) | Filled with 0 | Most common and business-plausible default |
| Missing `Profit` (137) | Filled with category median | Avoids fabricating precise values while keeping rows usable |

**Derived fields created:** Order Month/Quarter/Year, order-level totals (`order_level` table),
customer-level revenue/profit/purchase count/repeat flag/value segment (`customer_level` table),
`Days_Since_Last_Purchase`, `Inactive_180d`.

## 5. Exploratory Analysis

- Total Revenue: **$32,834,111.84**
- Total Orders: **9,800** | Total Customers: **798**
- Average Order Value: **$3,350.42**
- Total Units Sold: **82,318**

![EDA Overview](chart_eda_overview.png)

## 6. Deep-Dive Analysis

### 6.1 Customer Behaviour
Repeat-purchase rate: **97.7%**. Repeat customers average **$42,033** in lifetime revenue and
**12.5** purchases, versus **$2,687** and 1 purchase for one-time buyers.

![Customer Behaviour](chart_customer_behaviour.png)

### 6.2 Revenue Contribution
The top 10% of customers generate **30.7%** of total revenue — a meaningful concentration risk.

![Revenue Concentration](chart_revenue_concentration.png)

### 6.3 Product Performance
Technology leads revenue ($21.7M, 23.9% margin), Furniture is second ($9.5M, 23.8% margin),
Office Supplies is smallest ($1.6M, 23.8% margin) but has near-identical margins across all
three — the revenue gap is a volume/price story, not a margin story. Machines, Accessories,
and Phones are the top three sub-categories; Storage, Binders, Paper, Labels, and Art are the
weakest.

![Category Revenue](chart_category_revenue.png)

### 6.4 Trend Analysis
Revenue grew from $4.6M (2023, partial ramp-up) to $13.7M (2024, +196%) to $14.5M (2025, +5.7%)
— strong initial growth that is now maturing. November + December account for **20.5%** of
annual revenue, a clear seasonal concentration.

![Monthly Trend](chart_monthly_trend.png)

### 6.5 Regional Differences
East leads on both revenue ($8.85M) and average order value ($3,497); Central is weakest on
revenue ($7.50M), despite serving a similar number of customers (199 vs. 196) to East — pointing
to a per-customer/order-value gap rather than a smaller customer base.

![Region Revenue](chart_region_revenue.png)

### 6.6 Inactivity Patterns
*This is a churn-like/inactivity analysis based on purchase recency, not a formal churn model —
the dataset has no cancellation or subscription-end field.* **21.1%** of customers have not
purchased in 180+ days, representing **$3.36M** in historical revenue.

## 7. Key Insights

1. **Revenue concentration risk:** the top 10% of customers drive 30.7% of revenue — losing a
   handful of top accounts would materially affect the business.
2. **Repeat customers are the business.** They contribute effectively all revenue and are worth
   ~16x a one-time buyer in lifetime value. This is a correlation — high-value customers may
   simply be more inclined to return, rather than repeat purchasing itself causing higher value.
3. **Category revenue gaps are driven by volume/price mix, not margin** — all three categories
   sit within a percentage point of each other on profit margin (~23.8%).
4. **Seasonality is real and concentrated** — a fifth of annual revenue lands in just two months.
5. **Central region underperforms East on revenue despite a comparable customer count**,
   suggesting a per-customer engagement or order-value gap worth investigating rather than a
   market-size explanation.
6. **A fifth of the customer base is inactive**, and that inactivity is tied to a non-trivial
   amount of historical revenue.

## 8. Recommendations

| Recommendation | Evidence | Addresses | Potential Outcome |
|---|---|---|---|
| Dedicated retention program for top-decile customers | Top 10% = 30.7% of revenue (6.2) | Concentration risk | Protects disproportionate revenue share |
| Re-engagement campaign targeted at high-value inactive customers | 21.1% inactive, $3.36M at-risk revenue (6.6) | Revenue recovery | Recovers some of the at-risk revenue before it's fully lost |
| Evaluate margin before scaling Technology further | Near-identical ~23.8% margins across categories (6.3) | Investment prioritization | Avoids over-investing in volume without a margin payoff |
| Investigate Central region's customer/order-value gap | Similar customer count, lower revenue than East (6.5) | Regional underperformance | Identifies a fixable operational or marketing gap |
| Plan inventory & marketing around Nov–Dec | 20.5% of annual revenue in 2 months (6.4) | Seasonal demand | Reduces stockout/missed-promotion risk |
| Cross-sell/upsell push right after first purchase | One-time buyers average $2,687 vs. $42,033 for repeat (6.1) | Low conversion to repeat | Moves more customers into the high-value cohort |

## 9. Limitations

- Dataset is synthetic, generated to mirror a realistic retail schema and messiness profile;
  absolute dollar values are illustrative rather than real historical figures.
- Missing `Profit` values were imputed at the category-median level, slightly smoothing true
  product-level profit variation.
- Inactivity threshold (180 days) is a reasonable default, not a business-validated churn
  definition — no cancellation/subscription field exists in the data to define churn precisely.
- No formal statistical significance testing was applied to the regional/category differences
  described — they are notable in magnitude but not tested for statistical significance.
