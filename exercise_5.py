"""
Модуль 2 Python Advanced, Урок №5. Інтегратори та генератори, Вправа 5

Реалізуйте ітератор для перебору всіх ключів словника.

Приклад можливо подивитись у презентації до уроку

dictionary = {"a": 1, "b": 2, "c": 3}
dict_iter = DictKeysIterator(dictionary)
for key in dict_iter:
print(key)

a
b
c
"""

class DictKeysIterator:
    """
    ітератор для перебору всіх ключів словника
    """

    def __init__(self, dict_atrib):
        self.keys_list = list(dict_atrib.keys())
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > len(self.keys_list) - 1:
            raise StopIteration
        result = self.keys_list[self.i]
        self.i += 1
        return result


dictionary = {"a": 1, "b": 2, "c": 3}

dict_iter = DictKeysIterator(dictionary)

for key in dict_iter:
    print(key)
