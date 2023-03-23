#!/usr/bin/python3
"""This module contains the order's forms"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from inventory.models.user import OrderItem

class AddOrderForm(FlaskForm):
    """This class defines the registration form"""
    product = StringField('Product', validators=[DataRequired(), Length(min=2, max=100)])
    quantity = StringField('Quantity', validators=[DataRequired(), Length(min=2, max=100)])
    discount = StringField('Discount', validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Add Order')
