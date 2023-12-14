from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from sqlalchemy import Column, String
from sqlalchemy import Uuid
import uuid


class User(UserMixin, db.Model):
    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    snils = Column(String(14), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))
    fullname = Column(String(100))
    first_name = Column(String(50))
    last_name = Column(String(50))
    surname = Column(String(50))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_passwoord(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"<User {self.fullname}>"


@login.user_loader
def load_user(id):
    return User.query.get(uuid.UUID(id))

