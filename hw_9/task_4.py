def fake_string(text, word_to_replace, new_word, replace_count):
    replaced_text = text.replace(word_to_replace, new_word, replace_count)
    return replaced_text

# Приклад використання:
print(fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 1))
# Виведе: Marvel makes good movies, DC makes good comics

print(fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 2))
# Виведе: Marvel makes good movies, Marvel makes good comics