import math


def catheter(a, b):
    if a > b:
        return "not possible"
    return math.sqrt(a ** 2 + b ** 2)


def hypotenuse(a, b):
    if a < b:
        return "not possible"
    if a == b:
        return "not possible"
    return math.sqrt(a ** 2 - b ** 2)


def height(a, b):
    return a * 2 / b


def area(a, b):
    return a * b / 2


wished_result = input("What do you want to calculate? (a/b, c, h, A)\n>> ")
if wished_result == "a" or wished_result == "b":
    b = float(input("b = "))
    c = float(input("c = "))
    print(catheter(c, b))
elif wished_result == "c":
    a = float(input("a = "))
    b = float(input("b = "))
    print(hypotenuse(a, b))
elif wished_result == "h":
    a = float(input("A = "))
    b = float(input("c = "))
    print(height(a, b))
elif wished_result == "A":
    a = float(input("h or a = "))
    b = float(input("c or b = "))
    print(area(a, b))

