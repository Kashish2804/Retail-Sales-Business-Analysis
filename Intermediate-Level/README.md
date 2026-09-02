# Superstore Sales Analysis — Intermediate Data Analyst Project

## What this is
An end-to-end Python/Pandas analysis of a retail transactions dataset: data cleaning,
feature engineering, exploratory analysis, five deep-dive business analyses (customer
behaviour, revenue contribution, product performance, trend analysis, regional differences,
plus an inactivity/churn-like view), visualizations, insights, and recommendations.

## Files
| File | Description |
|---|---|
| `generate_data.py` | Generates the synthetic raw dataset (`raw_superstore_data.csv`) |
| `raw_superstore_data.csv` | Raw dataset, as originally "received" — includes intentional messiness |
| `superstore_analysis.ipynb` | **Main deliverable.** Full analysis notebook, cleaning → insights, with executed outputs and charts |
| `cleaned_superstore_data.csv` | Cleaned, analysis-ready dataset (output of the notebook) |
| `customer_level_summary.csv` | One row per customer: revenue, purchase count, repeat flag, inactivity flag |
| `order_level_summary.csv` | One row per order: total value, profit, region, segment |
| `Analytical_Report.md` | Full written report: executive summary → limitations |
| `chart_*.png` | Exported chart images (also embedded in the notebook and report) |
| `requirements.txt` | Python dependencies |

## How to run
```bash
pip install -r requirements.txt

# (optional) regenerate the raw dataset from scratch
python generate_data.py

# run the full analysis notebook end to end
jupyter nbconvert --to notebook --execute --inplace superstore_analysis.ipynb

# or open it interactively
jupyter notebook superstore_analysis.ipynb
```

## Notebook structure
1. Import libraries
2. Load data
3. Inspect data
4. Clean data
5. Create derived fields
6. Exploratory data analysis
7. Deep-dive business analysis (customer behaviour, revenue contribution, product
   performance, trend analysis, regional differences, inactivity patterns)
8. Key insights
9. Recommendations
10. Limitations
11. Export cleaned dataset

## Notes
The raw dataset is **synthetic** — generated with `generate_data.py` to mirror the structure,
scale, and realistic messiness (missing values, duplicates, inconsistent categories, mixed
date formats, impossible values) of a real "Superstore"-style retail dataset. To reuse this
project on real data, replace `raw_superstore_data.csv` with your own file (same column
schema) and re-run the notebook — the cleaning and analysis code will need column-name
adjustments if your schema differs.
