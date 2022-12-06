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

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# TODO:
