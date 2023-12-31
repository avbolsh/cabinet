from flask import Flask

from config import Config
from app.extensions import db, migrate, login, admin
from app.models.user import User
from app.models.ticket import Ticket
from flask_admin.contrib.sqla import ModelView

class CustomModelView(ModelView):
    column_display_pk = True
    column_display_all_relations = True
    column_auto_select_related = True
    column_searchable_list = ('id',)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Инициализируем тут расширения
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    admin.init_app(app)
    admin.add_view(CustomModelView(User, db.session))
    admin.add_view(CustomModelView(Ticket, db.session))

    # Регистрируем блюпринты
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.salary import bp as salary_bp
    app.register_blueprint(salary_bp, url_prefix="/salary")

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    @app.route("/ping/")
    def test_page():
        return "pong!"
    
    return app