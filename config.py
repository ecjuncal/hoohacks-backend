import os

class Config:
    # General Config
    TESTING = True
    DEBUG = True

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "localdb.db")

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
