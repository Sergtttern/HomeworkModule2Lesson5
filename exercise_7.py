"""
Модуль 2 Python Advanced, Урок №5. Інтегратори та генератори, Вправа 7

Створіть ітератор, який перебирає всі парні числа з заданого діапазону.

Приклад можливо подивитись у презентації до уроку

"""

class EvenNumbersFromRange:
    """
    ітератор, який перебирає всі парні числа з заданого діапазону
    """

    def __init__(self, start, end):
        self.i = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.end:
            raise StopIteration
        elif self.i % 2 == 0:
            result = self.i
            self.i += 1
            return result
        else:
            pass
            self.i += 1
            return next(self)


my_iterator = EvenNumbersFromRange(1,10)

for element in my_iterator:
    print(element)
