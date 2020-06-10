from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


# TABLES
class Livro(db.Model):
    __tablename__ = 'livros'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    gender = db.Column(db.String)
    author = db.Column(db.String)
    price = db.Column(db.String)
    pub_date = db.Column(db.Date)
    avaliable = db.Column(db.Boolean)

    def __init__(self, title, gender, author, price, pub_date, avaliable):
        self.title = title
        self.gender = gender
        self.author = author
        self.price = price
        self.pub_date = pub_date
        self.avaliable = avaliable

    def __repr__(self):
        return f'<Livro {self.title}>'


class Sede(db.Model):
    __tablename__ = 'sedes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    adrress = db.Column(db.String)
    contact = db.Column(db.String)
    picture = db.Column(db.String)

    def __init__(self, name, adrress, contact, picture):
        self.name = name
        self.adrress = adrress
        self.contact = contact
        self.picture = picture

    def __repr__(self):
        return f'<Sede {self.name}>'


class Novidades(db.Model):
    __tablename__ = 'novidades'
    content = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    pub_date = db.Column(db.String)

    def __init__(self, title, content, author, pub_date):
        self.title = title
        self.content = content
        self.author = author
        self.pub_date = pub_date

    def __repr__(self):
        return f'<Novidade {self.title}>'


class Disponibilidade(db.Model):
    __tablename__ = 'disponibilidade'

    id = db.Column(db.Integer, primary_key=True)
    livroid = db.Column(db.Integer, db.ForeignKey('livros.id'))
    sedeid = db.Column(db.Integer, db.ForeignKey('sedes.id'))

    title = db.relationship('livros', foreign_keys=livroid)
    alocation = db.relationship('sedes', foreign_keys=sedeid)

    def __init__(self, livroid, sedeid):
        self.livroid = livroid
        self.sedeid = sedeid


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/livros/')
def livros():
    return render_template('livros.html')


@app.route('/livros/livro_esp/')
def livro_esp():
    return render_template('livro_esp.html')


@app.route('/livros/adicionar-livro/')
def adicionar_livro():
    return render_template('adicionar-livro.html')


@app.route('/sedes/')
def sedes():
    return render_template('sedes.html')


@app.route('/sedes/sede_esp/')
def sede_esp():
    return render_template('sede_esp.html')


@app.route('/sedes/adicionar-sede/')
def adicionar_sede():
    return render_template('adicionar-sede.html')


@app.route('/novidades/')
def novidades():
    return render_template('novidades.html')


@app.route('/novidades/adicionar-novidades/')
def adicionar_novidades():
    return render_template('adicionar-novidades.html')


@app.route('/contato/')
def contato():
    return render_template('contato.html')


@app.route('/sobre/')
def sobre():
    return render_template('sobre.html')


if __name__ == "__main__":
    app.run(debug=True)
