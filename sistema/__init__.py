from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import os

app = Flask(__name__)

############################################################
################## BANCO DE DADOS ##########################
############################################################


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
