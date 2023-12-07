"""Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами)."""
# Использована функциональная парадигма
import math


def pearson_correlation(x, y):
    """
        Вычисляет корреляцию Пирсона между двумя массивами
        Возвращает:
        correlation -- значение корреляции Пирсона
        """

    n = len(x)
    median_x = sum(x) / n  # среднее арифметическое массива х
    median_y = sum(y) / n  # среднее арифметическое массива у
    numerator = sum([(xi - median_x) * (yi - median_y) for xi, yi in zip(x, y)])
    denominator = math.sqrt(sum([((xi - median_x) ** 2) * ((yi - median_y) ** 2) for xi, yi in zip(x, y)]))
    correlation = numerator / denominator
    return correlation


# Пример использования
x = [1, 2, 3, 4, 6]
y = [2, 4, 6, 8, 11]

correlation = pearson_correlation(x, y)
print("Корреляция Пирсона:", correlation)


