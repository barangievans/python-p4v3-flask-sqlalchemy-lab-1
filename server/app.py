# server/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from models import Earthquake  # Ensure your models are imported here
        db.create_all()  # Create tables if not already created

    return app

app = create_app()
