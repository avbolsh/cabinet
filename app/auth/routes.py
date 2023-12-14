from flask import render_template, redirect, flash, url_for
from app.auth import bp
from .forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models.user import User
from app import login as login_namager


@bp.route("/login/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(snils=form.snils.data).first()
        
        if user is None or not user.check_passwoord(form.password.data):
            flash("Неверные логин или пароль")
            return redirect(url_for("auth.login"))
        
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("main.index")) 
    
    return render_template("auth/login.html", form=form)


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@login_namager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for("auth.login"))


@bp.route("/profile/<snils>")
@login_required
def user(snils):
    user = User.query.filter_by(snils=snils).first_or_404()
    return render_template("auth/profile.html", user=user)