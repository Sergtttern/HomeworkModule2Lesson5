"""
Модуль 2 Python Advanced, Урок №5. Інтегратори та генератори, Вправа 6

Напишіть генератор, який фільтрує непарні числа з заданої послідовності.

Приклад можливо подивитись у презентації до уроку

"""
list_of_numbers = [1,2,3,4,5,6,7,8,9,10]

def filters_odd_numbers_from_sequence(list_of_numbers_param):
    """
    генератор, який фільтрує непарні числа з заданої послідовності
    """

    for i in range(1,len(list_of_numbers_param)):
        if list_of_numbers_param[i] % 2 == 0:
            yield list_of_numbers_param[i]


my_generator = filters_odd_numbers_from_sequence(list_of_numbers)

for element in my_generator:
    print(element)
