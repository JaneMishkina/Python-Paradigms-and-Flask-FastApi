"""Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами)."""
# Использована функциональная парадигма
import math


def mean(values):
    """Вычисляет среднее значение списка"""
    return sum(values) / len(values)


def pearson_correlation(x, y):
    """
        Вычисляет корреляцию Пирсона между двумя массивами
        Возвращает:
        correlation -- значение корреляции Пирсона
        """
    n = len(x)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_squared = sum(xi ** 2 for xi in x)
    sum_y_squared = sum(yi ** 2 for yi in y)

    numerator = (n * sum_xy) - (sum_x * sum_y)
    denominator = math.sqrt((n * sum_x_squared - sum_x ** 2) * (n * sum_y_squared - sum_y ** 2))

    correlation = numerator / denominator
    return correlation


# Пример использования
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

correlation = pearson_correlation(x, y)
print("Корреляция Пирсона:", correlation)

"""В этом примере используются две функции: mean, которая вычисляет среднее значение массива, и pearson_correlation, 
которая реализует формулу корреляции Пирсона. После определения этих функций, можно передать свои массивы x и y 
функции pearson_correlation, чтобы вычислить корреляцию, а затем вывести результат на экран."""
"""Этот скрипт оценивает только линейную корреляцию между двумя случайными величинами."""
