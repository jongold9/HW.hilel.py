#1.
name = input("Write your name: ")
print("Hellow,", name + "!")
#2.
number = int(input('Please enter an integer number:'))
print("You number =", number)
print("Next number for number ", number, "is", number + 1)
print("Previous number for number", number, "is", number - 1)
#3.
v = int(input("speed:"))
t = int(input("time:"))

if v < 0:
    print("Vasya is moving in the wrong direction")
if v > 0:
    s = v * t

    if s > 100:
        print("The distance cannot be more than 100 km, check the data!")
    if s <= 100:
        print("Distance is", s, "km")
#4.
year = int(input("write a year:"))
if year % 400 == 0 and year % 4 == 0 or year % 100 != 0:
    print("yes")
else:
    print("no")
#5.
x = int(input("X = "))
if x > 0:
    print("sign(x) = 1")
elif x < 0:
    print("sign(x) = -1")
else:
    print("sign(x) = 0")
#6.
x6 = abs(float(input("X6 = ")))
mylist = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
if x6 in mylist:
    print("yes")
else:
    print("no")
#7.
stars = int(input("Input number of stars:"))
print("*" * stars)