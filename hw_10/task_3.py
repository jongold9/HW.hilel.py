def shift_list(lst, N):
    # Перевіряємо, чи потрібно зрушення вправо чи вліво
    if N > 0:
        # Зрушення вправо
        N = N % len(lst)  # Обрізаємо N, якщо він більше довжини списку
        shifted_list = lst[-N:] + lst[:-N]
    elif N < 0:
        # Зрушення вліво
        N = abs(N) % len(lst)  # Обрізаємо N, якщо він більше довжини списку
        shifted_list = lst[N:] + lst[:N]
    else:
        # Ніякого зрушення, повертаємо оригінальний список
        shifted_list = lst
    return shifted_list

# Приклад використання функції
my_list = [1, 2, 3, 4, 5]

# Зрушення вправо на 2 елементи
shifted_right = shift_list(my_list, 2)
print("Зрушення вправо:", shifted_right)  # Виведе: [4, 5, 1, 2, 3]

# Зрушення вліво на 3 елементи
shifted_left = shift_list(my_list, -3)
print("Зрушення вліво:", shifted_left)  # Виведе: [4, 5, 1, 2, 3]
