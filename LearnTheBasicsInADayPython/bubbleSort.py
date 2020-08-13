a = [1, 2, 9, 8, 0, 6, 7, 5, 4, 3]

def bubble_sort(a):
    n = len(a)
    for i in reversed(range(n)):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

bubble_sort(a)
print(a)