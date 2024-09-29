import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecret')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/palaceofgoods')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwtsecret')
    PI_NETWORK_KEY = os.getenv('PI_NETWORK_KEY', 'my-pi-key')




import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'SC6ZJYWDGKLQ44SPQFK2SXCH2U3OVIFRWVXFOPRAVT3WAYFPQH2VQ3Z4')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PI_NETWORK_URL = os.getenv('PI_NETWORK_URL', 'https://sandbox.minepi.com/app/palace-of-goods')

config = {
    'default': Config
}
