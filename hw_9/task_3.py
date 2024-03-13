def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest

# Приклад використання:
print(longest_word("What makes a good man"))  # Виведе: makes