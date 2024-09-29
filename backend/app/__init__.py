from flask import Flask
from .config import Config
from .routes import auth_bp, products_bp, transactions_bp  # Update with new routes
from .routes.auth import auth_bp
from .routes.products import products_bp
from .routes.transactions import transactions_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(transactions_bp)

    return app