import pandas as pd

#1.Messy list from client
messy_data={'Patient_Name': ['john doe','ALICE SMITH', 'bob jones']}
df=pd.DataFrame(messy_data)

print("---Messy Data From Client ---")
print(df)

#2.Python Magic:Clean names automatically
df['Patient_Name'] = df['Patient_Name'].str.title()

print("\n---Clean Data Ready ($20 Earned!) ---")
print(df)

# DAY 3: Automated Pharmacy Data Cleaner

# 1. This is our messy data array from a pharmacy distributor
messy_medicines = [
     " paracetamol ",
     "AMOXICILLIN   ",
     "   ibuprofen",
     "Metformin   ",
     "  VITAMIN  C  "
]

print("---❌ Starting Messy List ---")
print(messy_medicines)
clean_medicines = []
for medicine in messy_medicines:
    # .strip() removes hidden spaces from the front and back
    # .capitalize() makes only the first letter capital (e.g., Paracetamol)
    fixed_name = medicine.strip().capitalize()
    clean_medicines.append(fixed_name)

print("\n---✅ Final Cleaned List ---")    
print(clean_medicines)


# DAY 3: Automated Pharmacy Data Cleaner

# 1. This is our messy data array from a pharmacy distributor
messy_medicines = [
    "  AMOXICILIN ",
    "paracetamol",
    "  iboprofin ",
    "Metformin   "
]
# 2. Convert the list into a clean pandas DataFrame
df_meds = pd.DataFrame(messy_medicines, columns=["Medicine_Name"])

print("--- Messy Medicine Data From Distributor ---")
print(df_meds)

# 3. Python Magic: Clean up the text auto,atically
print("\n---Cleaning up spacing and casing...---")
# .str.strip()removes extra spaces; .str.title()capitalizes correctly
df_meds["Medicine_Name"] = df_meds["Medicine_Name"].str.strip().str.title()

print(df_meds)

# 4. Save the perfect, finalized list to an Excel report for your client
output_file = "final_report.xlsx"
df_meds.to_excel(output_file, index=False)
print(f"\n✅Success! Clean pharmacy report saved to: {output_file} ($20 Earned!)")

 # 5. Automatically find rows with missing information
print("\n🔍 Checking for missing values...")
missing_summary = df_meds.isnull().sum()
print(missing_summary)