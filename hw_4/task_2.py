count = 0
amount = 0
additions = 1
max2 = -1
n = -1
even = 0
odd = 0
maximum = 0
count_max = 0

n = int(input("Enter number:"))
max1 = n
while n != 0:
    count += 1
    amount += n
    additions *= n
    avr = float(amount / count)
    n = int(input("Enter number:"))
    if n > maximum:
        maximum, count_max = n, 1
    if n == maximum:
        count_max += 1
    if n > max1:
        max2 = max1
        max1 = n
    if n > max2:
        max2 = n
    if n % 2 == 0:
        even += 1
    if n % 2 != 0:
        odd += 1

print("кількість введених чисел: ", count)
print("суму введених чисел: ", amount)
print("добуток: ", additions)
print("середнє арифметичне: ", avr)
print("номер найбільшого елемента послідовності: ", max1)
print("кількість парних: ", even, )
print("кількість непарних: ", odd)
print("значення другого за величиною: ", max2)
print("дорівнюють її найбільшому елементу: ", count_max)
