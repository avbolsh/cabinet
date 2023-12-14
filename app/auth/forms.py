from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    snils = StringField("Страховой номер ПФР", validators=[DataRequired(message="Это поле обязательно для заполнения")])
    password = PasswordField("Пароль", validators=[DataRequired(message="Это поле обязательно для заполнения")])
    remember_me = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")
