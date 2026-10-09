import pandas as pd

df = pd.read_csv("patients.csv")
print(df)

df["Patient_Name"] = df["Patient_Name"].str.strip().str.title()
print(df)

missing_data = df.isnull().sum()
print(missing_data)

df.to_excel("Dr_Ramesh_Clean_Report.xlsx", index=False)
print("SUCCESS!")