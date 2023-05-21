'''write the code for auth blueprint here '''
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user

from webapp import db
from webapp.models.User import User
from webapp.forms import LoginForm, RegistrationForm

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        # Check if user exists and password is correct
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password', 'danger')
            return redirect(url_for('auth.login'))

        # Log user in
        login_user(user, remember=form.remember_me.data)
        flash('You have been logged in', 'success')

        # Redirect user to page they were trying to access before logging in
        next_page = request.args.get('next')
        if next_page is None or not next_page.startswith('/'):
            next_page = url_for('home.home')
        return redirect(next_page)

    return render_template('auth/login.html', title='Login', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('home.home'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data)
        user.set_password(form.password.data)

        # Add user to the database
        db.session.add(user)
        db.session.commit()
        flash('You have been registered', 'success')

        # Log user in
        login_user(user)

        return redirect(url_for('home.home'))

    return render_template('auth/register.html', title='Register', form=form)



