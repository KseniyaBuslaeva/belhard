#Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путём форматирования 3-мя способами
if __name__ == '__main__':
    try:
        name = input('Enter you name: ')
        age = int(input('Enter you age: '))
        city = input('Enter you city: ')

        print('Hello ' + name + '. Your age is ' + str(age) + '. You are from ' + city)
        print('Hello {}. Your age is {}. You are from {}'.format(name, age, city))
        print('Hello {0}. Your age is {1}. You are from {2}'.format(name, age, city))
        print('Hello {str_name}. Your age is {str_age}. You are from {str_city}'.format(str_name=name, str_age=str(age), str_city=city))
    except ValueError:
        print('Age should be a number!!!')
