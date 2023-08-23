"""
Модуль 2 Python Advanced, Урок №5. Інтегратори та генератори, Вправа 4

Напишіть генератор, який видає послідовність квадратів чисел від 1 до N.

Приклад можливо подивитись у презентації до уроку

"""
print(100*'*')
print("Варіант 1: Генератор у вигляді ф-ї")
def sequence_of_squares_of_numbers(n:int):
    """
    генератор, який видає послідовність квадратів чисел від 1 до N
    """

    for i in range(1,n+1):
        yield i*i


number = 10

my_generator = sequence_of_squares_of_numbers(number)

for res_pow in my_generator:
    print(res_pow)

print(100*'*')
print("Варіант 2: Генератор списка.")

my_generator_2 = [i*i for i in range(1,number+1)]
print(my_generator_2)

for j in my_generator_2:
    print(j)


# res = [i for i in range(1,11) if i%2 == 0]
# print(res)
# i*i for i in range(1,11)]

print(100*'*')
print("Варіант 2: Генератор який використовує генератор обжект.")

my_generator_3 = (i*i for i in range(1,number+1))
print(my_generator_3)

for j in my_generator_3:
    print(j)

print(100*'*')

# my_generator_4 = {i*i for i in range(1,number+1)}
# print(my_generator_4)
#
# for j in my_generator_4:
#     print(j)
