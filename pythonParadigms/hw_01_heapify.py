"""Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
сортировки числа в списке в порядке убывания. Пример пирамидальной сортировки."""


def heapify(numbers, size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and numbers[i] > numbers[left]:
        largest = left

    if right < size and numbers[largest] > numbers[right]:
        largest = right

    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i]

        heapify(numbers, size, largest)


def heapSort(numbers):
    n = len(numbers)

    for i in range(n, -1, -1):
        heapify(numbers, n, i)

    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)

    return numbers

nums = [64, 34, 25, 12, 22, 11, 90]
heapSort(nums)
print("Отсортированный массив в порядке убывания:", nums)

