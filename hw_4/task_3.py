a = int(input("enter numbers for a: "))
b = int(input("enter numbers for b: "))
if a < b:
    for i in range(a, b + 1, 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)