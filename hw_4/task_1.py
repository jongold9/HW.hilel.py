day = 1
x = int(input("km 1 day: "))
y = int(input("km y day: "))
while x < y:
    day += 1
    x *= 1.1
print("Number of the day", day)