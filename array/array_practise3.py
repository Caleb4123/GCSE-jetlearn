score = [1,75,2,56,95]

#finding smallest item in list
lowest = 10000000
for i in range(len(score)):
    if score[i] < lowest:
        lowest = score[i] 
print(lowest)

lowest2 = min(score)
print(lowest2)

#finding largerst item in a list

highest = max(score)
print(highest)