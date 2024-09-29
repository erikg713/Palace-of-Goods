from models import User, db
from flask_jwt_extended import create_access_token

class AuthService:
    @staticmethod
    def signup(data):
        new_user = User(username=data['username'], email=data['email'])
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()
        return {"id": new_user.id, "username": new_user.username}

    @staticmethod
    def login(data):
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            token = create_access_token(identity=user.id)
            return token
        return None
