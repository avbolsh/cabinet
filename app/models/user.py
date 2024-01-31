import uuid
from sqlalchemy import Column, String
from app.extensions import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from app import login


class User(UserMixin, db.Model):
    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    username = Column(String(100), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password_hash = Column(String(256))

    def set_password(self, passwod):
        self.password_hash = generate_password_hash(passwod)

    def check_password(self, passwod):
        return check_password_hash(self.password_hash, passwod)

@login.user_loader
def login_user(id):
    return db.session.get(User, id)    