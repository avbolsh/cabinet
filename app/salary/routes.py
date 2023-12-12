from flask import render_template
from app.salary import bp

@bp.route("/")
def index():
    return render_template("salary/index.html")

