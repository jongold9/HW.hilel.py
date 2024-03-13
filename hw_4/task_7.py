from random import randint

list_1 = [randint(0, 100) for i in range(20)]
list_2 = [randint(0, 100) for t in range(20)]

set_list1 = set(list_1)
set_list2 = set(list_2)

print(list_1)
print(list_2)
print("числа, що містяться одночасно як у першому списку, так і в другому: ", set_list1 & set_list2)
print("числа, що містяться в першому, але відсутні в другому: ", set_list1.difference(set_list2))
print("унікальні для першого:", set_list1.difference(set_list2))
print("унікальні для другого:", set_list2.difference(set_list1))
