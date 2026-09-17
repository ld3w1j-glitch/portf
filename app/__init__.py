from flask import Flask
from config import Config
from .db import close_db, init_db


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    app.config["DATABASE"] = app.config.get("DATABASE") or "instance/portfolio.sqlite3"
    app.teardown_appcontext(close_db)
    with app.app_context():
        init_db()

    from .routes import main
    app.register_blueprint(main)
    return app
