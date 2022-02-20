import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    print(SECRET_KEY)
    MAIL_SERVER = os.environ.get('MAIL_SERVER','localhost')
    print(MAIL_SERVER)
    MAIL_PORT = os.environ.get('MAIL_PORT','25')
    print(MAIL_PORT)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    print(MAIL_USERNAME)
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    print(MAIL_PASSWORD)