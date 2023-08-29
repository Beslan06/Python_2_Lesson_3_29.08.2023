items = {
    "спальник": 1.5,
    "палатка": 3.0,
    "еда": 2.0,
    "фонарик": 0.5,
    "котелок": 1.0,
    "одежда": 1.0
}

max_weight = 5.0
backpack = {item: weight for item, weight in items.items() if weight <= max_weight}

for item, weight in backpack.items():
    print(f"{item}: {weight} кг")
