#2. Из предложенного текстового файла (text18-27.txt) вывести на экран его содержимое,
#количество пробельных символов. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно поставив последнюю строку фразой введенной пользователем.
fin = "text18-27.txt"
fout = "poem_result.txt"
try:
    with open(fin, "r", encoding="utf-8") as f:
        a = f.read()
    print(a)
    b = a.count(" ")
    print(f"Количество пробельных символов: {b}")
    c = input("Введите фразу: ")
    d = a.splitlines()
    if d:
        d[-1] = c
    e = "\n".join(d)
    with open(fout, "w", encoding="utf-8") as f:
        f.write(e)

except FileNotFoundError:
    print(f"Ошибка: Файл {fin} не найден.")
except IOError as err:
    print(f"Ошибка при работе с файлами: {err}")