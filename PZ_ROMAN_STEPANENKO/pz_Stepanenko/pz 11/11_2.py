 #2. Составить генератор (yield), который переведет символы строки из нижнего
#регистра в верхний
def up(inp):
    for char in inp:
        yield char.upper()
def main():
    text = "hello, python world!"
    print(f"строка: {text}")
    try:
        gen = up(text)
        result = "".join(gen)
        print(f": {result}")
    except Exception as e:
        print(f"ошибка: {e}")
main()