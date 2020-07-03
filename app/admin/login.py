import app
from app import db

from werkzeug.urls import url_parse

from app.models import User, Category
from app.api.forms import LoginForm
from flask import (
    Blueprint, request, render_template, make_response, abort, session, redirect, url_for
)

from flask_login import (
    login_user,
    logout_user,
    current_user
)

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('intro.index'))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        remember_me = form.remember_me.data
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login.index'))
        login_user(user, remember=remember_me)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('intro.index')
        return redirect(next_page)
  
    return render_template('admin/login.html',
                            title='Sign In',
                            form=form
                            )


@login.route('/logout')
def logout():
    logout_user()


