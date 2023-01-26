import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')


MAX_RANDOM_LENGTH = 6
MAX_CUSTOM_LENGTH = 16
REGULAR = '^[A-Za-z0-9]*$'
