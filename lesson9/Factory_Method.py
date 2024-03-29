__author__ = 'Соловьев Андрей Сергеевич.'

# Самостоятельно познакомиться с паттернами Factory (фабрика) и Factory method (фабричный метод) и решить следующую задачу:
# «Есть некоторый общий класс родитель Tag, который хранит в себе какой-то HTML тег (например: <tag></tag>). 
# От Tag наследуются еще четыре класса Image, Input, Text (т. е <p></p>), Link (т. е <a></a>).
# С использованием указанных паттернов реализовать следующее поведение: 
# Должна быть возможность создать необходимый тег, явно его не создавая, т. е не через img = Image(), 
# а через фабричный метод или фабрику, например factory.create_tag(name).»

# TODO:

# Паттерна Singleton

import functools


class Singleton:

    def singleton(cls):
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