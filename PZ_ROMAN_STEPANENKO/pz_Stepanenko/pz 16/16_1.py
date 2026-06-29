 #вариант 27
 #Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
#Добавьте методы для вычисления среднего балла и определения, является ли студент
#отличником.
class Student:

    def __init__(self, first_name: str, last_name: str, grades: list[int]):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def get_average_grade(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def is_excellent_student(self) -> bool:
        if not self.grades:
            return False
        return all(grade == 5 for grade in self.grades)


if __name__ == "__main__":
    student_1 = Student("Иван", "Петров", [5, 5, 5, 5])
    print(f"Студент: {student_1.first_name} {student_1.last_name}")
    print(f"Оценки: {student_1.grades}")
    print(f"Средний балл: {student_1.get_average_grade():.2f}")
    print(f"Отличник?: {student_1.is_excellent_student()}")
    print("-" * 30)

    student_2 = Student("Анна", "Сидорова", [4, 5, 3, 5])
    print(f"Студент: {student_2.first_name} {student_2.last_name}")
    print(f"Оценки: {student_2.grades}")
    print(f"Средний балл: {student_2.get_average_grade():.2f}")
    print(f"Отличник?: {student_2.is_excellent_student()}")
    print("-" * 30)

    student_3 = Student("Олег", "Иванов", [])
    print(f"Студент: {student_3.first_name} {student_3.last_name}")
    print(f"Оценки: {student_3.grades}")
    print(f"Средний балл: {student_3.get_average_grade():.2f}")
    print(f"Отличник?: {student_3.is_excellent_student()}")
