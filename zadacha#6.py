text = input("Введите строку текста: ")
words = text.split()

max_word_length = max(len(word) for word in words)
line_number = 1

for word in sorted(words, key=lambda x: (x, len(x))):
    print(f"{line_number:>{max_word_length + 1}} {word}")
    line_number += 1
