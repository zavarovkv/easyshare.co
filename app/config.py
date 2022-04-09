import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Config(object):
    DEBUG = True

    mysql_username = os.environ.get('MYSQL_USERNAME')
    mysql_password = os.environ.get('MYSQL_PASSWORD')
    mysql_dbname = os.environ.get('MYSQL_DBNAME')
    mysql_host = os.environ.get('MYSQL_HOST')
    mysql_port = os.environ.get('MYSQL_PORT')

    SQLALCHEMY_DATABASE_URI = f'mysql://{mysql_username}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_dbname}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    HASHIDS_SALT = os.environ.get('HASHIDS_SALT')

    LANGUAGES = ['en', 'ru', 'eu']

    # Yandex Metrika counter
    YA_METRIC_COUNTER = os.environ.get('YA_METRIC_COUNTER')
