n = int(input("Enter number:"))
number = ""
if int(n) > 9:
    print("This number > 9")
else:
    for i in range(1, n + 1):
        number += str(i)
        print(number)

