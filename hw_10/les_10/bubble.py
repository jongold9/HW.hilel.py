""" Algorithms examples v.1 - Bubble Sort """


def bubble_sort(array_sort):
    """ Sort list of numbers using bubble sort """
    arr = array_sort.copy()
    elements_num = len(arr)
    # Итерация по всем элементам
    for i in range(elements_num-1):
        # range(n) тоже сработает, но будет 1 лишний проход
        for j in range(elements_num-i-1):
            # Последние i элементов уже отсортированы
            # Меняем местами если текущий элемент больше чем следующий
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted()
some = [1,2,3]
some.sort()
# O(n) if already sorted, and O(n**2) for reverse order
array_to_sort = [65, 32, 26, 18, 122, 543, 2]
sorted_array = bubble_sort(array_to_sort)
print(f"Sorted array is: {sorted_array}")
