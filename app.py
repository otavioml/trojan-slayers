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
    __tablename__ = 'livro'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    gender = db.Column(db.String)
    author = db.Column(db.String)
    price = db.Column(db.String)
    pub_date = db.Column(db.String)
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
    __tablename__ = 'sede'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    contact = db.Column(db.String)
    picture = db.Column(db.String)

    def __init__(self, name, address, contact, picture):
        self.name = name
        self.address = address
        self.contact = contact
        self.picture = picture

    def __repr__(self):
        return f'<Sede {self.name}>'


class Novidade(db.Model):
    __tablename__ = 'novidade'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    author = db.Column(db.String)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return f'<Novidade {self.title}>'


class Disponibilidade(db.Model):
    __tablename__ = 'disponibilidade'

    id = db.Column(db.Integer, primary_key=True)
    livroid = db.Column(db.Integer)
    sedeid = db.Column(db.Integer)

    def __init__(self, livroid, sedeid):
        self.livroid = livroid
        self.sedeid = sedeid


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/livros/')
def livros():
    livros = Livro.query.order_by(Livro.id.desc()).all()
    return render_template('livros.html', livros_front = livros)


@app.route('/livros/livro_esp/')
def livro_esp():
    return render_template('livro_esp.html')


@app.route('/livros/adicionar-livro/', methods=['GET', 'POST'])
def adicionar_livro():
    if request.method == 'POST':
        titulo = request.form['title']
        genero = request.form['gender']
        autor = request.form['author']
        date = request.form['date']
        price = request.form['price']
        # É necessário converter as checkboxes em booleans, porque elas retornam strings.
        available = False
        if request.form['available'] == 'on':
            available = True
        # Método para converter o "price" para o modelo "R$ XX,XX"
        price.strip()
        price = price.replace(".", ",")
        price = price.replace("r", "R")
        if price.startswith('R$') and not price.startswith('R$ '):
            price = price.replace('R$', 'R$ ')
        if price.startswith('R$') and ',' not in price:
            price = price + ',00'
        if not price.startswith('R$'):
            if price.startswith(' '):
                price = "R$" + price
            else:
                price = "R$ " + price
        if not price.startswith('R$') and ',' not in price:
            if price.startswith(' '):
                price = "R$" + price
            else:
                price = "R$ " + price
            price = price + ',00'
        
        # Limpando espaço duplo
        price = price.replace("  ", " ")

        livro = Livro(titulo, genero, autor, price, date, available)
        db.session.add(livro)
        db.session.commit()
        return redirect(url_for('livros'))

    return render_template('adicionar-livro.html')


@app.route('/sedes/')
def sedes():
    sedes = Sede.query.order_by(Sede.id.desc()).all()
    return render_template('sedes.html', sedes_front = sedes)


@app.route('/sedes/sede_esp/')
def sede_esp():
    return render_template('sede_esp.html')


@app.route('/sedes/adicionar-sede/', methods=['GET', 'POST'])
def adicionar_sede():
    if request.method == 'POST':
        sede_name = request.form['sede-name']
        sede_address = request.form['address']
        sede_phone = request.form['contact']
        new_sede = Sede(sede_name, sede_phone, sede_address, sede_name)

        db.session.add(new_sede)
        db.session.commit()
        return redirect('/sedes/adicionar-sede/')

    else:
        return render_template('adicionar-sede.html')


@app.route('/novidades/')
def novidades():
    novidades = Novidade.query.order_by(Novidade.id.desc()).all()
    return render_template('novidades.html', novidades_front = novidades)


@app.route('/novidades/adicionar-novidade/', methods=['GET', 'POST'])
def adicionar_novidades():
    if request.method == 'POST':
        titulo = request.form['title']
        mensagem = request.form['mensagem']
        nome = request.form['nome']

        novidade = Novidade(titulo, mensagem, nome)
        db.session.add(novidade)
        db.session.commit()
        return redirect(url_for('novidades'))

    return render_template('adicionar-novidade.html')


@app.route('/contato/')
def contato():
    return render_template('contato.html')


@app.route('/sobre/')
def sobre():
    return render_template('sobre.html')


if __name__ == "__main__":
    app.run(debug=True)
