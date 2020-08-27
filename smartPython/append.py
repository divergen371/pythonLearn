numbers = [0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
positive = []
for i in range(len(numbers)):
    if numbers[i] >= 0:
        positive.append(numbers[i])


print(positive)
