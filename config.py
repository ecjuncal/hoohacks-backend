import os
from google.cloud import datastore
import logging

class Config:
    # General Config
    TESTING = True
    DEBUG = True

    client = datastore.Client()
    key = client.key('Database', 5634161670881280)
    logging.info(client.get(key))
    SQLALCHEMY_DATABASE_URI = client.get(key)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
