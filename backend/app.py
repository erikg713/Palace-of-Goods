from flask import Flask
from config import config
from models import db, login_manager
from blueprints.auth import auth_bp
from blueprints.marketplace import marketplace_bp
from blueprints.transaction import transaction_bp

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(marketplace_bp, url_prefix='/marketplace')
    app.register_blueprint(transaction_bp, url_prefix='/transaction')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
