from sqlalchemy import Column, INT, VARCHAR, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Category(Base):
    __tablename__ = 'categories'

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(24), nullable=False, unique=True)
    is_published = Column(Boolean, default=True, nullable=False)


class Products(Base):
    __tablename__ = 'product'

    id = Column(INT, primary_key=True)
    title = Column(VARCHAR(36), nullable=False)
    description = Column(VARCHAR(140), nullable=True)
    category_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)


class User(Base):
    __tablename__ = 'users'

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(24), nullable=False)
    email = Column(VARCHAR(24), nullable=False, unique=True)


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(INT, primary_key=True)
    order_id = Column(INT, ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
    product_id = Column(INT, ForeignKey('products.id', ondelete='CASCADE'), nullable=False)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(INT, primary_key=True)
    status_id = Column(INT, ForeignKey('statuses.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(INT, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)


class Status(Base):
    __tablename__ = 'statuses'

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(10), nullable=False, unique=True)
