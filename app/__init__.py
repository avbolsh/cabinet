from flask import Flask

from config import Config
from app.extensions import db, migrate
from app.models.user import User

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Инициализируем тут расширения
    db.init_app(app)
    migrate.init_app(app, db)

    # Регистрируем блюпринты
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.salary import bp as salary_bp
    app.register_blueprint(salary_bp, url_prefix="/salary")

    @app.route("/ping/")
    def test_page():
        return "pong!"
    
    return app