"""
Write a program to determine the discount on a shopping bill. The program should
first check if the total bill amount is greater than 3000. If it is, the
program should then check whether the customer is a premium member. If the
customer is a premium member, the program should further check whether a
coupon has been applied. If both conditions are true, the customer should 
receive a 30% discount; if only the membership condition is true, they 
should receive a 20% discount. If the customer is not a premium member,
they should receive a 10% discount. If the bill amount is 3000 or less, no 
discount should be applied.
"""
total = int(input("Enter your total bill: "))
premium = input("Are you a premium customer? (yes/no): ")
coupon = input("Have you applied a coupon? (yes/no): ")
if total > 3000:
    if premium == "yes":
        if coupon == "yes":
            print("discount is 30%")
        else:
            print("discount is 20%")
    else:
        print("discount is 10%")
else:
    print("no discount is applied")