# https://medium.com/@george.shuklin/why-you-cant-remove-parent-methods-in-python-d4935e6d54a4

# в питоне все методы класса по умолчанию считаются виртуальными, т.е. можно переопределять любой метод в любой момент
# если вы хотите запретить производному классу использовать какие-то методы базового класса - придется удалить их. например, в конструкторе класса-наследника:
class BaseClass():
    def __init__(self):
        pass

    def method_to_kill(self):
        print("Этому методу не повезло :(")

    def method_will_live(self):
        print("А этот метод пусть живет")

class DerivedClass(BaseClass):
    def __init__(self):
        print("Убираем ненужные методы при инициализации")
        # чтобы удалить метод базового класса, указывайте явно базовый класс (BaseClass.имя_метода)
        del BaseClass.method_to_kill

test_class = DerivedClass()
test_class.method_will_live()
test_class.method_to_kill()
