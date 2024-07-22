from flask import Blueprint

bp = Blueprint("hr_requests", __name__)

from app.hr_requests import routes