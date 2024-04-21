#1) Подсчет суммы всех четных чисел от 1 до n. Реализовать двумя видами циклов
n = int(input("Введите n: "))

count = 1
while count <= n:
    print(count)
    count += 1

for i in range(1, n + 1):
    print(i)
    i += 1

#2) самое длинное слово из массива. Реализовать двумя видами циклов
pencil_case = ['pen', 'pencil', 'eraser', 'steak', 'duct_tape']
longest_word = ''
i = 0
while i < len(pencil_case):
    if len(pencil_case[i]) >= len(longest_word):
        longest_word = pencil_case[i]
    i += 1
print(longest_word)

longest_word = ''
for j in pencil_case:
    if len(j) >= len(longest_word):
        longest_word = j
print(longest_word)

#3) Расчет факториала числа с выводом каждого шага.
f = int(input("Введите число для нахождения факториала: "))
factorial = 1
for i in range(f):
    factorial = factorial * (i + 1)
    print(factorial)

#4) Вывести каждый 3 элемент списка вместе с его индексом, используя enumerate()
my_list =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[0], 0)
for i, j in enumerate(my_list):
    if (i+1) % 3 == 0:
        print(j, i)

#5) Напечатать таблицу умножения для числа n, использовать f строки
n = int(input())
for i in range(10):
    print(f"{i} *  {n}  =  {i * n}")

#6) Подсчитать количество цифр в числе. Реализовать двумя видами циклов
n = int(input())
count = 0
while n > 0:
    count += 1
    n //= 10
print(count)

n = int(input())
count = 0
for i in str(n):
    if i.isdigit():
        count += 1
print(count)

#7) Проверить, является ли строка палиндромом (зеркальная)
string = str(input())
if string == string[::-1]:
    print("Is polinprom")
else:
    print("Is not polindrom")

#8) Определить, содержит ли список дубликаты
my_list = [1, 45, 54, 3, 4, 4, 43, 4322, 1, 5]
def duplicates(list_):
    set_ = set()
    for item in list_:
        if item in set_:
            return  True
        else:
            set_.add(item)
    return False

if duplicates(my_list):
    print("Yes")
else:
    print("No")

#9) Удалить все дубликаты из списка без использования дополнительных структур.
# Реализовать двумя видами циклов, для удаления можно использовать pop() либо del
def remove_duplicates_for (list_):
    for i in list_:
        for j in range(i):
            if list_[j] == list_[j+1]:
                del(list_[j])
def remove_duplicates_while (list_):
    i = 0
    while i < len(list_):
        j = i + 1
        while j < len(list_):
            if list_[i] == list_[j]:
                del list_[j]
            else:
                j += 1
        i += 1
my_list = [1, 1, 2, 3, 55, 6, 33, 55]
remove_duplicates_while(my_list)
print(my_list)

#10)Вывести каждую букву строки в обратном порядке без использования reversed() или [::-1]
string = "abcdefg"
for i in range(len(string)):
    print(string[len(string) - 1 - i])

#11) Напечатать календарь месяца, предполагая, что месяц начинается в понедельник и имеет 31 день
print("ПН ВТ СР ЧТ ПТ СБ ВС")
day = 1
list_= [1, 2, 3, 4, 5, 6, 7]
for i in range(5):
  for j in list_:
    j = day
    day += 1
    print(j)
  print("\n")












