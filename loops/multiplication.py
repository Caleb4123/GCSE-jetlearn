user = int(input("Enter the number to generate the table: "))
for i in range(1,11):
    calc = i * user
    print(f"{i} * {user} = {calc}")