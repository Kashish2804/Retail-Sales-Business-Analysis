# Tableau Build Guide — HR Attrition & Workforce Dashboard

You'll need **Tableau Desktop** or **Tableau Public** (free) installed.
This guide builds a 3-page executive dashboard from `employee_data_clean.csv`.

## Step 0 — Connect to Data

1. Open Tableau → **Connect → Text File** → select `employee_data_clean.csv`.
2. On the data source screen, confirm data types:
   - `EmployeeID` → String (not a measure — right-click the pill → Convert to Dimension)
   - `Age`, `MonthlyIncome`, `YearsAtCompany`, satisfaction scores → Number
   - `Attrition`, `Department`, `JobRole`, `Gender`, `OverTime` → String
   - `AgeGroup`, `TenureBand`, `IncomeBand` → String (they're already binned text)
3. Go to Sheet 1.

## Step 1 — Build the Calculated Fields

Analysis → Create Calculated Field. Add each one from `kpi_definitions.md`:
`Attrition Rate`, `IsHighRisk`. (`AttritionFlag`, `SatisfactionIndex`,
`AgeGroup`, `TenureBand`, `IncomeBand` already exist as columns.)

## Step 2 — Page 1: Executive Summary

**Layout:** 4–5 KPI cards across the top, 2 charts below.

1. **KPI cards:** New sheet per metric — Total Employees, Attrition Rate,
   Avg Tenure, Avg Monthly Income, Avg Satisfaction Index. For each: drag the
   measure to Text on the Marks card, use a large font (28–36pt), sheet
   title = metric name. Use "Text Table" mark type for a clean big-number card.
2. **Attrition Trend/Comparison chart:** Bar chart — `Department` on Columns,
   `Attrition Rate` on Rows, color by Department. Sort descending.
3. **Attrition by OverTime:** Bar chart — `OverTime` on Columns, `Attrition
   Rate` on Rows. This is your headline "workload culture" chart.
4. Assemble on a **Dashboard** (not a Sheet): New Dashboard → drag the 5 KPI
   sheets into a horizontal container at top, the 2 charts below in a
   horizontal container. Add a dashboard title: "Workforce Overview".

## Step 3 — Page 2: Key Drivers & Areas of Concern

1. **Attrition by Job Role:** Horizontal bar chart, `JobRole` on Rows sorted
   by `Attrition Rate` descending — immediately shows the riskiest roles.
2. **Attrition by Tenure Band:** Bar chart, `TenureBand` on Columns
   (order manually: 0-1, 2-3, 4-6, 7-10, 10+), `Attrition Rate` on Rows.
3. **Satisfaction vs Attrition scatter:** Scatter plot — `SatisfactionIndex`
   (avg) on Columns, `Attrition Rate` on Rows, one mark per `JobRole` or
   `Department`, size by headcount (`COUNTD([EmployeeID])`).
4. **Income Band vs Attrition:** Bar chart, `IncomeBand` on Columns
   (order manually low→high), `Attrition Rate` on Rows.
5. Add all 4 to a second dashboard tab: "Key Drivers".

## Step 4 — Page 3: Detailed Breakdown / Watch List

1. **Employee-level table:** `EmployeeID`, `Department`, `JobRole`,
   `TenureBand`, `OverTime`, `SatisfactionIndex`, `MonthlyIncome`,
   `Attrition` as columns in a Text Table (crosstab), filtered to
   `IsHighRisk = 1` by default via a Dashboard filter action — this is
   the actionable "who to talk to" list for HR.
2. Add to a third dashboard tab: "Watch List & Detail".

## Step 5 — Interactivity (required by the brief)

On the "Workforce Overview" dashboard:
1. Add **Filters**: Department, JobRole, Gender, OverTime, AgeGroup —
   drag each field to Filters shelf on one sheet, then right-click each
   pill → **Apply to Worksheets → All Using This Data Source** so one
   filter panel controls every page.
2. Add these filters to the dashboard as quick filters (Filter icon on
   the field's dashboard card menu → "Add to All Using Related Data Sources").
3. Add a **Dashboard Action** (Dashboard → Actions → Add Action → Filter):
   clicking a bar in the "Attrition by Job Role" chart filters the
   detail table on Page 3 — this is your cross-filtering/drill-down.
4. Add a **Highlight Action** on Department across all 3 sheets so hovering
   one chart highlights the same category elsewhere.

## Step 6 — Formatting Pass (usability requirement)

- Consistent color: pick one accent color for "Attrition" bars (e.g. red/
  orange) and a neutral gray for "Retained" — keep this consistent on
  every chart.
- Titles: every chart needs a plain-English title ("Attrition Is Highest
  Among Employees Working Overtime" beats "OverTime vs Attrition Rate").
- Remove gridlines/borders you don't need; align KPI cards to a grid.
- Add a short "How to use this dashboard" text box on Page 1 explaining
  the filters and navigation between tabs.

## Step 7 — Export

- File → Save As → `.twbx` (packaged workbook, bundles the data) →
  save to `dashboard/HR_Attrition_Dashboard.twbx` in your repo.
- Optionally: Server/Tableau Public → Publish, if you want a shareable
  web link for your video walkthrough.
