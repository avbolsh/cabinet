from flask import url_for, redirect, flash, request, render_template
from flask_login import current_user, login_user, logout_user
from app.auth import bp
from app.auth.forms import LoginForm
from app.models.user import User


@bp.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Неверные логин или пароль")
            return redirect(url_for("auth.login"))
        login_user(user, remember=form.remember_me.data)
    return render_template('auth/login.html', title=('Sign In'), form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))