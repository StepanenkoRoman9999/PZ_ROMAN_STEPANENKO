#Создайте класс "Автомобиль", который содержит информацию о марке, модели и
#годе выпуска. Создайте класс "Грузовик", который наследуется от класса
#"Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
#"Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
#информацию о количестве пассажиров.
class Car:

    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year


class Truck(Car):

    def __init__(self, brand: str, model: str, year: int, load_capacity: float):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity


class PassengerCar(Car):

    def __init__(self, brand: str, model: str, year: int, passenger_count: int):
        super().__init__(brand, model, year)
        self.passenger_count = passenger_count


if __name__ == "__main__":
    truck = Truck("Volvo", "FH16", 2022, 25.5)
    print(f"Грузовик: {truck.brand} {truck.model}")
    print(f"Год: {truck.year}, Грузоподъемность: {truck.load_capacity} т")
    print("-" * 30)

    passenger_car = PassengerCar("Toyota", "Camry", 2024, 5)
    print(f"Легковой автомобиль: {passenger_car.brand} {passenger_car.model}")
    print(f"Год: {passenger_car.year}, Пассажиров: {passenger_car.passenger_count}")
