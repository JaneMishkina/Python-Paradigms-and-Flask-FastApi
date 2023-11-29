"""Задача №1
Дан список целых чисел numbers. Необходимо написать в Императивном стиле процедуру для
сортировки числа в списке в порядке убывания. Пример пузырьковой сортировки
"""
def bubble_sort_descending(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

nums = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_descending(nums)
print("Отсортированный массив в порядке убывания:", nums)


"""Задача №2
Написать точно такую же процедуру, но в декларативном стиле"""

def bubble_sort_descending(numbers):
    return sorted(numbers, reverse=True)


nums = [64, 34, 25, 12, 22, 11, 90]
sorted_nums = bubble_sort_descending(nums)
print("Отсортированный массив в порядке убывания:", sorted_nums)