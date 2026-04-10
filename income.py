marks = int(input("Enter the marks: "))
income = int(input("Enter the family income: "))
sports = input("Do you have a sports quota (yes/no): ")
if marks >= 85:
    if income < 3:
        print("Full scholarship")
    else:
        print("50% scholarship")
elif marks >= 70 and marks <= 84:
    if sports == "yes":
        print("50% scholarship")
    else:
        print("25% scholarship")
else:
    print("No scholarship")