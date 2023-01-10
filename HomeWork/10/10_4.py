"""Дан CSV файл с данными о товарах (article, title, description, price)
Необходимо считать файл, привести к списку словарей, выполнить
приведение типов значений атрибута price, провести валидацию данных
с помощью Pydantic, не верные записи вывести в другой файл, а из
списка удалить"""
import csv
from pydantic import BaseModel

with open('10_4.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    list_dict = list(reader)


print(list_dict)

class GoodsModel(BaseModel):
    article: str
    title: str
    description: str
    price: float

goods = GoodsModel(list_dict)
