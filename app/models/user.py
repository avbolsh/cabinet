from app.extensions import db
from flask_login import UserMixin
from app import login
from sqlalchemy import Column, String, Integer, Uuid
import uuid


class User(UserMixin, db.Model):
    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    snils = db.Column(db.String(14), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    fullname = Column(String(100))
    first_name = Column(String(50))
    last_name = Column(String(50))
    surname = Column(String(50))

@login.user_loader
def load_user(id):
    return User.query.get(int(id))