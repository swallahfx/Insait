import os

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    # Create Flask app instance
    app = Flask(__name__)

    load_dotenv()

    # Configure app using environment variables
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    app.config["FLASK_ENV"] = os.getenv("FLASK_ENV", "development")

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints for routes
    from app.routes.test_route import question_bp

    app.register_blueprint(question_bp)

    return app
