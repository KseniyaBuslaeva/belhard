#Дан список чисел и на вход поступает число N, необходимо сместить список на
#указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]
if __name__ == '__main__':
    numbers_list = [1, 2, 3, 4, 5, 6, 7]
    num = int(input('enter number: '))
    print(numbers_list[num + 1::] + numbers_list[0:num + 1])

