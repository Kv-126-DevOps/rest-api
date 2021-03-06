import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()


def getEnvVariable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = f"Expected env variable {name} not set."
        raise Exception(message)


POSTGRES_HOST = getEnvVariable("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
POSTGRES_USER = getEnvVariable("POSTGRES_USER")
POSTGRES_PASS = getEnvVariable("POSTGRES_PASS")
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'postgres')

DB_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@' \
         f'{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'HelloWorld'
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
