import logging.config
import os

from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import redis

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('app')
load_dotenv()
app = Flask(__name__)

# redis config
redis_client = redis.Redis(host=os.environ['REDIS_HOST'], port=int(os.environ['REDIS_PORT']))

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + os.environ['MYSQL_USER'] + ":" + os.environ[
    'MYSQL_PASSWORD'] + "@" + os.environ['MYSQL_HOST'] + ":" + os.environ['MYSQL_PORT'] + "/" + os.environ[
                                            'MYSQL_DATABASE']
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "home_page"

from asset_app import routes
