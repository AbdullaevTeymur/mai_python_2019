# хорошая статья про декораторы https://python-scripts.com/decorators

# ДЕКОРАТОРЫ
# декоратор - это функции-обертки, которые позволяют сделать дополнение к уже существующей функции. Внимание: поведение самой функции вы изменить не сможете.
# но, например, сможете провести дальнейшую обработку результата, возвращаемого из функции, или добавить вывод информации для пользователя

# пример: пусть существует простая функция a_simple, которая умеет только возвращать строку, содержащую арифметическое выражение "1+1"
# считать она не может, поэтому создадим вторую функцию a_complex, которая способна вычислять выражение, которое возвращает a_simple
# как это работает: 1) в a_complex передается указатель на a_simple, 2) функция вычисляет значение и возвращает результат,
# 3) если бы мы остановились на 2), это был бы стандартный вызов функции. Но нам нужна функция-обертка, поэтому a_complex возвращает не результат расчета "1+1",
# а функцию, которая все это делает.
# Обратите внимание: т.к. в переменную decorator возвращается функция, ее тоже нужно вызвать (с круглыми скобками без параметров)
import sys

def a_complex(fun):
    def custom_calculator():
        return eval(fun())
    return custom_calculator

def a_simple():
    return "1+1"

decorator = a_complex(a_simple)
print(decorator())

# однако можно упростить себе жизнь: чтобы вызвать функцию-декоратор, мы просто "декорируем" исходную функцию, записывая перед ней название функции-обертки со знаком @
# после этого мы просто вызываем исходную функцию. Пример:

def a_complex(fun):
    def custom_calculator():
        return eval(fun())
    return custom_calculator

@a_complex
def a_simple():
    return "1+1"

print(a_simple())
# вместо
# decorator = a_complex(a_simple)
# print(decorator())

# пример с a_simple, возвращающей "1+1", может показаться надуманным, однако именно так работают системы символьной математики,
# которые вычисляют ввод пользователя. Или, например, такое пригодится для вычисления Польской нотации https://ru.wikipedia.org/wiki/Польская_нотация

# =============
# также декоратор можно использовать для документирования вызова кода - достаточно создать обертку-логгер и использовать ее как декоратор для любой функции

# библиотека для логирования
# https://python-scripts.com/logging-python
# https://docs.python.org/2/library/logging.html
import logging

def log(func):
    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler("%s.log" % name)
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.info("Вызов функции: %s" % name)
        # info("Вызов функции: %s" % name)
        result = func(*args, **kwargs)
        # logger.info("Результат: %s" % result)
        logger.info("Результат: %s" % result)
        return func

    return wrap_log

@log
def a_simple():
    return "1+1"

# обратите внимание: функция, декорированная логером, ничего не пишет на экране! она пишет лог-файл с именем, соответствующим имени функции
# поэтому ищите файл a_simple.log
result = a_simple()
print(f"Результат вызова функции a_simple - это функция: {result}")

# ДЕКОРАТОРЫ В КЛАССАХ
# "встроенные" декораторы: @classmethod, @staticmethod, @property
# до тех пор, пока вы не используете наследование, декораторы @classmethod и @staticmethod ведут себя одинаково: они делают так,
# что декорированную ими функцию можно вызывать как из экземпляра класса, так и статически из самого класса
# при наследовании @classmethod будет относиться к классу-наследнику, а @staticmethod - к базовому (родительскому) классу

# http://qaru.site/questions/10955/meaning-of-classmethod-and-staticmethod-for-beginner очень хороший пример про @static и @classmethod
class Date(object):
    __now = "18/11/2019"

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

    @staticmethod
    def millenium(month, day):
        return Date(month, day, 2000)

    @classmethod
    def millenium2(cls, month, day):
        return cls(month, day, 2000)

    # пара декораторов @property для метода now (get) и @now.setter (set) используются вместо связки now = property(get_now, set_now)
    @property
    def now(self):
        return self.__now

    @now.setter
    def now(self, val):
        self.__now = val

    # декораторы заменяютт собой прямое название getter и setter:
    # def get_now(self):
    #     return self.__now
    #
    # def set_now(self, val):
    #     self.__now = val
    #
    # now = property(get_now, set_now)


# ПРИМЕР
date2 = Date.from_string('11-09-2012')

class MyDate(Date):
    pass

# создаем экземпляр класса MyData - наследника Date
mydate = MyDate()
# вызываем @staticmethod и @classmethod
millenium = mydate.millenium(12, 31)
millenium2 = mydate.millenium2(12, 31)

print("Пытаемся поменять значение, возвращаемое классом, полученным методом millenium2 (@classmethod):")
print(f"Метод millenium2 принадлежит классу {type(millenium2)}")
print(f"millenium2 is MyDate: {isinstance(millenium2, MyDate)}")
print(millenium2.now)
millenium2.now = "19/11/2019"
print(millenium2.now)
print("Пытаемся поменять значение, возвращаемое классом, полученным методом millenium (@staticmethod):")
print(f"Метод millenium принадлежит классу {type(millenium)}")
print(f"millenium is MyDate: {isinstance(millenium, MyDate)}")
print(millenium.now)
millenium.now = "19/11/2019"
print(millenium.now)

