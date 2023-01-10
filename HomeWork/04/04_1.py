#заполнить список степенями числа 2(от 2^1 до 2^n)
if __name__ == '__main__':
    from random import randint
    list_2 = []

    for n in range(randint(1, 50)):
        list_2.append(2**n)

    print(list_2)
