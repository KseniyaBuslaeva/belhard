"""Изменить класс выше, список категорий должен содержать не просто имена категорий, а
словари с данными о каждой категории (name: str, is_published: bool)"""


class Category:
    categories = [
        {'name': 'comedy', 'is_published': True},
        {'name': 'thriller', 'is_published': True},
        {'name': 'romantic', 'is_published': False}]

    def __init__(self):
        pass

    """Добавить метод make_published принимающий индекс категории и меняющий значение
    ключа is_published на True, если такого индекса нет, вызвать исключение ValueError"""

    def make_published(self, index: int) -> bool:
        if index < len(self.categories):
            print('ggg')
        pass


cat = Category()
cat.make_published(2)
