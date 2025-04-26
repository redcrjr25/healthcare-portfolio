# patient_age_calculator.py

# Initialize an empty list to store patient ages
patients = []

# Prompt for the number of patients and collect ages
try:
    num_patients = int(input("Enter the number of patients: "))
    if num_patients <= 0:
        print("Please enter a positive number of patients.")
    else:
        for i in range(num_patients):
            age = int(input(f"Enter age for patient {i + 1}: "))
            if age < 0:
                print("Age cannot be negative. Please enter a valid age.")
            else:
                patients.append(age)

        # Calculate and display the average age
        if patients:  # Check if the list is not empty
            average_age = sum(patients) / len(patients)
            print(f"Average patient age: {average_age:.2f}")
        else:
            print("No valid ages were entered.")

except ValueError:
    print("Please enter a valid number for the number of patients.")
