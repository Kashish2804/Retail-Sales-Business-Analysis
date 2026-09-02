"""
generate_raw_data.py
Generates a synthetic, IBM-HR-Analytics-style employee dataset for the
Advanced Data Analyst project (attrition / workforce analytics).

The data is fully synthetic but built with realistic distributions and
correlations (e.g., low satisfaction + overtime + low income -> higher
attrition probability), so that the KPIs and insights built on top of it
are believable.

Deliberate data-quality issues are injected on purpose (missing values,
duplicate rows, inconsistent category spellings, wrong dtypes, stray
whitespace) so the cleaning stage of the project has real, documentable
work to do -- mirroring what a real HR export usually looks like.
"""

import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

N = 1650  # sufficiently rich for an executive dashboard

departments = ["Sales", "Research & Development", "Human Resources"]
dept_weights = [0.34, 0.55, 0.11]

job_roles_by_dept = {
    "Sales": ["Sales Executive", "Sales Representative", "Manager"],
    "Research & Development": [
        "Research Scientist", "Laboratory Technician", "Manufacturing Director",
        "Healthcare Representative", "Research Director", "Manager"
    ],
    "Human Resources": ["Human Resources", "Manager", "HR Business Partner"],
}

education_fields = ["Life Sciences", "Medical", "Marketing", "Technical Degree",
                     "Human Resources", "Other"]
edu_field_weights = [0.34, 0.27, 0.12, 0.15, 0.06, 0.06]

marital = ["Single", "Married", "Divorced"]
marital_weights = [0.32, 0.46, 0.22]

business_travel = ["Travel_Rarely", "Travel_Frequently", "Non-Travel"]
travel_weights = [0.71, 0.19, 0.10]

genders = ["Male", "Female"]

rows = []
for i in range(1, N + 1):
    dept = rng.choice(departments, p=dept_weights)
    role = rng.choice(job_roles_by_dept[dept])
    age = int(np.clip(rng.normal(37, 9), 18, 60))
    gender = rng.choice(genders)
    edu = int(rng.choice([1, 2, 3, 4, 5], p=[0.06, 0.20, 0.38, 0.27, 0.09]))
    edu_field = rng.choice(education_fields, p=edu_field_weights)
    marital_status = rng.choice(marital, p=marital_weights)
    distance = int(np.clip(rng.exponential(8), 1, 29))
    joblevel = int(rng.choice([1, 2, 3, 4, 5], p=[0.36, 0.28, 0.18, 0.10, 0.08]))
    total_working_years = int(np.clip(age - rng.integers(18, 25), 0, 40))
    years_at_company = int(np.clip(rng.integers(0, total_working_years + 1)
                                    if total_working_years > 0 else 0, 0, 40))
    years_in_role = int(np.clip(years_at_company - rng.integers(0, 4), 0, years_at_company))
    years_since_promo = int(np.clip(rng.integers(0, min(years_at_company, 15) + 1), 0, 15))
    years_with_mgr = int(np.clip(years_at_company - rng.integers(0, 4), 0, years_at_company))
    num_companies = int(rng.integers(0, 10))
    training_times = int(rng.integers(0, 7))
    stock_option = int(rng.choice([0, 1, 2, 3], p=[0.42, 0.38, 0.14, 0.06]))
    overtime = rng.choice(["Yes", "No"], p=[0.28, 0.72])
    percent_hike = int(np.clip(rng.normal(15, 4), 11, 25))
    perf_rating = int(rng.choice([3, 4], p=[0.85, 0.15]))
    job_involvement = int(rng.choice([1, 2, 3, 4], p=[0.09, 0.26, 0.51, 0.14]))
    job_satisfaction = int(rng.choice([1, 2, 3, 4], p=[0.20, 0.20, 0.30, 0.30]))
    env_satisfaction = int(rng.choice([1, 2, 3, 4], p=[0.19, 0.21, 0.30, 0.30]))
    worklife = int(rng.choice([1, 2, 3, 4], p=[0.06, 0.24, 0.55, 0.15]))
    relationship_sat = int(rng.choice([1, 2, 3, 4], p=[0.18, 0.22, 0.30, 0.30]))

    base_income = 2500 + joblevel * 2200 + total_working_years * 90
    monthly_income = int(np.clip(rng.normal(base_income, 900), 1009, 20000))

    # Attrition probability driven by realistic factors
    risk = 0.06
    if overtime == "Yes":
        risk += 0.14
    if job_satisfaction <= 2:
        risk += 0.10
    if env_satisfaction <= 2:
        risk += 0.06
    if worklife <= 2:
        risk += 0.06
    if monthly_income < 3500:
        risk += 0.10
    if years_at_company <= 1:
        risk += 0.10
    if distance > 15:
        risk += 0.05
    if age < 26:
        risk += 0.05
    if dept == "Sales":
        risk += 0.03
    risk = min(risk, 0.85)
    attrition = rng.choice(["Yes", "No"], p=[risk, 1 - risk])

    rows.append({
        "EmployeeID": 10000 + i,
        "Age": age,
        "Gender": gender,
        "MaritalStatus": marital_status,
        "Department": dept,
        "JobRole": role,
        "JobLevel": joblevel,
        "Education": edu,
        "EducationField": edu_field,
        "DistanceFromHome": distance,
        "BusinessTravel": rng.choice(business_travel, p=travel_weights),
        "MonthlyIncome": monthly_income,
        "PercentSalaryHike": percent_hike,
        "StockOptionLevel": stock_option,
        "OverTime": overtime,
        "TotalWorkingYears": total_working_years,
        "YearsAtCompany": years_at_company,
        "YearsInCurrentRole": years_in_role,
        "YearsSinceLastPromotion": years_since_promo,
        "YearsWithCurrManager": years_with_mgr,
        "NumCompaniesWorked": num_companies,
        "TrainingTimesLastYear": training_times,
        "PerformanceRating": perf_rating,
        "JobInvolvement": job_involvement,
        "JobSatisfaction": job_satisfaction,
        "EnvironmentSatisfaction": env_satisfaction,
        "WorkLifeBalance": worklife,
        "RelationshipSatisfaction": relationship_sat,
        "Attrition": attrition,
    })

df = pd.DataFrame(rows)

# ---------------------------------------------------------------------
# Inject realistic data-quality problems on purpose
# ---------------------------------------------------------------------
df_messy = df.copy()

# 1) Inconsistent category spellings / casing
dept_variants = {
    "Sales": ["Sales", "sales", "SALES", "Sales "],
    "Research & Development": ["Research & Development", "R&D", "research & development"],
    "Human Resources": ["Human Resources", "HR", "human resources"],
}
idx = rng.choice(df_messy.index, size=140, replace=False)
for i in idx:
    d = df_messy.loc[i, "Department"]
    df_messy.loc[i, "Department"] = rng.choice(dept_variants[d])

idx = rng.choice(df_messy.index, size=90, replace=False)
for i in idx:
    val = df_messy.loc[i, "OverTime"]
    df_messy.loc[i, "OverTime"] = rng.choice([val, val.lower(), val.upper(), f" {val}"])

# 2) Missing values scattered across several columns
for col, frac in [("MonthlyIncome", 0.02), ("JobSatisfaction", 0.03),
                   ("EnvironmentSatisfaction", 0.025), ("YearsSinceLastPromotion", 0.02),
                   ("EducationField", 0.015), ("Age", 0.01)]:
    idx = rng.choice(df_messy.index, size=int(len(df_messy) * frac), replace=False)
    df_messy.loc[idx, col] = np.nan

# 3) Duplicate rows (exact duplicates of existing employees)
dupes = df_messy.sample(25, random_state=7)
df_messy = pd.concat([df_messy, dupes], ignore_index=True)

# 4) Wrong data types (numbers stored as text with stray characters)
df_messy["MonthlyIncome"] = df_messy["MonthlyIncome"].astype(object)
idx = rng.choice(df_messy.index, size=60, replace=False)
df_messy.loc[idx, "MonthlyIncome"] = df_messy.loc[idx, "MonthlyIncome"].apply(
    lambda x: f"${int(x):,}" if pd.notna(x) else x
)

df_messy["DistanceFromHome"] = df_messy["DistanceFromHome"].astype(object)
idx = rng.choice(df_messy.index, size=40, replace=False)
df_messy.loc[idx, "DistanceFromHome"] = df_messy.loc[idx, "DistanceFromHome"].apply(
    lambda x: f"{x} km"
)

# 5) Invalid / out-of-range values
idx = rng.choice(df_messy.index, size=8, replace=False)
df_messy.loc[idx, "Age"] = -1

idx = rng.choice(df_messy.index, size=5, replace=False)
df_messy.loc[idx, "JobSatisfaction"] = 9

# 6) Extra unnecessary / constant columns (common in real HR exports)
df_messy["EmployeeCount"] = 1
df_messy["Over18"] = "Y"
df_messy["StandardHours"] = 80

# 7) Stray whitespace in text fields
idx = rng.choice(df_messy.index, size=50, replace=False)
df_messy.loc[idx, "JobRole"] = df_messy.loc[idx, "JobRole"].apply(lambda x: f"  {x}  ")

# Shuffle rows so duplicates aren't conveniently at the bottom
df_messy = df_messy.sample(frac=1, random_state=1).reset_index(drop=True)

df_messy.to_csv("/home/claude/hr_project/employee_data_raw.csv", index=False)
print("Rows:", len(df_messy))
print(df_messy.head())
