import re

def check_password(password):
    # Перевірка на наявність мінімум одного символу від a-z
    if not re.search(r'[a-z]', password):
        print("Пароль повинен містити як мінімум один символ від a-z")
        return False
    
    # Перевірка на наявність мінімум одного символу від A-Z
    if not re.search(r'[A-Z]', password):
        print("Пароль повинен містити як мінімум один символ від A-Z")
        return False
    
    # Перевірка на наявність щонайменше одного символу від 0-9
    if not re.search(r'[0-9]', password):
        print("Пароль повинен містити щонайменше один символ від 0-9")
        return False
    
    # Перевірка на наявність мінімум одного символу із $#@-+=
    if not re.search(r'[$#@+=-]', password):
        print("Пароль повинен містити мінімум один символ із $#@-+=")
        return False
    
    # Перевірка на мінімальну довжину пароля (8 символів)
    if len(password) < 8:
        print("Мінімальна довжина пароля повинна бути 8 символів")
        return False
    
    # Якщо всі умови виконані, повертаємо True
    return True

# Основна частина програми
while True:
    password = input("Введіть пароль: ")
    if check_password(password):
        print("Password is correct")
        break
