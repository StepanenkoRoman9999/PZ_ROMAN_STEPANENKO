#Вариант 27
#Книжные магазины предлагают следующие коллекции книг.
#ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
#БукМаркет – Пушкин, Достоевский, Маяковский.
#Галерея – Чехов, Тютчев, Пушкин. Определить в каких магазинах можно приобрести книги Маяковского

magistr = {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"}
dom_knigi = {"Толстой", "Грибоедов", "Чехов", "Пушкин"}
buk_market = {"Пушкин", "Достоевский", "Маяковский"}
galereya = {"Чехов", "Тютчев", "Пушкин"}

print(f"Магазин 'Магистр': {magistr}")
print(f"Магазин 'ДомКниги': {dom_knigi}")
print(f"Магазин 'БукМаркет': {buk_market}")
print(f"Магазин 'Галерея': {galereya}")
target_author = "Маяковский"
result_shops = []
if target_author in magistr:
    result_shops.append("Магистр")
if target_author in dom_knigi:
    result_shops.append("ДомКниги")
if target_author in buk_market:
    result_shops.append("БукМаркет")
if target_author in galereya:
    result_shops.append("Галерея")
if result_shops:
    print(f"Книги автора {target_author} можно приобрести в: {', '.join(result_shops)}")