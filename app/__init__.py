from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics

db = SQLAlchemy()

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@db/Database_db"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app():
    """Construct the core application."""
    app = Flask(__name__)

    db.init_app(app)
    PrometheusMetrics(app)

    with app.app_context():
        from . import routes  # Import routes

        db.create_all()  # Create sql tables for our data models

        return app
