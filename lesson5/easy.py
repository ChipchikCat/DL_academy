__author__ = 'Соловьев Андрей Сергеевич.'
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

# TODO:

list1 = [42, 202, 333, -4, -5, 5, 0, 2, 111, 2022, 101]
list2 = [i ** 2 for i in list1]
print(list2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# TODO:

fruits = ["лимон", "персик", "банан", "хурма", "груша", "aпельсин", "мандарин","яблоко"]
fruits_2 = ["банан", "киви", "арбуз", "яблоко", "гранат", "манго", "апельсин","слива","груша"]
copy_fruits = [i for i in fruits if i in fruits_2]
print(copy_fruits)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

# TODO:

numbers = [11, 52, 13, 2, 3, -66, 72, 81, -14, 18, -21, 12, 27, -277, 2.06, 67.242, -78.54, 66.74]
numbers_2 = [i for i in numbers if i % 3 == 0 and i > 0 and i % 4 != 0]
print(numbers_2)
