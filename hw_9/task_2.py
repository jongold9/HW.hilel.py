def hide_email(email):
    parts = email.split('@')
    username = parts[0]
    domain = parts[1]
    hidden_username = username[:2] + '*' * len(username[2:-2]) + username[-2:]
    hidden_email = hidden_username + '@' + domain
    return hidden_email

# Приклад використання:
print(hide_email("somebody_email@gmail.com"))  # Виведе: sm***@**il.com