#заполнить список степенями числа 2(от 2^1 до 2^n)
if __name__ == '__main__':
    exp = int(input('Введите степень: '))
    list_2 = []

    for n in range(1, exp):
        list_2.append(2**n)

    print(list_2)
