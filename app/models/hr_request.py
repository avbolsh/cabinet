from sqlalchemy import Column, String, Integer, Text, DateTime
from app.extensions import db
from datetime import datetime


class Hr_Request(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    body = Column(Text)
    created = db.Column(DateTime, default=datetime.now())
    user_id = Column(String(36), db.ForeignKey('user.id'))