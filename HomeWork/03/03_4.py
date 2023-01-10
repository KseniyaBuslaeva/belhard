#Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
if __name__ == '__main__':
    try:
        first_number = float(input('Enter the first number: '))
        second_number = float(input('Enter the second number: '))
        third_number = float(input('Enter the third number: '))

        positive_count = (first_number > 0) + (second_number > 0) + (third_number > 0)
        negative_count = (first_number < 0) + (second_number < 0) + (third_number < 0)

        print('Positive numbers: {}. Negative numbers {}.'.format(positive_count, negative_count))
    except ValueError:
        print('You should enter only a numbers!!!')
