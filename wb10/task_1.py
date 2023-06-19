# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string

def generator_random_name(start, end = None):
    """
    функция генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
    """

    alf = list(string.ascii_lowercase)
    while True:
        random.shuffle(alf)
        word1 = ''.join(alf[random.randint(1, 15):])
        word2 = ''.join(alf[:random.randint(1, 15)])
        yield word1 + ' ' + word2

gen = generator_random_name(0)
print(next(gen))
print(next(gen))
print(next(gen))

