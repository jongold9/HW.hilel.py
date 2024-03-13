def is_palindrome(text):
    # Видаляємо всі символи, крім літер
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    # Перевертаємо текст та порівнюємо його з оригіналом
    return cleaned_text == cleaned_text[::-1]

# Приклади використання функції
text1 = "Шалаш, зараз, Дід, Піп, 13231"
text2 = "Паліндром — і ні морд, ні лап"

print(is_palindrome(text1))  # Виведе True
print(is_palindrome(text2))  # Виведе True
