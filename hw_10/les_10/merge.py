""" Algorithms examples v.1 - Merge Sort """


def merge_sort(arr):
    """ Sort list of numbers using merge sort """
    if len(arr) > 1:
        mid = len(arr)//2  # Находим середину массива
        L = arr[:mid]  # Разделяем массив на две части
        R = arr[mid:]

        merge_sort(L)  # Сортируем первую часть
        merge_sort(R)  # Сортируем вторую часть

        i = j = k = 0
        # Копируем данные из временных массивов L[] и R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Проверяем если какой либо из элементов левый
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
# O(n**2)


array_to_sort = [65, 32, 26, 18, 122, 543, 2]
sorted_array = merge_sort(array_to_sort)
print(f"Sorted array is: {sorted_array}")
