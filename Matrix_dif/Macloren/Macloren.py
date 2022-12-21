import math as mat


def checker(n, x):
    if n < 0:
        msg = "n must be > 0"
        raise ValueError(msg)
    if type(n) != int:
        msg = "type error"
        raise TypeError(msg)
    if type(x) not in (int, float):
        msg = "type error"
        raise TypeError(msg)


def factorial(a):
    if a < 0:
        return 1
    if a == 0:
        return 1
    else:
        return a * mat.factorial(a - 1)


def exp(x, n):
    checker(n, x)
    s = 0
    for i in range(0, n + 1):
        s += x ** i / factorial(i)
    return s


def cos(x, n):
    checker(n, x)
    s = 0
    for i in range(0, n + 1):
        s += ((-1) ** i / factorial(2 * i)) * (x ** (2 * i))
    return s


def sin(x, n):
    checker(n, x)
    s = 0
    for i in range(0, n + 1):
        s += ((-1) ** i / factorial(2 * i + 1)) * (x ** (2 * i + 1))
    return s


def arcsin(x, n):
    checker(n, x)
    s = 0
    for i in range(0, n + 1):
        s += (factorial(2 * i) * x ** (2 * i + 1)) / \
            ((4 ** i) * (factorial(i) ** 2) * (2 * i + 1))
    return s


def arccos(x, n):
    checker(n, x)
    a = (mat.pi / 2) - arcsin(x, n)
    return a
