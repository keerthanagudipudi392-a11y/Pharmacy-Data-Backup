import pandas as pd 

# 1.Define your logical rules
def process_data(value):
    if value > 50:
        return "Category A"
    else:    
        return value * 1.5

 # 2. Create a clean EXCEL file automatically
data = {"Input_Value":[20,65,10,80]} 
pd.DataFrame(data).to_excel("data.xlsx", index=False)

  # 3. Read the EXCEL file
df= pd.read_excel("data.xlsx")

  # 4. Create a blank list to hold calculations
results = []

 # 5. Today's Core Lesson: The Loop
for index, row in df.iterrows():
  val = row["Input_Value"]
  calculated_result = process_data(val)
  results.append(calculated_result)

 # 6. Save the results into a new EXCEL file
df["Processed_Results"] = results
df.to_excel("final_report.xlsx", index=False)
print("Excel sheet successfully updated!")  