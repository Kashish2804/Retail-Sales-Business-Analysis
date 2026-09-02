"""
clean_data.py
Cleans and transforms employee_data_raw.csv into employee_data_clean.csv,
ready for the Tableau dashboard.

Each step below states WHAT is being fixed and WHY, so this file doubles
as the technical backbone of the "Data Transformation" section of the
project documentation.
"""

import numpy as np
import pandas as pd

RAW_PATH = "/home/claude/hr_project/employee_data_raw.csv"
CLEAN_PATH = "/home/claude/hr_project/employee_data_clean.csv"

df = pd.read_csv(RAW_PATH)
log = []


def note(msg):
    log.append(msg)
    print(msg)


note(f"Loaded raw dataset: {df.shape[0]} rows, {df.shape[1]} columns")

# ---------------------------------------------------------------------
# 1. Remove duplicate records
# ---------------------------------------------------------------------
before = len(df)
df = df.drop_duplicates(subset=[c for c in df.columns if c != "EmployeeID"])
note(f"Removed {before - len(df)} exact duplicate employee records")

# Also drop duplicate EmployeeIDs if any slipped through with different data
before = len(df)
df = df.drop_duplicates(subset="EmployeeID", keep="first")
note(f"Removed {before - len(df)} duplicate EmployeeIDs")

# ---------------------------------------------------------------------
# 2. Remove unnecessary / constant columns
#    (EmployeeCount, Over18, StandardHours carry a single value for every
#    row in this export and add no analytical value)
# ---------------------------------------------------------------------
constant_cols = [c for c in ["EmployeeCount", "Over18", "StandardHours"] if c in df.columns]
df = df.drop(columns=constant_cols)
note(f"Dropped constant/non-informative columns: {constant_cols}")

# ---------------------------------------------------------------------
# 3. Standardize inconsistent categorical values
# ---------------------------------------------------------------------
df["Department"] = df["Department"].str.strip().str.lower().map({
    "sales": "Sales",
    "research & development": "Research & Development",
    "r&d": "Research & Development",
    "human resources": "Human Resources",
    "hr": "Human Resources",
})
note("Standardized 'Department' spelling/casing variants (e.g. 'R&D', 'sales ') into 3 clean categories")

df["OverTime"] = df["OverTime"].astype(str).str.strip().str.capitalize()
note("Standardized 'OverTime' to consistent 'Yes'/'No' capitalization, trimmed whitespace")

df["JobRole"] = df["JobRole"].str.strip()
note("Trimmed stray leading/trailing whitespace from 'JobRole'")

# ---------------------------------------------------------------------
# 4. Fix incorrect data types (numbers stored as text)
# ---------------------------------------------------------------------
df["MonthlyIncome"] = (
    df["MonthlyIncome"].astype(str)
    .str.replace(r"[$,]", "", regex=True)
    .replace("nan", np.nan)
    .astype(float)
)
note("Converted 'MonthlyIncome' from mixed text/currency-formatted strings to numeric")

df["DistanceFromHome"] = (
    df["DistanceFromHome"].astype(str)
    .str.replace(" km", "", regex=False)
    .replace("nan", np.nan)
    .astype(float)
)
note("Converted 'DistanceFromHome' from mixed text ('12 km') to numeric")

# ---------------------------------------------------------------------
# 5. Fix invalid / out-of-range values
# ---------------------------------------------------------------------
invalid_age = (df["Age"] < 18) | (df["Age"] > 65)
note(f"Found {invalid_age.sum()} rows with invalid Age (<18 or >65) -> set to missing, then imputed")
df.loc[invalid_age, "Age"] = np.nan

invalid_sat = df["JobSatisfaction"] > 4
note(f"Found {invalid_sat.sum()} rows with JobSatisfaction outside valid 1-4 scale -> set to missing")
df.loc[invalid_sat, "JobSatisfaction"] = np.nan

# ---------------------------------------------------------------------
# 6. Handle missing values
#    Strategy: numeric columns -> median imputation (robust to outliers);
#    the one categorical column with gaps (EducationField) -> mode.
#    Median/mode chosen over mean to avoid distortion from skewed pay data.
# ---------------------------------------------------------------------
numeric_impute_cols = ["MonthlyIncome", "JobSatisfaction", "EnvironmentSatisfaction",
                        "YearsSinceLastPromotion", "Age"]
for col in numeric_impute_cols:
    n_missing = df[col].isna().sum()
    if n_missing:
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)
        note(f"Imputed {n_missing} missing '{col}' values with median ({median_val})")

if df["EducationField"].isna().sum():
    n_missing = df["EducationField"].isna().sum()
    mode_val = df["EducationField"].mode()[0]
    df["EducationField"] = df["EducationField"].fillna(mode_val)
    note(f"Imputed {n_missing} missing 'EducationField' values with mode ('{mode_val}')")

# ---------------------------------------------------------------------
# 7. Correct data types for downstream tools (Tableau reads these cleanly)
# ---------------------------------------------------------------------
int_cols = ["Age", "MonthlyIncome", "DistanceFromHome", "JobSatisfaction",
            "EnvironmentSatisfaction", "YearsSinceLastPromotion"]
for col in int_cols:
    df[col] = df[col].round(0).astype(int)
note(f"Cast {int_cols} to integer type after cleaning/imputation")

# ---------------------------------------------------------------------
# 8. Derived / calculated fields needed for the dashboard
# ---------------------------------------------------------------------
df["AttritionFlag"] = (df["Attrition"] == "Yes").astype(int)

df["AgeGroup"] = pd.cut(
    df["Age"], bins=[17, 25, 35, 45, 55, 65],
    labels=["18-25", "26-35", "36-45", "46-55", "56-65"]
)

df["TenureBand"] = pd.cut(
    df["YearsAtCompany"], bins=[-1, 1, 3, 6, 10, 40],
    labels=["0-1 yrs", "2-3 yrs", "4-6 yrs", "7-10 yrs", "10+ yrs"]
)

df["IncomeBand"] = pd.cut(
    df["MonthlyIncome"], bins=[0, 3000, 5000, 8000, 12000, 25000],
    labels=["<3K", "3K-5K", "5K-8K", "8K-12K", "12K+"]
)

df["SatisfactionIndex"] = (
    df["JobSatisfaction"] + df["EnvironmentSatisfaction"]
    + df["WorkLifeBalance"] + df["RelationshipSatisfaction"]
) / 4

note("Created derived fields: AttritionFlag, AgeGroup, TenureBand, IncomeBand, SatisfactionIndex")

# ---------------------------------------------------------------------
# Save cleaned dataset
# ---------------------------------------------------------------------
df.to_csv(CLEAN_PATH, index=False)
note(f"Saved cleaned dataset: {df.shape[0]} rows, {df.shape[1]} columns -> {CLEAN_PATH}")

with open("/home/claude/hr_project/cleaning_log.txt", "w") as f:
    f.write("\n".join(log))
