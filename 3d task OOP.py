#Создать класс для геометрической фигуры на выбор и
# добавить в него два метода – первый для расчета площади, второй для расчета периметра
class BaseFigure:
    def get_info(self):
        print(self.S, self.P)
class Square(BaseFigure):
    def __init__(self, a):
        self.S = a*a
        self.P = 4 * a
class Rectangle(BaseFigure):
    def __init__(self, a, b):
        self.square = a * b
        self.perimeter = 2*a + 2*b
class Circle(BaseFigure):
    def __init__(self, r):
        self.square = 3.14 * r * r
        self.perimeter = 6.28 * r


# Создать класс “Человек” с полями: имя, город проживания и год рождения.
# Написать метод, который будет возвращать возраст человека в годах

from datetime import datetime

class Human:
    def __init__(self, name, sity, year):
        self.name = name
        self.sity = sity
        self.year = year
    def age(self):
        return 2024 - self.year

#Создать класс калькулятор и описать в нём методы для базовых математических операций для двух чисел

class Calculate:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def plus(self):
        return self.a + self.b
    def minus(self):
        return self.a - self.b
    def divide(self):
        return self.a / self.b
    def multiplication(self):
        return self.a * self.b
    def power(self):
        return self.a ** self.b
sum = Calculate(3, 7)
print(sum.plus())

#Изучить метод str, создать класс с данным методом, продемонстрировать его выполнение
class Reminder:
    def __init__(self, subject, time, place):
        self.subject = subject
        self.time = time
        self.place = place

    def __str__(self):
        return f'Сегодняшний урок - {self.subject}, начинается в {self.time} в кабинете {self.place}'


r1 = Reminder('математика', 8.00, 511)

print(str(r1))

# Создать базовый класс сотрудник и два дочерних класса – менеджер и работник.
# В базовый класс добавить get_paid(), который в дальнейшем переопределить в дочерних,
# чтобы сотрудники разных должностей получали различную зарплату

class Employee:
    part = 'Отдел продаж'

    @classmethod
    def get_paid(cls):
        pass
class Manager(Employee):

    def get_paid(self):
        return 30000
class Worker(Employee):
    def get_paid(self):
        return 45000
employee = Worker()
print(employee.get_paid())

# Изучить что такое множественное наследование и миксины,
# привести пример использования данных концепций ООП
class Subjects:
    def __init__(self, name, time, place):
        super().__init__()
        print("init MixinLog")
        self.name = name
        self.time = time
        self.place = place

    def print_info(self):
        print(f"{self.name}, {self.time}, {self.place}")


class MixinLog:
    number = 0

    def __init__(self):
        print("init MixinLog")
        self.number += 1
        self.number = self.number

    def save_sell_log(self):
        print(f"урок будет по счету {self.number}")
class NoteBook(Subjects, MixinLog):
    pass

