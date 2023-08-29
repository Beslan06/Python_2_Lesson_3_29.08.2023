def list_of_duplicates(_list_integer: list[int]) -> list[int]:

    _set = set()

    for _item in _list_integer:
        if _list_integer.count(_item) > 1:
            _set.add(_item)

    return list(_set)


list_integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 3, 2, 1]

print(list_of_duplicates(list_integer))














# original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
# unique_list = list(set(original_list))

# print(unique_list)

