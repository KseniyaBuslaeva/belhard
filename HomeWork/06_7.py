#Дан список чисел, необходимо для каждого элемента посчитать сумму его
#соседей, для крайних чисел одним из соседей является число с противоположной
#стороны списка
if __name__ == '__main__':
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 45, 23, 2]
    summ_list = []
    max_index = len(numbers_list) - 1
    for index in range(max_index + 1):
        if index == 0:
            summ_list.append(numbers_list[max_index] + numbers_list[1])
            continue
        elif index == max_index:
            summ_list.append(numbers_list[index - 1] + numbers_list[0])
            continue

        summ_list.append(numbers_list[index - 1] + numbers_list[index + 1])

    print(summ_list)
