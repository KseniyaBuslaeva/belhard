#заполнить словарь где ключами будут выступать числа от 0 до n,
# а значениями вложенный словарь с ключами "name"и "email",
# а значения для этих ключей будут браться с клавиатуры
if __name__ == '__main__':
    users_dict = {}

    for _ in range(0, 10):
        users_dict[_] = {'name': input('input user name: '), 'email': input('enter user email: ')}

    print(users_dict)
