#Дан список чисел, необходимо его развернуть без использования метода revese и
#функции reversed, а так же дополнительного списка и среза
if __name__ == '__main__':
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 45, 23, 2]
    index = len(numbers_list) - 1
    while index >= 0:
        numbers_list.append(numbers_list[index])
        index -= 1

    length = len(numbers_list) / 2
    while index < length - 1:
        numbers_list.pop(0)
        index += 1

    print(numbers_list)

