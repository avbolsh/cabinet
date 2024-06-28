from flask import abort, jsonify
from flask_restful import Resource, reqparse
from .import rest_api
from app.models import User
from app.extensions import db
import json

parser = reqparse.RequestParser()

parser.add_argument("username", type=str)
parser.add_argument("email", type=str)
parser.add_argument("id", type=str)
parser.add_argument("password", type=str)
parser.add_argument("full_name", type=str)

class UserResource(Resource):

    def get(self, id=None, page=1):
        
        if not id:
            users = User.query.paginate(page=page, per_page=10).items
        else:
            users = User.query.get(id)
        
        if not users:
            abort(404)
        
        res = {}

        for user in users:
            res[user.id] = {
                "username": user.username,
                "email": user.email, 
                "full_name": user.full_name
            }
        
        return json.dumps(res, ensure_ascii=False) 

    def post(self):
        args = parser.parse_args()

        username = args["username"]
        full_name = args["full_name"]
        email = args["email"]
        password = args["password"]
        id = args["id"]

        new_user = User(username=username, email=email, id=id)
        new_user.set_password(password)
        db.session.add(new_user)
        try:
            db.session.commit()
        except:
            return abort(400, "Bad request")

        res = {}
        res[new_user.id] = {
            "username": new_user.username,
            "email": new_user.email
        }
        return jsonify(res)

    def delete(self, id):
        user = User.query.get(id)
    
        if not user:
            abort(404)

        db.session.delete(user)
        db.session.commit()

        return json.dumps({"respomse": "deleted"})


rest_api.add_resource(
    UserResource,
    "/users/", 
    "/users/<id>")
