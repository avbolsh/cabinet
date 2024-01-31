from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField(('Логин'), validators=[DataRequired("Необходимо указать логин")])
    password = PasswordField(('Пароль'), validators=[DataRequired("Необходимо указать пароль")])
    remember_me = BooleanField(('Запомнить меня'))
    submit = SubmitField(('Войти'))