#1) Попросите пользователя ввести строку и выведите ее в обратном порядке, не используя метод reverse() и sorted().
text = input()
reversed_text = text[::-1]
print("1st task:", reversed_text)

#2) Замените в пользовательской строке все появления буквы h на букву H, кроме первого и последнего вхождения.
text = input()
reversed_text = text[::-1]
left_index = text.find('h')
right_index = len(text) - 1 - reversed_text.find('h')
print("2nd task:", text[:left_index + 1] + text[left_index + 1:right_index].replace('h', 'H') + text[right_index:])

#3) Выведите количество слов в строке
list_ = input()
print("3d task:", list_.count(' ') + 1)

#4) Выведите количество слов в строке, не используя метод split()
#уже сделано

#5) У Вас есть строка, состоящая из двух слов, разделенных пробелом. Переставьте эти слова местами.
#Результат запишите в строку и выведите получившуюся строку.
string_ = input()
str_ = string_.split()
rev_str_ = ' '.join(reversed(str_))
print("5th task:", rev_str_)

#6) Ваша программа получает на вход строку, содержащую имя, отчество и фамилию человека
#Вам необходимо вывести фамилию и инициалы.
#Пример
#Ввели: Степанов Алексей Иванович
#Получили: Степанов А. И.
full_name = input()
lastname, name, father_name = full_name.split(" ")
print("6th task:", f'{lastname} {name[0]}. {father_name[0]}.')

#7) Создайте список-матрешку, в который поместите два элемента:
# целое число и вложенный список, в который поместите еще два элемента:
# вещественное число и вложенный список, в который поместите еще два элемента:
# комплексное число и вложенный список, в который поместите еще три элемента:
# пустой список целое число и строку "Иголка".
#Выведите на экран конечную строку.
matryoshka = [2024, [0j, [[], 2025, 'Иголка']]]
print("7th task:", matryoshka)

#8) Объедините два списка в один список двумя способами.
first = ["a", "b", "c", "d"]
second = ["e", "f", 'g']
union1 = first + second
union2 = []
union2.extend(first)
union2.extend(second)
print("8th task:", union1, union2)

#9) Соедините два списка и отсортируйте их. Затем удалите повторяющиеся элементы.
first = ["a", "b", "c", "d"]
second = ["e", "f", 'g', "a", "b", "d"]
union = first + second
union = list(set(union))
union.sort()
print("9th task", union)

#10) Проверить, все ли числа в произвольной последовательности уникальны
numbers_ = [1, 2, 3, 3, 45, 56, 55, 55]
numbers_.sort()
list_ = list(set(numbers_))
list_.sort()
print('10th task', numbers_ == list_)

#11) Дан словарь, вывести результат
date_dict = {'year': 2024, 'month': 4, 'day': 21}
result = f"{date_dict['year']}-{date_dict['month']}-{date_dict['day']}"
print('11th task', result)

#12) На вход от пользователя поступает строка с числами, разделёнными запятой.
# Вам нужно составить список и кортеж с этими числами.

string_ = input()
num_list = [int(i) for i in string_.split(',')]
num_tuple = tuple(num_list)
print('12th task', num_list, num_tuple)

#13) Вам дано множество студентов:
#    students = {‘Schultz’, ‘Django’, ‘Brunhilde’, ‘Fritz’}
#А также множество рабочих:
#  employees = {‘Schultz’, ‘Django’, ‘Calvin’, ‘Butch’, ‘Fritz’}
#Кто-то из них учится и работает одновременно.
#Предстоит вывести в консоль:
#•	Всех людей
#•	Всех тех, кто одновременно учится и работает
#•	Всех тех, кто только работает, но не учится
#•	Всех тех, кто либо учится, либо работает, но не одновременно
#Покажите по два способа достижения результата для каждого пункта

students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}
print('13th task', students | employees)
print(students & employees)
print(employees - students)
print((students | employees) - (students & employees))

#14) Вам дан произвольный двумерный список. Нужно выполнить его транспонирование.


array = [
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55]
]

#15 Пирамида высотой равной 5