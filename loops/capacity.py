capacity = int(input("Enter the amount in the class: "))
students = []
while capacity > len(students):
    students.append(input("Enter the name to enter: "))

print("class is now full")
print(students)
