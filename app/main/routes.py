from flask import render_template
from app.main import bp
from flask_login import login_required


@bp.route("/")
@login_required
def index():
    return render_template("main/index.html")

@bp.route("/vacation")
def vacation():
    return render_template("main/vacation.html", day_of_vacation=5)