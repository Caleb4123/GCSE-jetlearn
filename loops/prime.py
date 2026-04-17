count = 0
user = int(input("Enter a number: "))
for i in range(1,user+1):
    if user % i == 0:
        count = count + 1
  
if count <= 2:
    print("It is a prime number")
else:
    print("Not a prime number")

