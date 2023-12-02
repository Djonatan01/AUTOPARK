import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

template_dir = os.path.abspath('./Templates')

app = Flask(__name__,
            template_folder=template_dir,
            static_url_path="/Public",
            static_folder='Public')

app.secret_key = os.environ.get('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app,db)

login_manager = LoginManager()
login_manager.login_view = 'router.login.login'
login_manager.login_message = 'Please log in to access this page!'
login_manager.init_app(app)
