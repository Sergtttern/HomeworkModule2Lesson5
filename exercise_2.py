"""
Модуль 2 Python Advanced, Урок №5. Інтегратори та генератори, Вправа 2

Напишіть генератор, який повертає послідовність чисел Фібоначчі.

Приклад можливо подивитись у презентації до уроку
"""
number = 100


def sequence_of_fibonacci_numbers(n:int):
    """
    генератор, який повертає послідовність чисел Фібоначчі
    """
    before_the_previous_one = 0
    previous_element = 1
    for i in range(0, n):
        if i == 0:
            yield 0
        elif i == 1:
            yield 1
        else:
            sum_of_two_elements_of_the_sequence = before_the_previous_one + previous_element
            yield sum_of_two_elements_of_the_sequence
            before_the_previous_one = previous_element
            previous_element = sum_of_two_elements_of_the_sequence


my_generator = sequence_of_fibonacci_numbers(number)

for num in my_generator:
    print(num)
