from flask import render_template
from app.main import bp
from flask_login import login_required


@bp.route("/")
@login_required
def index():
    return render_template("index.html")


@bp.route("/profile/")
@login_required
def profile():
    return render_template("main/profile.html")
