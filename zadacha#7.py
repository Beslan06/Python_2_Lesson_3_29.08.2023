text = input("Введите строку текста: ")
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char, count in frequency.items():
    print(f"Символ '{char}' встречается {count} раз.")
