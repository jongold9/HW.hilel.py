def main():
    # Відкриваємо файл для запису
    with open('input_data.txt', 'w') as file:
        # Запитуємо користувача ввести дані та записуємо їх у файл
        while True:
            data = input("Введіть дані (Enter для завершення введення): ")
            if not data:  # Якщо користувач ввів порожній рядок, завершуємо введення
                break
            file.write(data + '\n')

    print("Дані були успішно записані у файл 'input_data.txt'.")


if __name__ == "__main__":
    main()