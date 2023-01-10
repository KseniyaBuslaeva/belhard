#Вывести четные числа от 2 до N по 5 в строку
try:
    range_end = int(input('enter end of range: '))
    i = 0
    for num in range(2, range_end, 2):
        i += 1
        print(num, end=' ')
        if i > 4:
            print()
            i = 0
except:
    print('range should be a number!!!')
