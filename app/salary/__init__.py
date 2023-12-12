from flask import Blueprint

bp = Blueprint("salary", __name__)

from app.salary import routes