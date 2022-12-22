"""Реализовать класс Category
Создать атрибут класса categories
"""


class Category:
    categories = ['moto', 'bus', 'trolleybus', 'gipergar']

    """Написать метод класса add принимающий на вход название категории, если такой
    категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
    индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать ошибку
    ValueError"""

    def add(self, category: str) -> int:
        if category in self.categories:
            raise ValueError('element is already in list')
        else:
            self.categories.append(category)
            return self.categories.index(category)

    """Написать метод класса get принимающий индекс и возвращающий категорию из списка
    категорий на этом индексе, если нет элемента на таком индексе, вызвать атрибут ValueError"""

    def get(self, index: int) -> str:
        try:
            return self.categories[index]
        except:
            raise ValueError('index is outbound list')

    """Написать метод класса delete принимающий индекс категории в списке категорий и
    удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
    индексе, ничего не делать, метод ничего возвращать не должен"""

    def delete(self, index: int):
        if index < len(self.categories):
            self.categories.pop(index)

    """Написать метод update принимающий индекс категорий и новое название категории, если
    нет элемента на таком индексе, то новая категория должна добавляться с учетом того, что
    имена категорий уникальны, если новое имя категории нарушает уникальность в списке
    категорий, вызвать исключение ValueError"""

    def update(self, index: int, category_new_name: str):
        if index < len(self.categories) and self.categories.count(category_new_name) < 1:
            self.categories[index] = category_new_name
        elif self.categories.count(category_new_name) > 0:
            raise ValueError('category already in list')
        elif index < len(self.categories):
            self.categories.append(category_new_name)


cat1 = Category()
# print(cat1.add('autobus'))
# print(cat1.get(6))
# cat1.delete(-1)
print(cat1.categories)
cat1.update(3, 'buss')
print(cat1.categories)
