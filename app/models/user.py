from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from sqlalchemy import Column, String
import uuid

def uuid_to_str():
    return str(uuid.uuid4())


class User(UserMixin, db.Model):
    id = Column(String(36), primary_key=True, default=uuid_to_str)
    username = Column(String(50), unique=True)
    snils = Column(String(14), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))
    fullname = Column(String(100))
    first_name = Column(String(50))
    last_name = Column(String(50))
    surname = Column(String(50))
    tickets = db.relationship("Ticket", backref="author", lazy="dynamic")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_passwoord(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"<User {self.fullname}>"

    def from_dict(self, data, new_user=False):
        for field in ["username", "snils", "id", "fullname"]:
            if field in data:
                setattr(self, field, data[field])
        if new_user and "password" in data:
            self.set_password(data["password"])


@login.user_loader
def load_user(id):
    return User.query.get(id)
