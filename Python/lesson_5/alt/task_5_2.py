# Задание 2 *(вместо 1)
#
# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
#
# Задание 1
#
# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
#
# $ odd_to_15 = odd_nums(15)
# $ next(odd_to_15)
# 1
# $ next(odd_to_15)
# 3
# ...
# $ next(odd_to_15)
# 15
# $ next(odd_to_15)
# ...StopIteration...
#
# ВНИМАНИЕ! Используйте стартовый код для своей реализации:
#
# def odd_nums(number: int) -> int:
#     """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
#     pass  # пишите свою реализацию здесь
#
#
# n = 15
# generator = odd_nums(n)
# for _ in range(1, n+1, 2):
#     print(next(generator))
# # next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration


import typing

def odd_nums(number: int) -> typing.Generator:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    return (x for x in range(1, number + 1) if x % 2 != 0)


n = 15
generator = odd_nums(n)
for _ in range(1, n+1, 2):
    print(next(generator))

# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
