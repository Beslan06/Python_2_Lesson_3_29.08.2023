def list_of_duplicates(_list_integer: list[int]) -> list[int]:
    _set = set()  # Создаем пустое множество для хранения дубликатов

    for _item in _list_integer:
        if _list_integer.count(_item) > 1:  # Проверяем, сколько раз встречается элемент в списке
            _set.add(_item)  # Если элемент встречается больше одного раза, добавляем его в множество

    return list(_set)  # Преобразуем множество обратно в список и возвращаем результат

list_integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 3, 2, 1]

print(list_of_duplicates(list_integer))  # Выводим список дубликатов















# original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
# unique_list = list(set(original_list))

# print(unique_list)

