import os
from dotenv import load_dotenv

class Config:
    # General Config
    TESTING = True
    DEBUG = True

    load_dotenv()
    SQLALCHEMY_DATABASE_URI = os.environ.get('LOCAL_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
