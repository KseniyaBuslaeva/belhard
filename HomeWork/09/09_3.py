"""Изменить класс выше, список категорий должен содержать не просто имена категорий, а
словари с данными о каждой категории (name: str, is_published: bool)"""


class Category:
    categories = [
        {'name': 'comedy', 'is_published': False},
        {'name': 'thriller', 'is_published': True},
        {'name': 'romantic', 'is_published': False}]

    @classmethod
    def add(cls, category: dict) -> int:
        if category in cls.categories:
            raise ValueError('element is already in list')
        else:
            cls.categories.append(category)
            return cls.categories.index(category)

    @classmethod
    def get(cls, index: int) -> dict:
        try:
            return cls.categories[index]
        except:
            raise ValueError('index is outbound list')

    @classmethod
    def delete(cls, index: int):
        if index < len(cls.categories):
            cls.categories.pop(index)

    @classmethod
    def update(cls, index: int, category_new_name: dict):
        if index < len(cls.categories) and len(list(filter(lambda item: item['name'] == category_new_name['name'], cls.categories))) < 1:
            cls.categories[index] = category_new_name
        elif cls.categories.count(category_new_name) > 0:
            raise ValueError('category already in list')
        elif index < len(cls.categories):
            cls.categories.append(category_new_name)

    """Добавить метод make_published принимающий индекс категории и меняющий значение
    ключа is_published на True, если такого индекса нет, вызвать исключение ValueError"""

    @classmethod
    def make_published(cls, index: int):
        if index < len(cls.categories):
            cls.categories[index].update({'is_published': True})
        else:
            raise ValueError('index is outbound categories list')

    """Добавить метод make_unpublished принимающий индекс категории и меняющий
    значение ключа is_published на False, если такого индекса нет, вызвать исключение
    ValueError"""

    @classmethod
    def make_unpublished(cls, index: int):
        if index < len(cls.categories):
            cls.categories[index].update({'is_published': False})
        else:
            raise ValueError('index is outbound categories list')

#
# cat = Category()
# cat.make_published(0)
# cat.make_unpublished(1)
# cat.make_published(6)

#
# cat1 = Category()
# print(cat1.add({'name': 'autobus', 'is_published': True}))
# print(cat1.get(1))
# # cat1.delete(-1)
# print(cat1.categories)
# cat1.update(1, {'name': 'autobus', 'is_published': True})
# print(cat1.categories)
