"""Изменить класс выше, список категорий должен содержать не просто имена категорий, а
словари с данными о каждой категории (name: str, is_published: bool)"""


class Category:
    categories = [
        {'name': 'comedy', 'is_published': False},
        {'name': 'thriller', 'is_published': True},
        {'name': 'romantic', 'is_published': False}]

    def add(self, category: dict) -> int:
        if category in self.categories:
            raise ValueError('element is already in list')
        else:
            self.categories.append(category)
            return self.categories.index(category)

    def get(self, index: int) -> dict:
        try:
            return self.categories[index]
        except:
            raise ValueError('index is outbound list')

    def delete(self, index: int):
        if index < len(self.categories):
            self.categories.pop(index)

    def update(self, index: int, category_new_name: dict):
        if index < len(self.categories) and len(list(filter(lambda item: item['name'] == category_new_name['name'], self.categories))) < 1:
            self.categories[index] = category_new_name
        elif self.categories.count(category_new_name) > 0:
            raise ValueError('category already in list')
        elif index < len(self.categories):
            self.categories.append(category_new_name)

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
