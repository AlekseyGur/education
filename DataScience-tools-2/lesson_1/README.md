# Урок 1. Введение в задачу классификации. Постановка задачи и подготовка данных

## Задание

1. Приведите по 2 примера, когда лучше максимизировать Precision, а когда Recall.
2. Почему мы используем F-меру, почему, например, нельзя просто взять среднее от Precision и Recall?

## Ответы

### Задача 1

При решении задачи построения модели для рекомендации товаров:

Precision = tp / (tp + fp) - это какой % от рекомендованных товаров купил пользователь. Есть ещё метрика "Precision@k", в которой
считается то же самое, но список рекомендованных ранжируется по релеватности для конкретного пользователя
и берётся только первые "k" товаров. Обычно k небольшое - от 5 до 20. Есть ещё метрика "MoneyPrecision@k" -
это выручка от использования "Precision@k" (то есть сумма цен купленных товаров), отнесённая к
суммарной цене всех товаров в "Precision@k" (чтоб не было размерности).

Precision выгодно максимизировать в тех случаях, когда fp решения очень негативно влиют на конечное решение.
Например, начинаем лечить человека, который не является больным, теряя деньги на лечение.

Recall = tp / (tp + fn) - это какой % среди купленных товаров был среди рекомендованных. Эта метрика похож на Precision,
но в знаменателе будет не количество рекомендованных, а количество купленных товаров. Аналогично предыдущей
метрике есть "Recall@k" и "Recall@k".

Recall выгодно максимизировать в тех случаях, когда fn решения очень негативно влиют на конечное решение.
Например, даём кредит тому человеку, который никогда не выплатит его, хотя подумали, что он сможет.

### Задача 2

F-мера используется для учёта ошибок и первого и второго рода одновременно. Она включает в себя и Precision, и Recall.
Причем в F-меру входит параметр бетта, с помощью которого можно регулировать, что именно должно больше
оказывать влияние на эту меру: Precision или Recall