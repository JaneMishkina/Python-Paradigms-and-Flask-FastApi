"""Предположим, что мы хотим найти элемент в массиве (получить
его индекс). Мы можем это сделать просто перебрав все элементы.
Но что, если массив уже отсортирован? В этом случае можно
использовать бинарный поиск. Принцип прост: сначала берём
элемент находящийся посередине и сравниваем с тем, который мы
хотим найти. Если центральный элемент больше нашего,
рассматриваем массив слева от центрального, а если больше -
справа и повторяем так до тех пор, пока не найдем наш элемент.
Ваша задача:
Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве"""

#Итерационный метод реализации бинарного поиска. Императивная (процедурная) парадигма.

def binary_search (num_list, to_search):
    first_index = 0
    last_index = len(num_list) -1
    mid_index = (last_index + first_index)//2
    mid_element = num_list[mid_index]

    is_found = True
    while is_found:
        if first_index == last_index:
            if to_search != mid_element:
                is_found = False
                return "Number is not in the list"
        elif mid_element == to_search:
            return f"{mid_element} is on the position {mid_index}"
        elif mid_element > to_search:
            new_position = mid_index - 1
            last_index = new_position
            mid_index = (first_index + last_index)//2
            mid_element = num_list[mid_index]
            if mid_element == to_search:
                return f"{mid_element} is on the position {mid_index}"
        elif mid_element < to_search:
            new_position = mid_index + 1
            first_index = new_position
            last_index = len(num_list) -1
            mid_index = (first_index + last_index) // 2
            mid_element = num_list[mid_index]
            if mid_element == to_search:
                return f"{mid_element} is on the position {mid_index}"

#list_num = [16 , 18 , 20 , 50 , 60 , 81 , 89]
list_num = list(map(int, input().split()))
print(binary_search(list_num, 81))