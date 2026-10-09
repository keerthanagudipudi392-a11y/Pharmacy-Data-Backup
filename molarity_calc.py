import pandas as pd

# 1. Load the laboratory dataset 
df = pd.read_csv("lab_solutions.csv")
df.columns = df.columns.str.strip()
df.columns = ['Drug_Name', 'Moles', 'Volume_Liters']

print(df.columns)

# 2. Python Math: Calculate Molarity for every single row instantly
df["Molarity_M"] = df["Moles"] / df["Volume_Liters"]

print("--- Automated Laboratory Formula Report ---")
print(df)

# 3. Export the scientific report to Excel
df.to_excel("Lab_Molarity_Report.xlsx", index=False)
print("\n✅ Success! Scientific formulation report exported.")

# Strip away any textt letters from the volume column automatically
df["Volume_Liters"] = df["Volume_Liters"].astype(str).str.replace(r'[^\d.]','',regex=True).astype(float)