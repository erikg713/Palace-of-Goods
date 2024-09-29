from flask import Flask
from .config import Config
from .routes import auth, products, transactions

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(auth)
    app.register_blueprint(products)
    app.register_blueprint(transactions)

    return app

