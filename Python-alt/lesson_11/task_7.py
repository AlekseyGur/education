# ## Задание 7
# Реализовать проект `Операции с комплексными числами`.
# * Создать класс `Комплексное число`.
# * Реализовать перегрузку методов `сложения` и `умножения` комплексных чисел.
# * Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение
# созданных экземпляров.
# * Проверить корректность полученного результата.


class Complex():
    """комплексные числа"""
    def __init__(self, value: complex):
        self.value = value

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __truediv__(self, other):
        return  self.value / other
