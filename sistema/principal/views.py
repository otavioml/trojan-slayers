from flask import Blueprint, render_template, request
from sistema.livros.models import Livro
from sistema.sedes.models import Sede
from sistema.livros.views import Livro
from sistema.sedes.views import Sede
from sistema.novidades.views import Novidade


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


@principal.route('/resultados/', methods=['GET', 'POST'])
def pesquisa():

    pesquisa = request.form['pesquisa']

    livros_pesquisados = Livro.query.filter(Livro.title.contains(str(pesquisa)))
    sedes_pesquisadas = Sede.query.filter(Sede.name.contains(str(pesquisa)))
    novidades_pesquisadas = Novidade.query.filter(Novidade.title.contains(str(pesquisa)))

    return render_template('resultados.html', livros=livros_pesquisados, sedes=sedes_pesquisadas, novidades=novidades_pesquisadas)
