#TODO Описать класButton, конструктор класса принимает width, height, text. Проверить
# аргументы на соответствие типам, в случае если типы не верные, вызвать
# исключение TypeError. Объявить атрибуты объекта на основании аргументов
# конструктора. Объявить атрибут объекта is_pressed со значением False.
# Объявить атрибут класса color со значением white. Объявить метод класса для
# изменения атрибута класса white с проверкой типа аргумента поступающего на
# вход метода, а также на проверку того, входит ли данное значение в список
# допустимых значений, в противном случае вызвать соответствующее
# исключение. Объявить метод объекта press изменяющий атрибут объекта
# is_pressed на противоположное значение. Написать магический метод str
# возвращающий текст кнопки. Написать метод объекта to_dict возвращающий
# словарь с ключами - название атрибутов, значения - значения атрибутов.
# Написать метод класса from_dict принимающий вход словарь с данными о
# кнопке и возвращающий новый объект данного класса.

class Button:
    button_colors = ['white', 'black', 'red', 'green', 'blue']
    color = 'white'

    def __init__(self, width: int, height: int, text: str) -> None:

        if not isinstance(width, int) or width < 0:
            raise TypeError('width should greater then 0')
        if not isinstance(height, int) or height < 0:
            raise TypeError('height should be greater then 0')
        if not isinstance(text, str):
            raise TypeError('text button should be a string')

        self.is_pressed = False
        self.width = width
        self.height = height
        self.text = text

    def __str__(self):
        return self.text

    @classmethod
    def change_color(cls, new_color: str) -> None:
        if new_color in cls.button_colors:
            cls.color = new_color
        else:
            print(new_color, 'is not defined button color !!!!')
            TypeError('No Value')

    def press(self) -> None:
        if self.is_pressed:
            self.is_pressed = False
        else:
            self.is_pressed = True

    def to_dict(self):
        return {'width': self.width, 'height': self.height, 'text': self.text}

    @classmethod
    def from_dict(cls, new_dict: dict):
        cls.width = new_dict['width']
        cls.height = new_dict['height']
        cls.text = new_dict['text']
        return cls


ok_button = Button(width=45, height=34, text='OK')
ok_button.press()
ok_button = Button(width=5, height=34, text='back')
print('button pressed: ', ok_button.is_pressed)

ok_button.change_color(new_color='black')
print('current button color is: ', ok_button.color)

ok_button.change_color(new_color='yellow')


ok_button.press()
print('button pressed: ', ok_button.is_pressed)

print('current button text is: ', str(ok_button))
print(ok_button.to_dict())
new_button = ok_button.from_dict({'width': 20, 'height': 10, 'text': 'exit'})
print('width: ', new_button.width, 'height', new_button.height, 'button text:', new_button.text)