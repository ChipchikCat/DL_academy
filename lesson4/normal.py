__author__ = 'Соловьев Андрей Сергеевич.'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# TODO:

def fibonacci(n, m):
    fib_list = [1, 1]

    for i in range(m):
        new_element = fib_list[-1] + fib_list[-2]
        fib_list.append(new_element)
    print(fib_list)


fibonacci(0, 10)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

# TODO:

def sort_to_max(origin_list):
    lenght = len(origin_list)
    for i in range(lenght):
        for j in range(0, lenght - i - 1):
            if origin_list[j] > origin_list[j + 1]:
                temp = origin_list[j]
                origin_list[j] = origin_list[j + 1]
                origin_list[j + 1] = temp
    return origin_list


origin_list = ([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
result = sort_to_max(origin_list)
print(result)


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

# TODO:

numbers = [1,2,3,4,5,6,7,11,121,222,221,20,-20,-100,10.5,-100.7]

def filter_odd_num(in_num):
    if (in_num % 2) == 0:
        return True
    else:
        return False
    
out_filter = filter(filter_odd_num, numbers)

print("Отфильтрованный список: ", list(out_filter))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# TODO:

import math

A1 = [2, 1]
A2 = [3, 5]
A3 = [6, 6]
A4 = [5, 2]

B1 = [1, 1]
B2 = [1, 5]
B3 = [5, 5]
B4 = [5, 1]

C1 = [1, 1]
C2 = [5, 5]
C3 = [1, 5]
C4 = [5, 1]


def is_paral(a1, a2, a3, a4):
    def cos_angle(b1, b2, b3):
        a = (b1[0] - b2[0]) * (b1[0] - b3[0]) + (b1[1] - b2[1]) * (b1[1] - b3[1])
        b = math.sqrt((b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2)
        c = math.sqrt((b1[0] - b3[0]) ** 2 + (b1[1] - b3[1]) ** 2)
        return a / (b * c)

    cos_a1 = cos_angle(a1, a2, a4)
    cos_a2 = cos_angle(a2, a3, a1)
    cos_a3 = cos_angle(a3, a4, a2)
    cos_a4 = cos_angle(a4, a3, a1)
    if cos_a1 == cos_a3 and cos_a2 == cos_a4 and (cos_a1 + cos_a2) == 0.0 and (cos_a3 + cos_a4) == 0.0:
        return True
    else:
        return False

print(is_paral(A1, A2, A3, A4))
print(is_paral(B1, B2, B3, B4))
print(is_paral(C1, C2, C3, C4))

