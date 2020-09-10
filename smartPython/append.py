from typing import Any, List, Union

numbers: List[Union[int, Any]] = [0, -6, 1, -8, 2, 3, 4, 5, -1, -2, -3, -4, -5, -8, 6, 7, 8, -9]
positive = []

for i in range(len(numbers)):
    if numbers[i] >= 0:
        positive.append(numbers[i])


print(positive)
