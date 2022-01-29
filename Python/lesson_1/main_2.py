# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

#Примеры:

#duration = 53
#53 сек
#duration = 153
#2 мин 33 сек
#duration = 4153
#1 час 9 мин 13 сек
#duration = 400153
#4 дн 15 час 9 мин 13 сек

duration = int(input('Сколько секунд? '))
days = duration // 86400
hours = (duration % 86400) // 3600
minutes = (duration % 3600) // 60
seconds = duration % 60

if days:
    print(f'{days} дн {hours} час {minutes} мин {seconds} сек')
elif hours:
    print(f'{hours} час {minutes} мин {seconds} сек')
elif minutes:
    print(f'{minutes} мин {seconds} сек')
else:
    print(f'{seconds} сек')

#2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):

a = [i**3 for i in range(1, 1001) if i % 2 != 0]

b = []
for i in a:
    s = 0
    for n in str(i):
        s += int(n)
    if s % 7 == 0:
        b.append(i)

print(sum(b))

#Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
#К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#* Решить задачу под пунктом b, не создавая новый список.

a = [i + 17 for i in a]

for idx, val in enumerate(a):
    s = 0
    for n in str(val):
        s += int(n)
    if s % 7 == 0:
        del a[idx]

print(sum(a))

#3.Склонение слова
#Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

#1 процент
#2 процента
#3 процента
#4 процента
#5 процентов
#6 процентов
#...
#100 процентов

for i in range(1,101):
    if i in [11,12,13,14,15,16,17,18,19,20]: ending = 'ов'
    elif int(str(i)[-1]) == 1: ending = ''
    elif int(str(i)[-1]) in [2,3,4]: ending = 'а'
    else: ending = 'ов'

    print(f'{i} процент{ending}')
