seat = ["empty","booked","booked","empty","booked","empty","booked","booked","booked"]
count = 0
for element in seat:
    if element == "empty":
        count += 1
    
print("There are",count,"empty seats left")