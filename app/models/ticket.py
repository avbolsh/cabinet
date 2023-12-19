from app import db
from sqlalchemy import Column, Integer, String, DateTime, Uuid, ForeignKey, Enum
from datetime import datetime


class Ticket(db.Model):
    id = Column(Integer, primary_key=True)
    body = Column(String(140))
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)
    user_id = Column(String(36), ForeignKey("user.id"))
    type = Column(Enum("Справка 2-НДФЛ", "Справка с места работы", "Справка по использованным отпускам"))

    def __repr__(self):
        return f"<Ticket {self.body}>"