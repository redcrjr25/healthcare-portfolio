def patients_append(age):
    # Calculate and display the average age
    if patients:  # Check if the list of patients is not empty
        average_age = sum(patients) / len(patients)
        print(f"Average patient age: {average_age:.2f}")
    else:
        print("No valid ages were entered.")


# This assumes `patients` is a list defined elsewhere in your code
patients = []  # For testing, if not already defined

# Input validation (moved from the misplaced else block)
try:
    num_patients = int(input("Enter the number of patients: "))
    if num_patients <= 0:
        print("Please enter a valid number for the number of patients.")
    else:
        for _ in range(num_patients):
            age = int(input("Enter patient age: "))
            patients.append(age)
        patients_append(age)  # Calculate and print the average age
        # Calculate patients over 50
        older_patients = [age for age in patients if age > 50]
        print(f"Number of patients over 50: {len(older_patients)}")
except ValueError:
    print("No valid ages were entered.")
