__author__ = 'Соловьев Андрей Сергеевич.'

# Реализовать тестирование в вашем приложении «чата» (два предыдущих дз).
#
# Основные требования:
# Как юнит определить функцию (т.е. надо написать тесты для всех ваших функций и методов). 
# Возможны исключения для вашей реализации. Разделите тесты клиента и сервера на два (или более) раздельных файла.
#
# *Дополнительно:
# Написать тесты для всех домашних заданий.

# TODO :
from lesson9 import Factory_Method
import functools


class Singleton:

    def test__singleton(cls):
        cls = "test"
        assert test__sigleton(cls)== "Test_pattern"
        @functools.wraps(cls)
        def wrapper(*args, **kwargs):
            if not wrapper.instance:
                wrapper.instance = cls(*args, **kwargs)
            return wrapper.instance
        wrapper.instance = None
        return wrapper

    @singleton
    class TheOne:
        pass
