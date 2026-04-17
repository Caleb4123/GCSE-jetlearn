password = "password1"
correct = False
for i in range(3):
    user = input("Enter the password: ")
    if user == password:
        print("Correct password")
        correct = True
        break
    else:
        print("Incorrect password, try again")
        
if correct == False:
    print("No more attempts left")
    