patients = []
num_patients = int(input("How many patients? "))
for i in range(num_patients):
    age = int(input(f"Enter age for patient {i+1}: "))
    patients.append(age)
average_age = sum(patients) / len(patients)
print(f"Average patient age: {average_age}")