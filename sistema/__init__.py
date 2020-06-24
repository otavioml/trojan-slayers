from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

############################################################
################## BANCO DE DADOS ##########################
############################################################


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['IMAGE_UPLOADS'] = os.path.join(os.path.dirname(__file__), 'static', 'images')
app.config['ALLOWED_IMAGE_EXTENSIONS'] = ['PNG', 'JPG', 'JPEG']

# PROCESSAMENTO DE IMAGENS


def allowed_image(filename):
    if "." not in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config['ALLOWED_IMAGE_EXTENSIONS']:
        return True
    else:
        return False


db = SQLAlchemy(app)
Migrate(app, db)

#############################################################
####################### BLUEPRINTS ##########################
#############################################################

from sistema.principal.views import principal
from sistema.livros.views import livros
from sistema.sedes.views import sedes
from sistema.novidades.views import novidades


app.register_blueprint(principal)
app.register_blueprint(livros, url_prefix="/livros")
app.register_blueprint(sedes, url_prefix="/sedes")
app.register_blueprint(novidades, url_prefix="/novidades")
