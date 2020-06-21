from flask import Blueprint, render_template
from sistema.livros.models import Livro
from sistema.sedes.models import Sede


principal = Blueprint('principal', __name__)

@principal.route('/', methods=['GET', 'POST'])
def index():
    sedes = Sede.query.order_by(Sede.id.desc()).all()
    livros = Livro.query.order_by(Livro.id.desc()).all()
    return render_template('index.html', livros=livros, sedes_front=sedes)

@principal.route('/contato/')
def contato():
    return render_template('contato.html')


@principal.route('/sobre/')
def sobre():
    return render_template('sobre.html')
