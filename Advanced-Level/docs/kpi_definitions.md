# KPI Definitions — HR Attrition & Workforce Dashboard

Every KPI below is supported directly by the cleaned dataset. For each,
Tableau calculated-field syntax is given so you can paste it straight in
(Analysis → Create Calculated Field).

## Executive Summary KPIs (top of dashboard)

### 1. Total Employees (Headcount)
- **Definition:** Count of active employee records.
- **Tableau:** `COUNTD([EmployeeID])`
- **Why it matters:** Baseline denominator for every rate metric; tracked
  over time it shows workforce growth/shrinkage.

### 2. Attrition Rate
- **Definition:** % of employees whose Attrition = "Yes".
- **Tableau:** `SUM([AttritionFlag]) / COUNTD([EmployeeID])`
  (format as percentage)
- **Why it matters:** The single most important workforce-health metric —
  directly tied to replacement cost, institutional knowledge loss, and
  team disruption. Current overall value in this dataset: **~22%**.

### 3. Average Tenure (Years at Company)
- **Tableau:** `AVG([YearsAtCompany])`
- **Why it matters:** Signals workforce stability/experience; a falling
  trend alongside rising attrition indicates a retention problem
  concentrated among newer hires (worth checking via TenureBand).

### 4. Average Monthly Income
- **Tableau:** `AVG([MonthlyIncome])`
- **Why it matters:** Compensation-competitiveness proxy; cut by
  Department/JobRole it flags roles at risk of pay-driven attrition.

### 5. Average Satisfaction Index
- **Tableau:** `AVG([SatisfactionIndex])`
- **Why it matters:** Composite engagement score (job + environment +
  work-life + relationship satisfaction); an early warning indicator that
  typically moves before attrition does.

## Diagnostic / Breakdown KPIs (drill-down level)

### 6. Attrition Rate by Department
- **Tableau:** Same attrition-rate calc, with `[Department]` on rows/color.
- **Purpose:** Identifies which business function is bleeding talent.

### 7. Attrition Rate by Job Role
- **Purpose:** Pinpoints specific roles needing intervention — usually more
  actionable than department-level alone.

### 8. Attrition Rate by OverTime Status
- **Purpose:** Tests whether workload/overtime culture is a driver.
  In this dataset, employees working overtime attrite at **~30%** vs
  **~19%** for those who don't — a clear, actionable gap.

### 9. Attrition Rate by Tenure Band
- **Tableau:** Attrition-rate calc with `[TenureBand]` on rows.
- **Purpose:** Tests the "flight risk in year one" hypothesis. In this
  dataset, 0–1 year employees attrite at **~30%**, roughly double the
  4–10 year bands — classic early-tenure risk.

### 10. Headcount Distribution (Workforce Mix)
- **Tableau:** `COUNTD([EmployeeID])` with Department/JobRole/Gender on rows.
- **Purpose:** Shows where the organization's people actually sit —
  context for every other KPI.

### 11. Average Salary Hike %
- **Tableau:** `AVG([PercentSalaryHike])`
- **Purpose:** Checks whether pay growth is keeping pace across roles,
  useful alongside attrition-by-income-band.

### 12. High-Risk Segment Count
- **Definition:** Employees who are simultaneously OverTime = Yes,
  SatisfactionIndex below the org average, and TenureBand = "0-1 yrs".
- **Tableau (calc field `IsHighRisk`):**
  ```
  IF [OverTime] = "Yes"
     AND [SatisfactionIndex] < {AVG([SatisfactionIndex])}
     AND [TenureBand] = "0-1 yrs"
  THEN 1 ELSE 0 END
  ```
- **Purpose:** A single actionable "watch list" number for HR leadership —
  concrete, not just a rate.

## KPI → Business Question Map

| KPI | Business Question Answered |
|---|---|
| Attrition Rate (overall + trend) | Is our attrition problem getting better or worse? |
| Attrition by Department/Role | Where should HR focus first? |
| Attrition by OverTime | Is workload culture driving people out? |
| Attrition by Tenure Band | Are we losing people early (onboarding issue) or late (career-growth issue)? |
| Avg Income / Salary Hike by role | Is pay a plausible driver of attrition? |
| Satisfaction Index | Is engagement declining before people leave? |
| High-Risk Segment Count | Who should HR proactively reach out to *this month*? |
