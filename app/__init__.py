from flask import Flask

from config import Config
from app.extensions import db, migrate, admin
from app.models.user import User
from flask_admin.contrib.sqla import ModelView


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)

    admin.add_view(ModelView(User, db.session))

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)


    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app