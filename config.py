import os
import gae_env
from gae_env import ValueNotSetError, NOT_SET_VALUE

class Config:
    # General Config
    TESTING = True
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = gae_env.get('Database id:5634161670881280')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
