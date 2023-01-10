#Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
#четные, потом нечётные
if __name__ == '__main__':
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 45, 23, 2]
    even = []
    odd = []

    for index in range(len(numbers_list) - 1):
        if numbers_list[index] % 2:
            odd.append(numbers_list[index])
        else:
            even.append(numbers_list[index])

    print(even + odd)


