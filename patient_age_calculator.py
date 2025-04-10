patients = []
try:
    num_patients = int(input("How many patients? "))
    if num_patients <= 0:
        print("Please enter at least 1 patient.")
    else:    
        for i in range(num_patients):
            while True:
                try:
                    age = int(input(f"Enter age for patient {i+1}: "))
                    if age < 0:
                        print("Age cannot be negative. Please try again.")
                        continue 
                    patients.append(age)
                    break
                except ValueError:
                    print("Please enter a valid number for age.")
        average_age = sum(patients) / len(patients)
        print(f"Average patient age: {average_age}")
except ValueError:
    print("Please enter a valid number for the number of patients.")        