import os

class Config:
    # General Config
    TESTING = True
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.environ.get('URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
