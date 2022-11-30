#Пользователь вводит 3 числа, найти среднеарифметическое с точностью 3
if __name__ == '__main__':
    try:
        first_number = float(input('Enter the first number: '))
        second_number = float(input('Enter the second number: '))
        third_number = float(input('Enter the third number: '))

        average = round((first_number + second_number + third_number) / 3, 3)
        print(average)
    except ValueError:
        print('You should enter only numbers!!!')
