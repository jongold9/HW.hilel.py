""" Algorithms examples v.1 - Selection Sort """


def selection_sort(array_sort):
    """ Sort list of numbers using selection sort """
    arr = array_sort.copy()
    for i in range(len(arr)):  # pythonic way is to use enumerate
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# O(n**2)


array_to_sort = [65, 32, 26, 18, 122, 543, 2]
sorted_array = selection_sort(array_to_sort)
print(f"Sorted array is: {sorted_array}")
