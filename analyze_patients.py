# analyze_patients.py
import pandas as pd

# Example dataset
data = {
    "patient_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "age": [25, 30, 45, 50, 28, 35, 40, 60],
    "condition": ["Flu", "Diabetes", "Flu", "Hypertension", "Diabetes", "Flu", "Hypertension", "Diabetes"]
}
df = pd.DataFrame(data)

# Existing analysis
print("Average Age:", df["age"].mean())
print("Condition Counts:", df["condition"].value_counts())

# New feature: Filter by condition
condition_filter = input("Enter a condition to filter (e.g., Flu, Diabetes, Hypertension): ")
filtered_df = df[df["condition"] == condition_filter]
if not filtered_df.empty:
    print(f"Patients with {condition_filter}:")
    print(filtered_df)
    print(f"Average age of patients with {condition_filter}:", filtered_df["age"].mean())
else:
    print(f"No patients found with condition: {condition_filter}")