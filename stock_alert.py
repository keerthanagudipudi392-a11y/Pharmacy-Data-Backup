import pandas as pd
# 1. Load the pharmacy stock file
df = pd.read_csv("pharmacy_stock.csv")

print("---Full Pharmacy Inventory ---")
print(pd)

# 2. Advanced Filtering: Find medicines with less than 10 items left
print("\n🚨 CRITICAL ALERTS: Low Stock Items (< 10 units)🚨")
low_stock = df[df["Stock_Count"] < 10]
print(low_stock)

# 3. Export only the alerts to an Excel sheet for the manager
low_stock.to_excel("Urgent_Restock_Report.xlsx", index=False)
print("\n✅ Success! Urgent restock report saved to Excel.")

# 4. Filter for premium items over 200 INR
print("\n💰 PREMIUM INVENTORY: Items > 200 INR 💰")
expensive_meds = df[df["Price_INR"] > 200]
print(expensive_meds)