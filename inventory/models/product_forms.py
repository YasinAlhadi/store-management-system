#!/usr/bin/python3
"""This module contains the product's forms"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
from inventory.models.user import Product

class AddProductForm(FlaskForm):
    """This class defines the registration form"""
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    price = StringField('Price', validators=[DataRequired(), Length(min=2, max=100)])
    quantity = StringField('Quantity', validators=[DataRequired(), Length(min=2, max=100)])
    description = StringField('Description', validators=[DataRequired(), Length(min=5, max=100)])
    submit = SubmitField('Add Product')

    def validate_name(self, name):
        """This method validates the email"""
        from inventory import storage
        product = storage.all(Product).values()
        for p in product:
            if p.name == name.data:
                raise ValidationError('That product is added. Please enter new one.')