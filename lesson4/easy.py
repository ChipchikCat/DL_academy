__author__ = 'Соловьев Андрей Сергеевич.'
# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили

# TODO:

km = int(input("Введите количество километров: "))


def convert(km):
    miles = km / 1.609
    print(f"{miles} миль.")


convert(km)

# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# TODO:

def my_round(number, ndigits):
    int_ndigits = int(ndigits)
    degree = pow(10, int(ndigits))
    mul = number*degree
    res = int(mul)
    ost = mul-res
    # print(number,mul,res,ost)
    if not (abs(ost) < 0.5):
        if res > 0:
            res += 1
        else:
            res -= 1
    return res/degree


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

# TODO:

def lucky_ticket(ticket_number):
    str_ticket_number = str(ticket_number)
    if len(str_ticket_number) == 6:
        first_sum = 0
        for i in str_ticket_number[0:3]:
            first_sum += int(i)
        second_sum = 0
        for i in str_ticket_number[3:]:
            second_sum += int(i)
        if first_sum == second_sum:
            return True
        else:
            return False
    else:
        return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
