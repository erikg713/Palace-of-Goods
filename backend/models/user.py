from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    wallet_address = db.Column(db.String(256), nullable=False)
    private_key = db.Column(db.String(256), nullable=False)
    products = db.relationship('Product', backref='owner', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'wallet_address': self.wallet_address
        }
