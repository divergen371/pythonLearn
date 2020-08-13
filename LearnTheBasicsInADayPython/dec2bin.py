target = 255
resultbin = ""

while target != 0:
    reminder =target % 2
    target = target // 2
    resultbin += str(reminder)

resultbin_reverse = ''.join(list(reversed(resultbin)))
print(resultbin_reverse)

