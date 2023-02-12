# Урок 4. Оценка и интерпретация полученной модели

## Задание

1. Расскажите, как работает регуляризация в решающих деревьях, какие параметры мы штрафуем в данных алгоритмах?
2. По какому принципу рассчитывается "важность признака (feature_importance)" в ансамблях деревьев?

## Ответы

### Задача 1

Регуляризация препятствует переобучению модели.
В решающих деревьях, где нет функции потерь и сложно сделать L1/L2 регуляризацию,
используется регуляризация путём штрафа параметров:

- max_depths - ограничение глубины дерева
- max_leaves - ограничение количества листьев

Помимо этого может делаться "Стрижка деревьев", удаляющая листья с низким критерием информативности.

### Задача 2

Важность признака определяет то, насколько сильно меняется прогноз от изменения значения признака.
Чем больше важность, тем сильнее влияние на прогноз.

В ансамблях деревьев есть следующие способы расчёта важности признаков:

- Через искобчение признаков и замере эффекта, который они вносили в предсказание.
- С помощью "индекса Джини" или "среднего уменьшения примеси (изменчивости)".
Для этого вычисляется суммарное снижения информативности (impurity)
узлов с весами. Они рассчитываются для каждого узла как отношение примеров
достигших данного узла к общему количетву примеров в обучающей выборке.
Важность признаков расчитыватся усреднением по всем деревьям ансамбля.