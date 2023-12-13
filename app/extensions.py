from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
admin = Admin(name="Полет", template_mode="bootstrap4")