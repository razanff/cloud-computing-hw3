# student_data.py

import pandas as pd

# Load data
df = pd.read_csv("temp.txt", header=None, names=["ID", "FirstName", "LastName", "Age", "Phone", "City"])

# Sort by age DESC
sorted_desc = df.sort_values(by="Age", ascending=False)
print("Sorted by Age DESC:")
print(sorted_desc)

# Sort by age ASC
sorted_asc = df.sort_values(by="Age", ascending=True)
print("\nSorted by Age ASC:")
print(sorted_asc)
