# HR Attrition & Workforce Analytics Dashboard (Advanced-Level Project)

## 1. Project Overview

An executive-style, interactive Tableau dashboard analyzing employee
attrition and workforce health for a mid-size organization, built on an
IBM-HR-Analytics-style dataset (synthetic, generated to match the real
dataset's structure and distributions).

**Audience:** CHRO / VP of People, department heads
**Primary business question:** *Where are we losing people, why, and what
should we do about it?*

## 2. Repository Structure

```
hr-attrition-dashboard/
├── data/
│   ├── employee_data_raw.csv          # raw, uncleaned export (with injected issues)
│   └── employee_data_clean.csv        # cleaned, transformation-ready dataset
├── scripts/
│   ├── generate_raw_data.py           # (optional) how the synthetic raw data was built
│   └── clean_data.py                  # cleaning & transformation pipeline
├── docs/
│   ├── cleaning_log.txt               # auto-generated log of every cleaning step
│   ├── kpi_definitions.md             # KPI catalogue with formulas & business purpose
│   ├── tableau_build_guide.md         # step-by-step dashboard build instructions
│   └── insights_and_recommendations.md
├── dashboard/
│   └── HR_Attrition_Dashboard.twbx    # (you add this after building in Tableau)
└── README.md
```

## 3. Dataset

- **Source:** Synthetic dataset generated to mirror the structure, fields, and
  realistic distributions of the IBM HR Analytics Employee Attrition dataset.
- **Grain:** One row per employee.
- **Size:** 1,650 employees (post-cleaning), 34 columns.
- **Key dimensions:** Department, JobRole, Gender, Age/AgeGroup, MaritalStatus,
  BusinessTravel, OverTime, TenureBand, IncomeBand.
- **Key measures:** MonthlyIncome, YearsAtCompany, JobSatisfaction,
  EnvironmentSatisfaction, WorkLifeBalance, PerformanceRating, AttritionFlag.
- **Limitation:** Being synthetic, correlations were deliberately built in
  (overtime, low satisfaction, low tenure, and low income raise attrition
  probability) to mirror realistic workforce patterns; absolute figures should
  be read as illustrative, not as a real company's actuals.

## 4. Data Cleaning & Transformation (summary)

Full step-by-step log in `docs/cleaning_log.txt`. Highlights:

| Issue | Fix |
|---|---|
| 19 exact duplicate rows + 6 duplicate EmployeeIDs | Dropped |
| 3 constant, non-informative columns (EmployeeCount, Over18, StandardHours) | Dropped |
| Inconsistent category spelling ("R&D", "sales ", "HR") | Standardized to 3 clean Department values |
| Mixed-case / whitespace in OverTime, JobRole | Trimmed and standardized |
| MonthlyIncome stored as text with "$" and commas | Converted to numeric |
| DistanceFromHome stored as text with " km" suffix | Converted to numeric |
| Invalid Age values (negative) | Treated as missing, imputed |
| Invalid JobSatisfaction values (out of 1-4 scale) | Treated as missing, imputed |
| Missing values in 6 columns | Median (numeric) / mode (categorical) imputation |

**Derived fields created for the dashboard:**
- `AttritionFlag` — numeric 1/0 version of Attrition, needed for rate calculations
- `AgeGroup`, `TenureBand`, `IncomeBand` — binned dimensions for cleaner filtering/visuals
- `SatisfactionIndex` — average of the four satisfaction/engagement scores, a single
  composite measure of employee sentiment

## 5. How to Reproduce

```bash
pip install pandas numpy
python scripts/generate_raw_data.py   # optional — recreates the raw file
python scripts/clean_data.py          # cleans data/employee_data_raw.csv
```

Then open Tableau Desktop/Public and connect to `data/employee_data_clean.csv`
following `docs/tableau_build_guide.md`.

## 6. KPIs, Dashboard Design, Insights, Recommendations

See:
- `docs/kpi_definitions.md`
- `docs/tableau_build_guide.md`
- `docs/insights_and_recommendations.md`

## 7. Deliverables Checklist (per project brief)

- [x] Cleaned/transformed dataset + reproducible transformation script
- [x] Dashboard documentation (this README + docs/)
- [x] Business insights
- [x] Decision-oriented recommendations
- [ ] Tableau workbook (.twbx) — build following the guide, then add to `dashboard/`
- [ ] 3–5 min recorded walkthrough video [Watch the video here](https://drive.google.com/file/d/1q3k0CwIwhI1tgamvMlbCwQKSl9380wmF/view?usp=sharing)
