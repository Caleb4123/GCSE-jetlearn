fruits = ["pomegranate","orange","bannana","apple","watermelon","tomato"]

#printing individual item of a list
print(fruits[2])

#counting number of items in a list
print(len(fruits))

#adding an item at the end of the list
user = input("Add a fruit: ")
fruits.append(user)
print(fruits)

#removing an item from a list based on its index number
fruits.pop(1)
print(fruits)

#removing an item based on its value
fruits.remove("watermelon")

#changing existing value of an index
fruits[3] = "pineapple"
print(fruits)

#inserting a new item at a specific index
fruits.insert(1,"grapes")
print(fruits)

#checking if a value exists in a list
if "pomegranate" in fruits:
    print("It is in the list")
else:
    print("not in list")

for i in range(len(fruits)):
    print(fruits[i])

#
for element in fruits:
    print(element, end = "\t")

