user = int(input("Enter the number to revserse: "))
reversed = 0
while user != 0:
    last_digit = user % 10
    reversed = (reversed * 10) + last_digit
    user = user // 10
print(reversed)
