import random
from collections import Counter


def input_array(max_range = 100):

    n = 0
    while True:
        try:
            n = int(input("n = "))
            if n <= 0:
                raise ValueError("n phải là số dương.")
            break
        except ValueError as e:
            pass

    so_list = [random.randint(1, max_range + 1) for _ in range(n)]

    return so_list


def find_counter_max(array):
    dict = {}

    for item in array:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1

    max_count = max(dict, key=dict.get)
    find_count = dict[max_count]

    print(f'số xuất hiện nhiều nhất {max_count}, xuất hiện {find_count} lần')

if __name__ == '__main__':
    list = input_array()

    print('danh sách ngẫun nhiên: ',end='')
    print(list)

    condition = lambda x: x % 2 ==0
    even_list = [item for item in list if condition(item)]

    if(even_list == []):
        print('danh sách không có số chẵn')
    else:
        print('danh sách số chẵn trong list: ',end='')
        print(even_list)

    find_counter_max(list)