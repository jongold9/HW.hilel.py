def count_points(win, draw, loss):
    return win * 3 + draw * 1 + loss * (-1)

# Приклад використання:
print(count_points(3, 2, 2))  # Виведе: 9