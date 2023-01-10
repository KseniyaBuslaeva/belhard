# TODO На вход функции подается упорядоченный список чисел и некоторое число,
#  реализовать бинарный поиск данного числа в списке

def binary_search(num_list: list, num: int):
    min_index = 0
    max_index = len(num_list) - 1
    mid = len(num_list) // 2

    while num_list[mid] != num and min_index <= max_index:
        if num > num_list[mid]:
            min_index = mid + 1
        else:
            max_index = mid - 1
        mid = (min_index + max_index) // 2

    if min_index > max_index:
        print("Not in list")
    else:
        print("Position = ", mid)
    pass


if __name__ == '__main__':

    from random import randint

    n_list = []
    for i in range(10):
        n_list.append(randint(-100, 100))
    n_list.sort()
    print(n_list)

    n = int(input('enter num: '))

    binary_search(n_list, n)