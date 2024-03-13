temper = input("input format, C, F, K : ")
if temper == "C":
    C = input("C number:")

if temper == "F":
    F = input("F number:")

if temper == "K":
    K = input("K number:")

text = ("C =", C,
        "F=", C * 32)
print(text)


