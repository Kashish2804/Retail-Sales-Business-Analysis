"""
Generates a synthetic 'Superstore-style' retail transactions dataset.
Intentionally injects realistic messiness (missing values, duplicates,
inconsistent categories, bad dtypes, impossible values) so the cleaning
stage of the project has genuine work to do.
"""
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

rng = np.random.default_rng(42)

# ---- Reference data -------------------------------------------------
n_customers = 800
n_orders_target = 9800

regions = {
    "East": ["New York", "Boston", "Philadelphia", "Newark"],
    "West": ["Los Angeles", "San Francisco", "Seattle", "Phoenix"],
    "Central": ["Chicago", "Dallas", "Houston", "Detroit"],
    "South": ["Atlanta", "Miami", "Charlotte", "Nashville"],
}

categories = {
    "Furniture": ["Chairs", "Tables", "Bookcases", "Furnishings"],
    "Office Supplies": ["Binders", "Paper", "Storage", "Art", "Labels"],
    "Technology": ["Phones", "Machines", "Accessories", "Copiers"],
}

segments = ["Consumer", "Corporate", "Home Office"]
ship_modes = ["Standard Class", "Second Class", "First Class", "Same Day"]

# messy variants that will need cleaning later
category_variants = {
    "Furniture": ["Furniture", "furniture", "FURNITURE", "Furnitur "],
    "Office Supplies": ["Office Supplies", "office supplies", "Office  Supplies", "OfficeSupplies"],
    "Technology": ["Technology", "technology", "TECHNOLOGY", "Tech"],
}
region_variants = {
    "East": ["East", "east", "EAST"],
    "West": ["West", "west", "WEST"],
    "Central": ["Central", "central", "Centrl"],
    "South": ["South", "south", "SOUTH"],
}

# ---- Customers --------------------------------------------------------
customer_ids = [f"CUST-{i:05d}" for i in range(1, n_customers + 1)]
customer_region = {cid: rng.choice(list(regions.keys())) for cid in customer_ids}
customer_segment = {cid: rng.choice(segments, p=[0.55, 0.3, 0.15]) for cid in customer_ids}
first_names = ["James","Mary","John","Patricia","Robert","Jennifer","Michael","Linda",
               "William","Elizabeth","David","Barbara","Richard","Susan","Joseph","Jessica",
               "Thomas","Sarah","Charles","Karen","Chris","Nancy","Daniel","Lisa","Paul","Betty"]
last_names = ["Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis",
              "Rodriguez","Martinez","Hernandez","Lopez","Gonzalez","Wilson","Anderson",
              "Thomas","Taylor","Moore","Jackson","Martin","Lee","Perez","Thompson","White"]
customer_name = {cid: f"{rng.choice(first_names)} {rng.choice(last_names)}" for cid in customer_ids}

# give customers different "activity levels" so repeat-purchase / churn analysis is meaningful
activity_weight = rng.choice([1, 2, 3, 5, 9], size=n_customers, p=[0.35, 0.25, 0.2, 0.13, 0.07])
weights = activity_weight / activity_weight.sum()

# ---- Date range: 3 years, with mild seasonality + a soft growth trend ----
start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 12, 31)
total_days = (end_date - start_date).days

def sample_order_date():
    # weight later months slightly higher (growth) + Nov/Dec seasonal bump
    while True:
        day_offset = rng.triangular(0, total_days * 0.85, total_days)
        d = start_date + timedelta(days=day_offset)
        boost = 1.6 if d.month in (11, 12) else 1.0
        if rng.random() < boost / 1.6:
            return d

# ---- Products -----------------------------------------------------------
products = []
pid = 1
for cat, subs in categories.items():
    for sub in subs:
        n_products = rng.integers(4, 9)
        for _ in range(n_products):
            base_price = {
                "Furniture": rng.uniform(60, 900),
                "Office Supplies": rng.uniform(2, 120),
                "Technology": rng.uniform(30, 1800),
            }[cat]
            products.append({
                "Product ID": f"PROD-{pid:04d}",
                "Category": cat,
                "Sub-Category": sub,
                "Product Name": f"{sub} Item {pid}",
                "Unit Price": round(base_price, 2),
            })
            pid += 1
products_df = pd.DataFrame(products)

# ---- Generate order/line rows -------------------------------------------
rows = []
order_id_counter = 1
n_orders = n_orders_target
customer_sample = rng.choice(customer_ids, size=n_orders, p=weights)

for i in range(n_orders):
    cust = customer_sample[i]
    order_date = sample_order_date()
    order_id = f"ORD-{2023000 + order_id_counter}"
    order_id_counter += 1
    n_lines = rng.choice([1, 1, 2, 2, 3], p=[0.35, 0.3, 0.2, 0.1, 0.05])
    ship_days = int(rng.choice([2, 3, 4, 5, 7]))
    ship_date = order_date + timedelta(days=ship_days)
    city = rng.choice(regions[customer_region[cust]])
    region_val = customer_region[cust]
    for _ in range(int(n_lines)):
        prod = products_df.sample(1, random_state=rng.integers(0, 1_000_000)).iloc[0]
        qty = int(rng.integers(1, 12))
        discount = float(rng.choice([0, 0, 0, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5], p=[0.35,0.15,0.1,0.12,0.1,0.08,0.05,0.03,0.02]))
        unit_price = prod["Unit Price"]
        sales = round(unit_price * qty * (1 - discount), 2)
        cost_ratio = rng.uniform(0.55, 0.85)
        profit = round(sales - (unit_price * qty * cost_ratio), 2)

        rows.append({
            "Order ID": order_id,
            "Order Date": order_date,
            "Ship Date": ship_date,
            "Ship Mode": rng.choice(ship_modes, p=[0.55, 0.2, 0.15, 0.1]),
            "Customer ID": cust,
            "Customer Name": customer_name[cust],
            "Segment": customer_segment[cust],
            "Region": rng.choice(region_variants[region_val]),  # inject case/typo variants
            "City": city,
            "Category": rng.choice(category_variants[prod["Category"]]),  # inject variants
            "Sub-Category": prod["Sub-Category"],
            "Product Name": prod["Product Name"],
            "Quantity": qty,
            "Discount": discount,
            "Sales": sales,
            "Profit": profit,
        })

df = pd.DataFrame(rows)

# ---- Inject messiness -----------------------------------------------------

# 1. Missing values in a few columns
for col, frac in [("City", 0.015), ("Ship Mode", 0.01), ("Discount", 0.02), ("Profit", 0.01)]:
    idx = df.sample(frac=frac, random_state=1).index
    df.loc[idx, col] = np.nan

# 2. Duplicate rows (exact dupes, simulating double-logged transactions)
dupes = df.sample(frac=0.008, random_state=2)
df = pd.concat([df, dupes], ignore_index=True)

# 3. Dates stored as inconsistent strings (will need parsing)
df["Order Date"] = df["Order Date"].dt.strftime("%Y-%m-%d")
mixed_fmt_idx = df.sample(frac=0.05, random_state=3).index
df.loc[mixed_fmt_idx, "Order Date"] = pd.to_datetime(df.loc[mixed_fmt_idx, "Order Date"]).dt.strftime("%d/%m/%Y")
df["Ship Date"] = df["Ship Date"].dt.strftime("%Y-%m-%d")

# 4. A few impossible / suspicious values
bad_idx = df.sample(frac=0.004, random_state=4).index
df.loc[bad_idx, "Quantity"] = -abs(df.loc[bad_idx, "Quantity"])  # negative quantity
bad_idx2 = df.sample(frac=0.003, random_state=5).index
df.loc[bad_idx2, "Sales"] = 0  # zero-sales rows (likely cancelled/void, undocumented)

# 5. Quantity stored as text for some rows (dtype issue)
df["Quantity"] = df["Quantity"].astype(object)
text_idx = df.sample(frac=0.01, random_state=6).index
df.loc[text_idx, "Quantity"] = df.loc[text_idx, "Quantity"].astype(str) + " units"

# 6. Whitespace / casing issues in Customer Name
ws_idx = df.sample(frac=0.01, random_state=7).index
df.loc[ws_idx, "Customer Name"] = " " + df.loc[ws_idx, "Customer Name"].astype(str) + "  "

# Shuffle rows so duplicates/messy rows aren't clustered at the end
df = df.sample(frac=1, random_state=99).reset_index(drop=True)

df.to_csv("/home/claude/project/raw_superstore_data.csv", index=False)
print("Rows:", len(df))
print("Unique orders:", df["Order ID"].nunique())
print("Unique customers:", df["Customer ID"].nunique())
print(df.dtypes)
print(df.isna().sum())
