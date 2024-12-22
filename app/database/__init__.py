# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
#
# def init_db(app):
#     app.config['SQLALCHEMY_DATABASE_URI'] = app.config.get('DATABASE_URL')
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db.init_app(app)


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    """Initialize the database with the Flask app."""
    db.init_app(app)
