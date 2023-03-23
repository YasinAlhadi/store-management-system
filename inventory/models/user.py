#!/usr/bin/python3
"""This module contains the classes for the database"""
from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin


"""
from inventory import login_manager
from inventory import storage

@login_manager.user_loader
def load_user(user_id):
    This function loads the user
    return storage.get(User, user_id)
"""
Base = declarative_base()

class User(Base, UserMixin):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    roleid = Column(Integer, nullable=False)
    name = Column(String(128), nullable=False)
    phone = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

class Product(Base):
    """This class defines a product by various attributes"""
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    description = Column(String(128), nullable=False)
    price = Column(String(128), nullable=False)
    quantity = Column(String(128), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

class Order(Base):
    """This class defines an order by various attributes"""
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(Integer, nullable=False), ForeignKey('users.id')
    total = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    user = relationship('User', backref='orders')

class OrderItem(Base):
    """This class defines an order item by various attributes"""
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, nullable=False), ForeignKey('orders.id')
    product_id = Column(Integer, nullable=False), ForeignKey('products.id')
    quantity = Column(Integer, nullable=False)
    subtotal = Column(Float, nullable=False)
    discount = Column(Float, nullable=False, default=0.0)
    grandtotal = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    order = relationship('Order', backref='order_items')
    product = relationship('Product', backref='order_items')

class Transaction(Base):
    """This class defines a transaction by various attributes"""
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    order_id = Column(Integer, nullable=False), ForeignKey('orders.id')
    userid = Column(Integer, nullable=False), ForeignKey('users.id')
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    order = relationship('Order', backref='transactions')