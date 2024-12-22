from app.routes.test_route import question_bp


def register_routes(app):
    app.register_blueprint(question_bp, url_prefix="/api")
