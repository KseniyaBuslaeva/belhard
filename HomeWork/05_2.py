#сделать калькулятор: у пользователя спрашивается число, потом действие и второе число
try:
    first_number = float(input('enter first number: '))
    operator = input('enter operator (+, -, *, /): ')
    operators = ['+', '-', '*', '/']
    while operator not in operators:
        operator = input('you should enter only one of this operator (+, -, *, /): ')
        continue
    second_number = float(input('enter second number: '))
    result = 0

    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    elif operator == '/':
        result = first_number / second_number

    print(first_number, operator, second_number, '=', result)
except Exception as error:
    print(error)
