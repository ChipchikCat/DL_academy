__author__ = 'Соловьев Андрей Сергеевич.'
# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:

# TODO:

def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.
    Параметры:
        - a, b (int или float).
    Результат:
        - float.
    """
    return (a * b) ** 0.5

try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except ValueError:
    print('Некорректные данные:Введите число!')

# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# TODO:

import os
try:
    for i in range(1, 10):
        os.mkdir("dir_" + str(i))
except:
    print("Папки созданы!")
a = input("")
print(a)
try:
    for i in range(1, 10):
        os.rmdir("dir_" + str(i))
except:
    print("Папки удалены!")


# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

# TODO:

import os

os.listdir()
print(os.listdir())


# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# TODO:

import os

os.system("copy %s %s" % (__file__,"easy.py"))

