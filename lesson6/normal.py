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
except Exception:
    print("Некорректные данные:Введите число!")

# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь "меню" выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

# TODO:

import os

def cd(path):

    path = os.path.normpath(path)
    try:
        os.chdir(path)
        if os.getcwd() == path:
            print(f"Успешно перешёл. Текущая директория {os.getcwd()}")
    except FileNotFoundError:
        print(f"Папка {path} не найдена")


while True:
    print("-"*50)
    print("[1] - Перейти в папку")
    print("[2] - Просмотреть содержимое текущей папки")
    print("[3] - Удалить папку")
    print("[4] - Создать папку")
    print("[5] - Выход")
    print("-"*50)

    do = input("Укажите номер действия: ").lower()

    if do == "1":
        dirname = input("Введите название папки: ")
        cd(dirname)

    if do == "2":
        path = os.getcwd()
        os.listdir(path)

    if do == "3":
        dirname = input("Введите название папки: ")
        os.rmdir(dirname)

    if do == "4":
        dirname = input("Введите название папки: ")
        os.mkdir(dirname)

    if do == "5":
        break

