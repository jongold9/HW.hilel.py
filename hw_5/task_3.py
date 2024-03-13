figure = input("1-rectangle, 2-ellipse, 3-triangle : ")

a = float(input("a: "))
b = float(input("b: "))


def mat():
    if figure == "1":
        print("S = : %.2f" % (a * b))
    elif figure == "2":
        from math import pi
        print("S = ", (pi * a * b))
    else:
        print("S = ", (a * b / 2))


print(mat())