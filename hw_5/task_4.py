from random import randint

my_list = [randint(0, 100) for i in range(20)]
print(my_list)


def nul():
    for numbers, elements in enumerate(my_list):
        if elements % 2 != 0:
            my_list[numbers] = 0
    print(my_list)
    print(my_list.count(0))


if __name__ == "__main__":
    nul()

