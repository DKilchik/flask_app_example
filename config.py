from environs import Env
import os

basedir = os.path.abspath(os.path.dirname(__file__))

env = Env()
env.read_env()


class Config(object):
    SECRET_KEY = env.str("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
