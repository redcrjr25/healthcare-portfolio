# analyze_patients.py
import pandas as pd

# Example: Analyze a small dataset of patients
data = {
    "patient_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "age": [25, 30, 45, 50, 28, 35, 40, 60],
    "condition": ["Flu", "Diabetes", "Flu", "Hypertension", "Diabetes", "Flu", "Hypertension", "Diabetes"]
}
df = pd.DataFrame(data)
print("Average Age:", df["age"].mean())
print("Condition Counts:", df["condition"].value_counts())