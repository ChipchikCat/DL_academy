# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

TODO:
fruits = ["apple", "banana", "qiwi", "watermelon"]
for number, fruit in enumerate(fruits, start=1):
    print(f"{number}. {fruit:>10}")

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# TODO:
cars = ['bmw', 'audi', 'toyota', 'subaru', 'honda', 'suzuki', 'volvo', 'geely']
print(f"Оригинальный список: {cars}")

del (cars[0], cars[4], cars[5])
print(f"Список без дубликатов: {cars}")

motorcycle = ['suzuki', 'bmw', 'ducati','yamaha', 'ninja', 'honda', 'kawasaki']
print(f"Оригинальный список: {motorcycle}")


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

# TODO:
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []
for i in range(len(integers)):
    if integers[i] % 2 == 0:
        new_list.append(integers[i] / 4)
    else:
        new_list.append(integers[i] * 2)
print(new_list)
