from random import randint

some_list = [randint(0, 100) for i in range(20)]
count = 0

for i, _ in enumerate(some_list):
    if 0 < i < len(some_list) - 1:
        if some_list[i - 1] < some_list[i] > some_list[i + 1]:
            count += 1

print("Кількість елементів: ", count)

