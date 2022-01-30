# Задание 1 Выяснить тип результата выражений:

print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

# Задание 2 На вход будет выдаваться список, пример:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# a) Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# b) Сформировать из обработанного списка строку:
#
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
#
#     Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!
#
# ВНИМАНИЕ! Используйте стартовый код для своей реализации:
#
# def convert_list_in_str(list_in: list) -> str:
#     """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
#         списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
#         Формирует из списка результирующую строковую переменную и возвращает."""
#     # пишите реализацию своей программы здесь
#     str_out = "здесь полученная после всех преобразования строковая переменная"
#     return str_out
#
#
# my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# result = convert_list_in_str(my_list)
# print(result)

def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    a = []
    for i in list_in:
        try:
            ins = int(i)
            ins = str(ins).zfill(2)
            if '+' in i: ins = '+' + ins
            if '-' in i: ins = '-' + ins
            a.append(['"', ins, '"'])
        except:
            a.append(i)

    str_out = ' '.join([''.join(i) if type(i) == list else i for i in a])
    return str_out

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)


#
# Задание 3
#
# *(вместо задачи 2) Решить задачу 2, не создавая новый список (как говорят, in place). Эта задача намного серьёзнее, чем может сначала показаться.

def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    i = 0
    while i < len(list_in):
        v = list_in[i]
        try:
            ins = int(v)
            ins = str(ins).zfill(2)
            if '+' in v: ins = '+' + ins
            if '-' in v: ins = '-' + ins
            del list_in[i]
            list_in.insert(i, ['"', ins, '"'])
            i += 1
            if 50 < i: break
        except:
            i += 1

    str_out = ' '.join([''.join(i) if type(i) == list else i for i in list_in])
    return str_out

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)


# Задание 4
#
# На вход будет подаваться список, содержащий искажённые данные с должностями и именами сотрудников:
#
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
#
# Известно, что имя сотрудника всегда в конце строки!
#
# Обработать все элементы списка и вернуть в качестве результата список, состоящий из фраз вида:
#
# ['Привет, Игорь!', 'Привет, Марина!', 'Привет, Николай!', 'Привет, Аэлита!']
#
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
#
# Можно ли при этом не создавать новый список?
#
# ВНИМАНИЕ! Используйте стартовый код для своей реализации:
#
# def convert_name_extract(list_in: list) -> list:
#     """Извлекает имена из элементов и формирует список приветствий."""
#     # пишите реализацию своей программы здесь
#     list_out = ["здесь должены оказаться результирующие строковые приветствия"]
#     return list_out
#
#
# my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# result = convert_name_extract(my_list)
# print(result)

def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    # пишите реализацию своей программы здесь
    list_out = [f'Привет, {i.split()[-1].title()}!' for i in list_in]
    return list_out

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)


# Задание 5
#
# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
#
# [57.8, 46.51, 97, ...]
#
# a) Привести каждый элемент списка к виду <r> руб <kk> коп и собрать их в одну строку через запятую. Пример:
#
# 57 руб 80 коп, 46 руб 51 коп ...
#
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
#
# b) Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
#
# c) Создать новый список, содержащий те же цены, но отсортированные по убыванию.
#
# d) Вернуть цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
#
# ВНИМАНИЕ! Используйте стартовый код для своей реализации:
#
# from random import uniform
#
#
# def transfer_list_in_str(list_in: list) -> str:
#     """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
#         формирует из них единую строковую переменную разделяя значения запятой."""
#     # пишите реализацию своей программы здесь
#     str_out = "здесь итоговая строка"
#     return str_out
#
#
# my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
# print(f'Исходный список: {my_list}')
# result_1 = transfer_list_in_str(my_list)
# print(result_1)
#
#
# def sort_prices(list_in: list) -> list:
#     """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
#     # пишите реализацию здесь
#     return ["отсортированный результирующий список"]
#
#
# # зафиксируйте здесь информацию по исходному списку my_list
# result_2 = sort_prices(my_list)
# # зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
# print(result_2)
#
#
# def sort_price_adv(list_in: list) -> list:
#     """Создаёт новый список и возвращает список с элементами по убыванию"""
#     # пишите реализацию здесь
#     list_out = ["список элементов в списке по убыванию"]
#     return list_out
#
#
# result_3 = sort_price_adv(my_list)
# print(result_3)
#
#
# def check_five_max_elements(list_in: list) -> list:
#     """Проверяет элементы входного списка вещественных чисел и возвращает
#         список из ПЯТИ максимальных значений"""
#     # пишите реализацию здесь
#     list_out = ["список из пяти самых больших элементов"]
#     return list_out
#
#
# result_4 = check_five_max_elements(my_list)
# print(result_4)
#
#     Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.



from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    # пишите реализацию своей программы здесь
    str_out = ', '.join([f'{str(int(i)).zfill(2)} руб {str(round(100*(i%1))).zfill(2)} коп' for i in list_in])
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    # пишите реализацию здесь
    list_in.sort()
    return list_in


# зафиксируйте здесь информацию по исходному списку my_list
id_my_list = id(my_list)
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
id_result_2 = id(result_2)
print(result_2)

print(id_my_list == id_result_2) # вернёт True


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    # пишите реализацию здесь
    list_out = sorted(list_in, reverse=True)
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    # пишите реализацию здесь
    list_out = sort_price_adv(list_in)[:5][::-1]
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
