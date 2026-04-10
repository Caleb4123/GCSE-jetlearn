"""
Write a program to determine whether a person is eligible for a loan.
The system should first check if the applicant’s salary is at least 40,000.
If this condition is satisfied, then the program should check whether the credit
#score is 700 or above. If the credit score is also satisfactory, the program
should then check the number of existing loans. If the applicant has no existing
loans, the output should be “Loan Approved - Best Offer”; otherwise, it should
print “Loan Approved - Limited Offer.” If the credit score is below 700, the
program should print “Rejected due to low credit score.” 
If the salary is less than 40,000, the program should print “Rejected due to low
salary.”
"""
salary = int(input("Enter your salary: "))
credit = int(input("Enter your credit score: "))
loans = int(input("Enter the amount of existing loans: "))
if salary >= 40000:
    if credit >= 700:
        if loans == 0:
            print("Loan Approved - Best Offer")
        else:
            print("Loan Approved - Limited Offer.")
    else:
        print("Rejected due to low credit score.")
else:
    print("Rejected due to low salary.")