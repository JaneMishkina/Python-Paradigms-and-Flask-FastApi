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