from list_comparison import ListComparer
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

comparer = ListComparer(list1, list2)
comparer.compare_lists()

average = ListComparer(list1, list2)
average1 = average.calculate_average(list1)
average2 = average.calculate_average(list2)
print("Average of list1:", average1)
print("Average of list2:", average2)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
