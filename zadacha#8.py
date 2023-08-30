# Создаем словарь с вещами друзей
friends_items = {
    "Друг 1": ("палатка", "спальник", "фонарик"),
    "Друг 2": ("палатка", "котелок", "еда"),
    "Друг 3": ("спальник", "фонарик", "одежда")
}

# Получаем список имен всех друзей
all_friends = list(friends_items.keys())

# Получаем множество вещей, которые взяли все друзья
all_items = set.intersection(*[set(items) for items in friends_items.values()])

# Создаем множество для уникальных вещей, которые есть только у одного друга
unique_items = set()
for items in friends_items.values():
    unique_items.update(set(items))

# Создаем словарь для вещей, которые есть у всех, кроме одного друга, с указанием имени друга
shared_items = {}
for friend, items in friends_items.items():
    other_friends = all_friends.copy()
    other_friends.remove(friend)
    other_items = set.union(*[set(friends_items[other_friend]) for other_friend in other_friends])
    diff_items = set(items) - other_items
    if diff_items:
        shared_items[friend] = diff_items

# Выводим результаты
print("Вещи, которые взяли все друзья:", all_items)
print("Уникальные вещи, есть только у одного друга:", unique_items - all_items)
print("Вещи, есть у всех кроме одного друга и имя друга:", shared_items)
