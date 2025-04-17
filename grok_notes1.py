import pandas as pd
import matplotlib.pyplot as plt

#example: Analyzing a diabetes dataset
df = pd.read_csv("diabetes.csv") 
print(df.head())  #View first 5 rows
plt.scatter(df["Glucose"],
df["BMI"], c=df["Outcome"])
plt.xlabel("Glucose Level")
plt.ylabel("BMI")
plt.title("Diabetes Risk Analysis")
plt.show()