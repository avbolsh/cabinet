from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField


class HrRequestForm(FlaskForm):
    title = StringField("Тема заявки")
    body = TextAreaField("Содержание")
    submit = SubmitField("Отправить")
    