# backend/blueprints/__init__.py

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from backend.blueprints.auth import auth_blueprint
from backend.blueprints.products import products_blueprint
from backend.blueprints.transactions import transactions_blueprint
from backend.config import Config
from backend.database import db
from backend.models import User, Product, Transaction

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)
    
    # Load app configuration from config file
    app.config.from_object(Config)
    
    # Initialize CORS to allow cross-origin requests (important for frontend-backend communication)
    CORS(app)
    
    # Initialize JWT for authentication
    jwt = JWTManager(app)
    
    # Initialize SQLAlchemy with the app (DB connection)
    db.init_app(app)
    
    # Register blueprints for different modules
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(products_blueprint, url_prefix='/products')
    app.register_blueprint(transactions_blueprint, url_prefix='/transactions')

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    return app

