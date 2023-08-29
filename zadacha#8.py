# Создаем словарь, где ключи - имена друзей, а значения - кортежи вещей
friends_items = {
    "Друг 1": ("палатка", "спальник", "фонарик"),
    "Друг 2": ("палатка", "котелок", "еда"),
    "Друг 3": ("спальник", "фонарик", "одежда")
}

# Список имен всех друзей
all_friends = list(friends_items.keys())

# Множество вещей, которые взяли все друзья
all_items = set.intersection(*[set(items) for items in friends_items.values()])

# Множество уникальных вещей, есть только у одного друга
unique_items = set()
for items in friends_items.values():
    unique_items.update(set(items))

# Множество вещей, есть у всех кроме одного и имя друга
shared_items = {}
for friend, items in friends_items.items():
    other_friends = all_friends.copy()
    other_friends.remove(friend)
    other_items = set.union(*[set(friends_items[other_friend]) for other_friend in other_friends])
    diff_items = set(items) - other_items
    if diff_items:
        shared_items[friend] = diff_items

print("Вещи, которые взяли все друзья:", all_items)
print("Уникальные вещи, есть только у одного друга:", unique_items - all_items)
print("Вещи, есть у всех кроме одного и имя друга:", shared_items)
