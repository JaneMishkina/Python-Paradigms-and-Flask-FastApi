"""Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
сортировки числа в списке в порядке убывания. Пример сортировки слиянием."""

def merge_sort_desc(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2
    left_half = numbers[:middle]
    right_half = numbers[middle:]

    left_half = merge_sort_desc(left_half)
    right_half = merge_sort_desc(right_half)

    merged = []
    i = 0
    j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] > right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    while i < len(left_half):
        merged.append(left_half[i])
        i += 1

    while j < len(right_half):
        merged.append(right_half[j])
        j += 1

    return merged

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = merge_sort_desc(numbers)
print("Отсортированный массив в порядке убывания:", sorted_numbers)

"""Эта же сортирвка, но в декларативном стиле"""

def merge_sort_desc(numbers):
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left_half = numbers[:mid]
    right_half = numbers[mid:]

    left_half = merge_sort_desc(left_half)
    right_half = merge_sort_desc(right_half)

    return merge_desc(left_half, right_half)

def merge_desc(left_half, right_half):
    merged = []
    i = 0
    j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] > right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    while i < len(left_half):
        merged.append(left_half[i])
        i += 1

    while j < len(right_half):
        merged.append(right_half[j])
        j += 1

    return merged

nums = [64, 34, 25, 12, 22, 11, 90]
sorted_nums = merge_sort_desc(nums)
print("Отсортированный массив в порядке убывания:", sorted_nums)
