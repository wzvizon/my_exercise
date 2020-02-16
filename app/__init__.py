from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

db = SQLAlchemy()


def create_app(config_class=DevConfig):
    app = Flask(__name__)

    # Configure app wth the settings from config.py
    app.config.from_object(config_class)

    # Allow the app to access to the database
    db.init_app(app)

    with app.app_context():
        db.Model.metadata.reflect(db.engine)

    from app.main.routes import bp_main
    app.register_blueprint(bp_main)

    return app
