from flask import Blueprint, render_template
from sistema.livros.models import Livro
from sistema.sedes.models import Sede
from sistema.novidades.models import Novidade


principal = Blueprint('principal', __name__)


@principal.route('/', methods=['GET', 'POST'])
def index():
    sedes = Sede.query.order_by(Sede.id.desc()).all()
    livros = Livro.query.order_by(Livro.id.desc()).all()
    ultima_sede = Sede.query.order_by(Sede.id.asc()).first()
    return render_template('index.html',  ultima_sede = ultima_sede, livros=livros, sedes_front=sedes)


@principal.route('/contato/')
def contato():
    return render_template('contato.html')


@principal.route('/sobre/')
def sobre():
    return render_template('sobre.html')

@principal.route('/pesquisa/')
def pesquisa():
    result_livros = Livro.query.order_by(Livro.id.desc()).all()
    result_sedes = Sede.query.order_by(Sede.id.desc()).all()
    result_novidades = Novidade.query.order_by(Novidade.pub_date.desc()).all()
    ultima_sede = Sede.query.order_by(Sede.id.asc()).first()
    return render_template('resultados.html', ultima_sede = ultima_sede, result_livros = result_livros, result_sedes = result_sedes, result_novidades = result_novidades)
