# arithmetic: =,+,-,/,*,%,,//,**,()
# boolean: and,or,not
# PEMDAS - parenthesis, exponent, multiplication, division, addition, subtration
# relational: ==,!=, >=, <=, <, >  

"""
A shopping website gives discounts based on the following rules:
    If cart value is above ₹5000 → 20% discount
    If cart value is between ₹2000 and ₹5000 → 10% discount
    If the user is a premium member → extra 5% discount
    Final price should not go below ₹0
👉 Task:
 Write a program that:
    Takes cart value and membership status (True/False)
    Calculates final payable amount
"""
"""
value = int(input("Enter the cart value: "))
premium = input("Are you a premium member? (yes or no) ")
if value > 5000:
    value = value * 0.8
elif value > 2000 and value < 5000:
    value = value * 0.9

if premium == "yes":
    value = value * 0.95

print(value)

"""


"""
Delivery charges depend on:
Distance:
≤ 5 km → ₹50
5–15 km → ₹100
15 km → ₹200



If order value > ₹1000 → free delivery
If raining → extra ₹30
	Calculate the final charges.
"""

"""
order = int(input("Enter the order value: "))
distance = int(input("Enter the distance (in km): "))
charge = 0
rain = input("Is it raining? (yes or no) ")
if distance <= 5:
    charge = 50
elif distance > 5 and distance < 15:
    charge = 100
else:
    charge = 200

if order > 1000:
    charge = 0

if rain == "yes":
    charge = charge + 30

total = order + charge
print("The total is",total)
"""

"""
If each day of the week is represented with a number with Monday as 1, Tuesday as 2 and so on. Write an expression to check if it is a weekend.


day = int(input("Enter the day as a number: "))
if day == 6 or day == 7:
    print("weekend")
else:
    print("weekday")
"""
"""
A student gets scholarship based on:
Marks ≥ 85
If family income < 3 lakh → 100% scholarship
Else → 50% scholarship
Marks 70-84
If sports quota → 50%
Else → 25%
Marks < 70 → No scholarship
"""
