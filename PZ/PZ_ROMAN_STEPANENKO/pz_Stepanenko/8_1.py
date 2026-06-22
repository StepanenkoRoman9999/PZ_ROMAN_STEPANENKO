#Вариант 27
#1. Удалите ключи ["name", "salary"] из sample_dict
sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

print("Исходный словарь")
print(sample_dict)
keys_to_remove = ["name", "salary"]
for key in keys_to_remove:
    if key in sample_dict:
        sample_dict.pop(key)
print("Итог")
print(sample_dict)
