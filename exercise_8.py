"""
Модуль 2 Python Advanced, Урок №5. Інтегратори та генератори, Вправа 8

Напишіть генератор, який видає послідовність простих чисел.

Приклад можливо подивитись у презентації до уроку

"""

def generator_that_produces_sequence_of_prime_numbers(start, end):
    """
    генератор, який видає послідовність простих чисел
    """

    for i in range(start,end+1):
        result = True
        if i == 1:
            result = False

        for j in range(2, end + 1):
            if (i != j) and (i % j == 0):
                # print(f"{i} ділиться на {j} без остачі")
                result = False
                # print(f"i={i}, j={j}, result = {result}")

        if result:
            yield i

my_generator = generator_that_produces_sequence_of_prime_numbers(1,100)
for element in my_generator:
    print(element)
