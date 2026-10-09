import pandas as pd

# 1. Load the messy  Nykaa cosmetic inventory file
df=pd.read_csv("nykaa_inventory.csv")
print("---Raw Nykaa Data ---")
print(df)

# 2. Automation: Fix spacing and messy brand text casing
df["Product_Name"] = df["Product_Name"].str.strip().str.title()

# 3. Security: Automatically fill empty stock fields with 'Unknown'
df["In_Stock"] = df["In_Stock"].fillna("Unknown")

print("\n---Perfect Formatted Nykaa Inventory---")
print(df)

# 4. Export pristine spreadsheet out to Excel for the client
df.to_excel("Nykaa_Clean_Report.xlsx", index=False)
print("\n✅Success! Clean beauty inventory report generated.")