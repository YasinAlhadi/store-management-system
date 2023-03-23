#!/usr/bin/python3
"""This module contains the database storage engine"""
import sqlalchemy
"""from inventory.models.user import User"""
from inventory.models.user import User, Product, Order, OrderItem, Transaction
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


classes = {"User": User, "Product": Product, "Order": Order,
           "OrderItem": OrderItem, "Transaction": Transaction}

Base = declarative_base()

class DBStorage:
    """This class manages the database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """This method initializes the database storage engine"""
        self.__engine = create_engine('mysql+mysqldb://rms_dev:rms_y_pwd@localhost/rms_dev_db', pool_pre_ping=True)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.name
                    new_dict[key] = obj
        return (new_dict)
    
    def new(self, obj):
        """This method adds an object to the database"""
        self.__session.add(obj)
    
    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
    
    def get(self, cls, id):
        """get object"""
        if cls and id:
            key = cls.__name__ + '.' + id
            return self.all(cls).get(key)
        return None
