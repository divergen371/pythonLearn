heightList = [180, 170, 160, 165, 175]

sum = 0
for i in heightList:
    sum += i
    ave = sum / len(heightList)

print(ave)

heightMax = 0
for i in heightList:
    if heightMax < i:
        heightMax = i

print(heightMax)

heightMin = heightMax
for i in heightList:
    if heightMin > i:
        heightMin = i

print(heightMin)