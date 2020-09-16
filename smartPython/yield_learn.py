

def func2():
    a = 10
    b = 20
    c = a + b
    yield c

    a = 100
    b = 200
    c = a + b
    yield c

    a = 1000
    b = 2000
    c = a + b
    yield c

for x in func2():
    print(x)
