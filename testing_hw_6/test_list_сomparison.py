import pytest
from list_comparison import ListComparer


def test_calculate_average():
    """
    Test for calculate_average function
    """
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 6, 7, 8, 9]
    comparer = ListComparer(list1, list2)
    assert comparer.calculate_average(list1) == 3.0
    assert comparer.calculate_average(list2) == 7.0


def test_compare_lists_first_more():
    """
    Test for compare_lists function when the first list has a greater average value
    """
    list1 = [5, 6, 7, 8, 9]
    list2 = [1, 2, 3, 4, 5]
    comparer = ListComparer(list1, list2)
    assert "Первый список имеет большее среднее значение" in comparer.compare_lists()


def test_compare_lists_second_more():
    """
    Test for compare_lists function when the second list has a greater average value
    """
    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 6, 8, 10]
    comparer = ListComparer(list1, list2)
    assert "Второй список имеет большее среднее значение" in comparer.compare_lists()


def test_compare_lists_equal():
    """
    Test for compare_lists function when the lists have equal average values
    """
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 4, 3, 2, 1]
    comparer = ListComparer(list1, list2)
    assert "Средние значения равны" in comparer.compare_lists()
