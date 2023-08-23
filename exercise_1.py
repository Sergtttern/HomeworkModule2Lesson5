"""
Модуль 2 Python Advanced, Урок №5. Інтегратори та генератори, Вправа 1

Змініть функцію even_odd_generator так, щоб вона генерувала послідовність чисел від 1 до n з рядками "Fizz" для чисел,
які діляться на 3, "Buzz" для чисел, які діляться на 5, і "FizzBuzz" для чисел, які діляться як на 3, так і на 5.

Приклад можливо подивитись у презентації до уроку
"""

number = 100


def even_odd_generator(n):
    """
    генерує послідовність чисел від 1 до n з рядками "Fizz" для чисел,
    які діляться на 3, "Buzz" для чисел, які діляться на 5, і "FizzBuzz" для чисел, які діляться як на 3, так і на 5.
    """
    for i in range(1, n+1):
        if (i % 3 == 0) and (i % 5 == 0):
            yield f"{i} - FizzBuzz"
        elif i % 5 == 0:
            yield f"{i} - Buzz"
        elif i % 3 == 0:
            yield f"{i} - Fizz"


# Створення генератора
my_generator = even_odd_generator(number)

# for i in range(1, number +1):
#     print(next(my_generator))

for num in my_generator:
    print(num)
