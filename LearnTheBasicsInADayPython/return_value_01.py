def my_print1(x):
    print('my print1: ' + str(x))


def my_print2(x):
    print('my print2: ' + str(x))
    return

a = my_print1(5)
print(a)

b = my_print2(5)
print(b)