from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from .routes import auth_bp, transactions_bp, products_bp, contracts_bp, error_handlers

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(transactions_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(contracts_bp)

    # Register error handlers
    app.register_error_handler(Exception, error_handlers.handle_error)

    return app
