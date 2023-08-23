"""
Модуль 2 Python Advanced, Урок №5. Інтегратори та генератори, Вправа 3

Створіть ітератор який буде приймати рядок та кожен виклик методу next() буде повертати наступний символ рядку.

Приклад можливо подивитись у презентації до уроку

"""


class NextSymbol:
    """
    ітератор який приймає рядок та кожен виклик методу next() повертає наступний символ рядку.
    """

    def __init__(self, str_param):
        self.str_param = str_param
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > len(self.str_param) - 1:
            raise StopIteration
        result = self.str_param[self.i]
        self.i += 1
        return result


str_var = "Привіт!"

my_iterator = NextSymbol(str_var)

for char in my_iterator:
    print(char)
