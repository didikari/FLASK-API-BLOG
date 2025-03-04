from flask import Flask
from app.config import Config
from app.extensions import db, migrate
from app.routes import register_routes
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    JWTManager(app)

    register_routes(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
