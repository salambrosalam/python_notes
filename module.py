###module

def factorial(x):
    y = x - 1
    a = x * y
    print(a)
    x = x - 1
    if (x == 1):
        return
    else:
        factorial(x)