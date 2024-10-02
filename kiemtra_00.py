def input_list() :
    n = int(input("Nhập số phần tử cho list: "))
    my_list = []

    # Sử dụng for loop
    for i in range(n):
        element = input(f"Nhập phần tử thứ {i + 1}: ")
        my_list.append(element)

    print("List:", my_list)

def input_tupple():
    n = int(input("Nhập số phần tử cho tuple: "))
    temp_list = []

    i = 0
    while i < n:
        element = input(f"Nhập phần tử thứ {i + 1}: ")
        temp_list.append(element)
        i += 1

    my_tuple = tuple(temp_list)
    print("Tuple:", my_tuple)

def input_set():
    n = int(input("Nhập số phần tử cho set: "))
    my_set = set()

    # Sử dụng for loop
    for i in range(n):
        element = input(f"Nhập phần tử thứ {i + 1}: ")
        my_set.add(element)

    print("Set:", my_set)

def input_dict():
    n = int(input("Nhập số phần tử cho dictionary: "))
    my_dict = {}
    i = 0
    while i < n:
        key = input(f"Nhập key thứ {i + 1}: ")
        value = input(f"Nhập value cho key {key}: ")
        my_dict[key] = value
        i += 1

    print("Dictionary:", my_dict)


if __name__ == '__main__':
    input_list()