import numpy as np
import pandas as pd


# 1. Create the DataFrame
data1 = pd.DataFrame([
    [420, 380, 390], 
    [900, 1000, 3000]
], columns = ["First Class", "Second Class", "Third Class"], 
   index = ["Survived", "Died"])

# 1: Inspection ---
# View basic info about the dataset
print("--- Data Info ---")
print(data1.info()) 

# 2: Describing the Data ---
# Use describe() to get a statistical summary of the columns
print("\n--- Statistical Summary ---")
print(data1.describe())

# 3: Aggregation ---
# Calculate the total passengers in each class (Column Sum)
class_totals = data1.sum()
print("\n--- Total Passengers per Class ---")
print(class_totals)

# Calculate the total outcomes (Row Sum)
outcome_totals = data1.sum(axis=1)
print("\n--- Total Survived vs Died ---")
print(outcome_totals)

# 4: Finding Max/Min ---
# Identify which class had the highest number of deaths
# Note: Since 'Died' is an index, we look at the 'Died' row
print("\n--- Deaths per Class ---")
print(data1.loc["Died"])
print(f"\nMax Deaths: {data1.loc['Died'].max()}")

# 5: Calculating Percentages ---
# Calculate the percentage of survival for First Class
first_class_total = data1["First Class"].sum()
first_class_survival = (data1.loc["Survived", "First Class"] / first_class_total) * 100
print(f"\nFirst Class Survival Rate: {first_class_survival:.2f}%")
