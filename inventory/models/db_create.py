#!/usr/bin/python3
"""This module contains the classes for the database"""
from user import User, Product, Order, OrderItem, Transaction, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://rms_dev:rms_y_pwd@localhost/rms_dev_db',
                                pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()
    session.close()