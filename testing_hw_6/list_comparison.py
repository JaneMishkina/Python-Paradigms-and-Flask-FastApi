"""
Модуль для сравнения списков
"""


class ListComparer:
    """
    Класс для сравнения списков
    """

    def __init__(self, list1, list2):
        """
        Инициализирует экземпляр класса двумя списками
        """

        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, lst):
        """
        Рассчитывает среднее значение каждого списка
        """

        return sum(lst) / len(lst)

    def compare_lists(self):
        """
        Сравнивает средние значения двух списков
        """

        avg_list1 = self.calculate_average(self.list1)
        avg_list2 = self.calculate_average(self.list2)

        if avg_list1 > avg_list2:
            return "Первый список имеет большее среднее значение"
        if avg_list1 < avg_list2:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
