from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    # Initializing core flask application
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('config.Config')

    # Initializing flask extensions
    db.init_app(app)
    bcrypt.init_app(app)
    # CORS(app)

    with app.app_context():
        # Include our Routes
        from . import routes

        # Create tables for our models
        db.create_all()

        return app
