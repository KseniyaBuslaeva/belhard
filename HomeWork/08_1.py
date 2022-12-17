#TODO Описать класButton, конструктор класса принимает width, height, text. Проверить
# аргументы на соответствие типам, в случае если типы не верные, вызвать
# исключение TypeError. Объявить атрибуты объекта на основании аргументов
# конструктора. Объявить атрибут объекта is_pressed со значением False.
# Объявить атрибут класса color со значением white. Объявить метод класса для
# изменения атрибута класса white с проверкой типа аргумента поступающего на
# вход метода, а также на проверку того, входит ли данное значение в список
# допустимых значений, в противном случае вызвать соответствующее
# исключение. Объявить метод объекта press изменяющий атрибут объекта
# is_pressed на противоположное значение. Написать магический метод __str__
# возвращающий текст кнопки. Написать метод объекта to_dict возвращающий
# словарь с ключами - название атрибутов, значения - значения атрибутов.
# Написать метод класса from_dict принимающий вход словарь с данными о
# кнопке и возвращающий новый объект данного класса.

class Button:
    button_colors = ['white', 'black', 'red', 'green', 'blue']

    def __init__(self, width: int, height: int, text: str) -> None:
        self.color = 'white'
        self.is_pressed = False
        self.width = width
        self.height = height
        self.text = text

        if not isinstance(width, int) or width < 0:
            raise TypeError
        if not isinstance(height, int) or height < 0:
            raise TypeError
        if not isinstance(text, str):
            raise TypeError

    def __str__(self):
        return self.text

    def change_color(self, new_color: str) -> None:
        if new_color in self.button_colors:
            self.color = new_color
        else:
            print('Button color should be in defined button colors')

    def press(self) -> None:
        if self.is_pressed:
            self.is_pressed = False
        else:
            self.is_pressed = True

    def to_dict(self):
        return {'width': self.width, 'height': self.height, 'text': self.text}

    def from_dict(self, new_dict: dict):
        self.width = new_dict[0]
        self.height = new_dict[1]
        self.text = new_dict[2]
        return self


ok_button = Button(width=45, height=34, text='OK')
ok_button.press()
ok_button.change_color(new_color='black1')

print(ok_button.color)
print(ok_button.is_pressed)
ok_button.press()
print(ok_button.is_pressed)
print(str(ok_button))
print(ok_button.to_dict())
ok_button.from_dict({0: 34, 1: 32, 2: 'exit'})
print(ok_button.to_dict())
