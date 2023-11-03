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
#Nome da Chave do proprio TG
app.secret_key = 'tg1_fatecCruzeiro'
#Nome do banco TG autopark_
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_autopark.sqlite3"
#Não ficar realizando rastreamento no banco de dados
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app,db)

login_manager = LoginManager()
login_manager.login_view = 'router.login.login'
login_manager.login_message = 'Realize o login para acessar essa página!'
login_manager.init_app(app)