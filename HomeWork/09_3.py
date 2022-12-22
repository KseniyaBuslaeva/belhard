"""Изменить класс выше, список категорий должен содержать не просто имена категорий, а
словари с данными о каждой категории (name: str, is_published: bool)"""


class Category:
    categories = [
        {'name': 'comedy', 'is_published': False},
        {'name': 'thriller', 'is_published': True},
        {'name': 'romantic', 'is_published': False}]

    def __init__(self):
        pass

    """Добавить метод make_published принимающий индекс категории и меняющий значение
    ключа is_published на True, если такого индекса нет, вызвать исключение ValueError"""

    def make_published(self, index: int):
        if index < len(self.categories):
            self.categories[index].update({'is_published': True})
        else:
            raise ValueError('index is outbound categories list')

    """Добавить метод make_unpublished принимающий индекс категории и меняющий
    значение ключа is_published на False, если такого индекса нет, вызвать исключение
    ValueError"""

    def make_unpublished(self, index: int):
        if index < len(self.categories):
            self.categories[index].update({'is_published': False})
        else:
            raise ValueError('index is outbound categories list')


cat = Category()
cat.make_published(0)
cat.make_unpublished(1)
cat.make_published(6)
