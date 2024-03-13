""" Algorithms examples v.1 - Insertion Sort """


def insertion_sort(array_sort):
    """ Sort list of numbers using insertion sort """
    # Итерация от 1 до len(array_sort)
    arr = array_sort.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        # Передвигаем элементы arr[0..i-1] которые больше чем key
        # на одну позицию впереди текущей
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# O(n**2)


array_to_sort = [65, 32, 26, 18, 122, 543, 2]
sorted_array = insertion_sort(array_to_sort)
print(f"Sorted array is: {sorted_array}")
