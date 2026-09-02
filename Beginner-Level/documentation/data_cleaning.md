# Data Cleaning Documentation

## Summary

- Original number of records (raw, including duplicates): **2233**
- Exact duplicate rows found and removed: **25**
- Region values standardized. Before: ['East', 'NORTH', 'North', 'South', 'WEST', 'West', 'east', 'north', 'south', 'west'] -> After: ['East', 'North', 'South', 'West']
- Category values standardized (casing/spelling). Before: ['Cloth ing', 'Clothing', 'ELECTRONICS', 'Electonics', 'Electronics', 'Furniture', 'Furnitures', 'Home & Kitchen', 'Home and Kitchen', 'Stationery', 'clothing', 'electronics', 'furniture', 'home & kitchen'] -> After: ['Clothing', 'Electronics', 'Furniture', 'Home & Kitchen', 'Stationery']
- Missing 'Customer Name' values: **44** -> filled with 'Unknown Customer' (the row is still a valid transaction tied to a Customer ID, so it was kept, not dropped).
- Invalid / unparseable 'Order Date' values found: **11** (examples: ['2024-13-05', nan, 'not_a_date', '2024/02/30', '31-02-2024']) -> these rows were removed since a transaction with no valid date cannot be placed in the monthly/seasonal analysis.
- Missing 'Discount' values: **66** -> filled with **0** (no discount recorded means no discount was applied, so 0 is the correct value, not a guess).
- Rows with invalid numeric values (Quantity <= 0 or Unit Price <= 0): **8** -> removed, since a non-positive quantity or price is a data-entry error, not a legitimate transaction.
- 'Sales' and 'Profit' values were left as recorded (not recalculated from Quantity x Unit Price), since a POS/e-commerce export can include pricing rules not visible in a flat file. Recalculating would risk silently overwriting legitimate figures with assumptions.
- Checked for outliers: **20** orders sit above the 99th percentile of Sales (> 15,518.40). These were reviewed and kept, since large orders (higher quantity or premium products) are legitimate business activity, not errors.
- Duplicate 'Customer ID' values were NOT treated as an issue: repeat purchases by the same customer are expected and are used later in customer analysis.
- **Final number of records after cleaning: 2189** (original 2233 -> removed 25 duplicates, 11 invalid-date rows, and 8 invalid-numeric rows).
- Derived columns created: Year, Month, Month Number, Year-Month, Profit Margin %, Order Value.
- Fields requiring no correction: Order ID, Customer ID, Sub-Category/Product Name linkage, Payment Method (already consistent in the raw export).

## Before / After Row Counts

| Stage | Row Count |
|---|---|
| Raw data (as exported) | 2233 |
| After removing exact duplicates | 2208 |
| After removing invalid dates & invalid numeric rows | 2189 |
