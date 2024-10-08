from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from blueprints.auth import auth_bp
from blueprints.marketplace import marketplace_bp
from blueprints.transaction import transaction_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/palace_of_goods'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

from models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(marketplace_bp, url_prefix='/marketplace')
app.register_blueprint(transaction_bp, url_prefix='/transaction')

if __name__ == '__main__':
    app.run(debug=True)
