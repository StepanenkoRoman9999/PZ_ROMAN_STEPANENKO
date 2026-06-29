#Вариант 27.
#1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
#Элементы первого и второго файлов:
#Элементы первого файла, присутствующие во втором:
#Элементы второго файла, присутствующие в первом:
#Количество элементов:
#Количество отрицательных элементов:
#Количество положительных элементов:
a = [10, -5, 3, 7, -1, 0, 12, -8]
b = [3, -8, 5, -1, 14, 20, -5]
with open("file1.txt", "w", encoding="utf-8") as f1:
    f1.write(" ".join(map(str, a)))

with open("file2.txt", "w", encoding="utf-8") as f2:
    f2.write(" ".join(map(str, b)))
try:
    with open("file1.txt", "r", encoding="utf-8") as f1:
        a = [int(x) for x in f1.read().split()]
    with open("file2.txt", "r", encoding="utf-8") as f2:
        b = [int(x) for x in f2.read().split()]
except (ValueError, IOError) as e:
    print(f"Ошибка чтения файлов: {e}")
    a, b = [], []
ab = a + b
set_a, set_b = set(a), set(b)

a_in_b = [x for x in a if x in set_b]
b_in_a = [x for x in b if x in set_a]
cnt = len(ab)
neg = sum(1 for x in ab if x < 0)
pos = sum(1 for x in ab if x > 0)
try:
    with open("result.txt", "w", encoding="utf-8") as res:
        res.write(f"Элементы первого и второго файлов: {' '.join(map(str, ab))}\n")
        res.write(f"Элементы первого файла, присутствующие во втором: {' '.join(map(str, a_in_b))}\n")
        res.write(f"Элементы второго файла, присутствующие в первом: {' '.join(map(str, b_in_a))}\n")
        res.write(f"Количество элементов: {cnt}\n")
        res.write(f"Количество отрицательных элементов: {neg}\n")
        res.write(f"Количество положительных элементов: {pos}\n")
    print("Файл result.txt успешно создан в папке проекта!")
except IOError as e:
    print(f"Ошибка записи итогового файла: {e}")
