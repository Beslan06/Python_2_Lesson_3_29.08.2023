text = input("Введите строку текста: ")  # Запрашиваем у пользователя строку текста
words = text.split()  # Разделяем строку на слова и сохраняем их в списке "words"

max_word_length = max(len(word) for word in words)  # Находим максимальную длину слова в списке
line_number = 1  # Инициализируем переменную для отслеживания номера строки

for word in sorted(words, key=lambda x: (x, len(x))):  # Перебираем слова, отсортированные по алфавиту и длине
    print(f"{line_number:>{max_word_length + 1}} {word}")  # Выводим номер строки, выравнивая по максимальной длине слова, и само слово
    line_number += 1  # Увеличиваем номер строки для следующей итерации
