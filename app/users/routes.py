from flask import render_template, redirect, flash, url_for
from app.users import bp
from .forms import LoginForm

@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for {form.username.data}, remember_me={form.remember_me.data}")
        return redirect(url_for("main.index")) 
    return render_template("users/login.html", form=form)