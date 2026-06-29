import os
import sqlite3
from sqlite3 import Error

DB_NAME = "online_market.db"


def a() -> sqlite3.Connection | None:
    try:
        b_conn = sqlite3.connect(DB_NAME)
        b_conn.row_factory = sqlite3.Row
        return b_conn
    except Error as e:
        print(f"Ошибка БД: {e}")
        return None


def b() -> None:
    c = a()
    if not c:
        return
    try:
        d_cursor = c.cursor()

        # Принудительно пересоздаем чистую таблицу при запуске
        d_cursor.execute("DROP TABLE IF EXISTS Sales")

        d_cursor.execute(
            """
            CREATE TABLE Sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                product TEXT NOT NULL,
                unit TEXT NOT NULL,
                quantity REAL NOT NULL,
                price REAL NOT NULL
            )
        """
        )

        e = [
            ("Иванов И.И.", "Ноутбук", "штуки", 1.0, 75000.0),
            ("Петров П.П.", "Кофе в зернах", "килограммы", 2.5, 3200.0),
            ("Сидоров С.С.", "Минеральная вода", "литры", 12.0, 80.0),
            ("Иванов И.И.", "Мышь беспроводная", "штуки", 2.0, 1500.0),
            ("Алексеев А.А.", "Яблоки", "килограммы", 5.0, 120.0),
            ("Николаев Н.Н.", "Моторное масло", "литры", 4.0, 4500.0),
            ("Петров П.П.", "Монитор", "штуки", 1.0, 18000.0),
            ("Смирнова А.В.", "Апельсиновый сок", "литры", 6.0, 150.0),
            ("Федоров Ф.Ф.", "Смартфон", "штуки", 1.0, 45000.0),
            ("Кузнецов К.К.", "Бананы", "килограммы", 3.2, 140.0),
        ]

        d_cursor.executemany(
            """
            INSERT INTO Sales (customer_name, product, unit, quantity, price)
            VALUES (?, ?, ?, ?, ?)
        """,
            e,
        )
        c.commit()
        print("База успешно заполнена 10 позициями.")
    except Error as e:
        print(f"Ошибка при заполнении: {e}")
    finally:
        c.close()


def c() -> None:
    print("\n--- Новая продажа ---")
    try:
        f = input("ФИО покупателя: ").strip()
        g_val = input("Товар: ").strip()
        h = input("Ед. изм. (штуки/килограммы/литры): ").strip()
        i = float(input("Количество: "))
        j = float(input("Цена за единицу: "))
        if not f or not g_val or not h:
            print("Ошибка: Пустые поля!")
            return
        k = a()
        if k:
            d_cursor = k.cursor()
            d_cursor.execute(
                """
                INSERT INTO Sales (customer_name, product, unit, quantity, price)
                VALUES (?, ?, ?, ?, ?)
            """,
                (f, g_val, h, i, j),
            )
            k.commit()
            print("Запись добавлена!")
            k.close()
    except ValueError:
        print("Ошибка: Неверный формат чисел!")
    except Error as e:
        print(f"Ошибка БД: {e}")


def d() -> None:
    print("\n--- Поиск ---")
    print(
        "1. По ФИО покупателя\n2. Дороже заданной цены\n3. По ед. измерения"
    )
    f = input("Выбор (1-3): ").strip()
    k = a()
    if not k:
        return
    l = k.cursor()
    try:
        if f == "1":
            m = input("Введите ФИО или часть: ").strip()
            l.execute(
                "SELECT * FROM Sales WHERE customer_name LIKE ?",
                (f"%{m}%",),
            )
        elif f == "2":
            n = float(input("Минимальная цена: "))
            l.execute("SELECT * FROM Sales WHERE price > ?", (n,))
        elif f == "3":
            o = input("Единица измерения: ").strip()
            l.execute("SELECT * FROM Sales WHERE unit = ?", (o,))
        else:
            print("Неверный выбор.")
            return
        p = l.fetchall()
        if p:
            print(
                f"\n{'ID':<4} | {'Покупатель':<15} | {'Товар':<18} | {'Ед':<5} | {'Кол':<4} | {'Цена':<8}"
            )
            print("-" * 65)
            for r in p:
                print(
                    f"{r['id']:<4} | {r['customer_name']:<15} | {r['product']:<18} | {r['unit']:<5} | {r['quantity']:<4} | {r['price']:<8}"
                )
        else:
            print("Ничего не найдено.")
    except (ValueError, Error) as e:
        print(f"Ошибка: {e}")
    finally:
        k.close()


def e() -> None:
    print("\n--- Редактирование ---")
    print(
        "1. Изменить цену товара по имени\n2. Скидка покупателю\n3. Изменить количество по ID"
    )
    f = input("Выбор (1-3): ").strip()
    k = a()
    if not k:
        return
    l = k.cursor()
    try:
        if f == "1":
            g_val = input("Точное имя товара: ").strip()
            j = float(input("Новая цена: "))
            l.execute(
                "UPDATE Sales SET price = ? WHERE product = ?", (j, g_val)
            )
        elif f == "2":
            m = input("ФИО покупателя: ").strip()
            s = float(input("Размер скидки (руб): "))
            l.execute(
                "UPDATE Sales SET price = MAX(0, price - ?) WHERE customer_name = ?",
                (s, m),
            )
        elif f == "3":
            t = int(input("ID записи: "))
            i = float(input("Новое количество: "))
            l.execute("UPDATE Sales SET quantity = ? WHERE id = ?", (i, t))
        else:
            print("Неверный выбор.")
            return
        k.commit()
        print(f"Обновлено строк: {l.rowcount}")
    except (ValueError, Error) as e:
        print(f"Ошибка: {e}")
    finally:
        k.close()


def f() -> None:
    print("\n--- Удаление ---")
    print(
        "1. По уникальному ID\n2. Все покупки товара\n3. Все заказы дешевле заданной цены"
    )
    g_val = input("Выбор (1-3): ").strip()
    k = a()
    if not k:
        return
    l = k.cursor()
    try:
        if g_val == "1":
            t = int(input("ID для удаления: "))
            l.execute("DELETE FROM Sales WHERE id = ?", (t,))
        elif g_val == "2":
            h = input("Имя товара для удаления: ").strip()
            l.execute("DELETE FROM Sales WHERE product = ?", (h,))
        elif g_val == "3":
            u = float(input("Удалить всё, что дешевле (руб): "))
            l.execute("DELETE FROM Sales WHERE price < ?", (u,))
        else:
            print("Неверный выбор.")
            return
        k.commit()
        print(f"Удалено строк: {l.rowcount}")
    except (ValueError, Error) as e:
        print(f"Ошибка: {e}")
    finally:
        k.close()


def g() -> None:
    k = a()
    if not k:
        return
    l = k.cursor()
    l.execute("SELECT * FROM Sales")
    p = l.fetchall()
    k.close()
    print("\n=== ВСЯ БАЗА ДАННЫХ ===")
    if not p:
        print("База пуста.")
        return
    for r in p:
        print(
            f"ID: {r['id']} | {r['customer_name']} | {r['product']} | {r['quantity']} {r['unit']} | {r['price']} руб"
        )


def main() -> None:
    b()
    while True:
        print("\n=== МЕНЮ ===")
        print(
            "1. Показать всё | 2. Добавить | 3. Найти | 4. Изменить | 5. Удалить | 0. Выход"
        )
        v = input("\nДействие: ").strip()
        if v == "1":
            g()
        elif v == "2":
            c()
        elif v == "3":
            d()
        elif v == "4":
            e()
        elif v == "5":
            f()
        elif v == "0":
            print("Выход.")
            break
        else:
            print("Ошибка ввода.")


if __name__ == "__main__":
    main()