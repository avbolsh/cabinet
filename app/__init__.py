from flask import Flask

from config import Config
from app.extensions import db, migrate, admin, login
from app.models.user import User
from flask_admin.contrib.sqla import ModelView


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    login.init_app(app)

    login.login_view = 'auth.login'
    login.login_message = "Введите ваши логин и пароль"

    admin.add_view(ModelView(User, db.session))

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.hr_requests import bp as hr_requests_bp
    app.register_blueprint(hr_requests_bp, url_prefix="/hr-requests")

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    from app.api import bp as api_bp 
    app.register_blueprint(api_bp, url_prefix="/api")

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app