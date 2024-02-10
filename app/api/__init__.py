
from flask import Blueprint
from flask_restful import Api

bp = Blueprint("api", __name__)

rest_api = Api(bp)

from . import routes