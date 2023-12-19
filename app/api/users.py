from app.api import bp
from flask import request
from app.api.errors import bad_request
from app.models.user import User
from app import db
from flask import jsonify

@bp.route("/users/<string:id>", methods=["GET"])
def get_user(id):
    return "hello"
    pass

@bp.route("/users/", methods=["GET"])
def get_users():
    pass

@bp.route("/users/", methods=["POST"])
def create_user():
    data = request.get_json() or {}
    if "username" not in data or "snils" not in data or "id" not in data:
        return bad_request("must include: username, snils, id")
    if User.query.get(data["id"]):
        return bad_request("there is a user with this id")
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify({"user": user.username})
    response.status_code = 201
    return response
     


@bp.route("/users/<string:id>", methods=["PUT"])
def update_user(id):
    pass

