"""
Модуль 2 Python Advanced, Урок №5. Інтегратори та генератори, Вправа 9

Створіть ітератор, який перебирає всі паліндроми (слова, які читаються однаково зліва направо та зправа наліво)
з заданого списку слів.

Приклад можливо подивитись у презентації до уроку

"""
list_of_words = ['level', 'racecar', 'python', 'madam']
class OutputsWordsPolynomials:
    """
    ітератор, який перебирає всі паліндроми (слова, які читаються однаково зліва направо та зправа наліво)
    з заданого списку слів
    """

    def __init__(self, list_of_words_param):
        self.list_of_words_param = list_of_words_param
        self.number_of_word_in_list_param = 0

    def __iter__(self):
        return self

    def __next__(self):
        # for word in self.list_of_words_param:
        while self.number_of_word_in_list_param < len(self.list_of_words_param):

            word = self.list_of_words_param[self.number_of_word_in_list_param]
            i = 1
            s2 = ""
            while i < len(word) + 1:
                s2 = s2 + word[-i]
                i += 1

            if word == s2:
                self.number_of_word_in_list_param += 1
                return word
            else:
                self.number_of_word_in_list_param += 1
                # return next(self)

        raise StopIteration


my_iterator = OutputsWordsPolynomials(list_of_words)
print(my_iterator)

for element in my_iterator:
    print(element)
