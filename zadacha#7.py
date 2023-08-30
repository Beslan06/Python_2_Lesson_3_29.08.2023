text = input("Введите строку текста: ")  # Запрашиваем у пользователя строку текста
frequency = {}  # Создаем пустой словарь для подсчета частоты символов

# Перебираем каждый символ в тексте
for char in text:
    if char in frequency:  # Если символ уже есть в словаре
        frequency[char] += 1  # Увеличиваем его счетчик на 1
    else:
        frequency[char] = 1  # Иначе добавляем символ в словарь со значением 1

# Перебираем пары ключ-значение в словаре
for char, count in frequency.items():
    print(f"Символ '{char}' встречается {count} раз.")  # Выводим информацию о частоте символа
