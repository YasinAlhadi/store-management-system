#!/usr/bin/python3
"""This module contains a user routes"""
from flask import render_template, url_for, flash, redirect, request
from  inventory.models.user_forms import RegistrationForm, LoginForm
from inventory.models.user import User
from flask_login import login_user, current_user, logout_user, login_required, LoginManager
from inventory import app, bcrypt, storage



@app.route("/")
@app.route("/home")
def home():
    """home page"""
    return render_template('home.html')

@app.route("/adduser", methods=['GET', 'POST'])
def adduser():
    """add new user"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(roleid=form.roleid.data, name=form.full_name.data, phone=form.phone.data, address=form.address.data, email=form.email.data, password=hash_pwd)
        storage.new(user)
        storage.save()
        flash(f'User has been added!', 'success')
        return redirect(url_for('adduser'))
    return render_template('adduser.html', title='Add User', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    """login user
    if current_user.is_authenticated:
        return redirect(url_for('home'))"""
    form = LoginForm()
    if form.validate_on_submit():
        user = storage.all(User).values()
        for u in user:
            if u.email == form.email.data :
                if bcrypt.check_password_hash(u.password, form.password.data):
                    login_user(u, remember=form.remember.data)
                """next_page = request.args.get('next')"""
                redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    """logout user"""
    logout_user()
    return redirect(url_for('login'))

@app.teardown_appcontext
def teardown_db(exception):
    """close the database"""
    storage.close()
