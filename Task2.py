from re import findall
from collections import Counter


def ten_most_common_words(_text: str) -> list[tuple]:

    _PATTERN = r'\b\w+\b'
    _words = findall(_PATTERN, _text.lower())

    _TEN_WORDS = 10

    return Counter(_words).most_common(_TEN_WORDS)

text = """Сложно сказать, почему активно развивающиеся страны третьего мира набирают популярность среди определенных слоев населения, 
а значит, должны быть функционально разнесены на независимые элементы. Значимость этих проблем настолько очевидна, 
что начало повседневной работы по формированию позиции позволяет оценить значение благоприятных перспектив. 
Противоположная точка зрения подразумевает, что многие известные личности являются только методом политического участия 
и подвергнуты целой серии независимых исследований. В целом, конечно, граница обучения кадров предоставляет 
широкие возможности для вывода текущих активов. Для современного мира сложившаяся структура организации 
обеспечивает широкому кругу (специалистов) участие в формировании переосмысления внешнеэкономических политик."""

print(ten_most_common_words(text))

















# import re
# from collections import Counter

# text = """Nissan Cube третьего поколения (код кузова Z12) — автомобиль японского автопроизводителя Nissan, входящего в альянс Renault—Nissan. 
# Выпуск Cube третьего поколения осуществлялся с 2008 по 2019 год на японском предприятии Nissan Oppama Plant (город Йокосука). 
# В модельном ряду Cube сменил модель второго поколения. Отличительной особенностью автомобиля является его кубическая форма кузова, 
# от которой и происходит его название."""

# # Приведем текст к нижнему регистру и разделим его на слова, убрав знаки препинания
# words = re.findall(r'\w+', text.lower())

# # Используем Counter для подсчета частоты встречаемости слов
# word_counter = Counter(words)

# # Получаем 10 самых часто встречаемых слов
# most_common_words = word_counter.most_common(10)

# print("10 самых часто встречаемых слов:")
# for word, count in most_common_words:
#     print(f"{word}: {count}")
