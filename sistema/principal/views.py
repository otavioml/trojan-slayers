from flask import Blueprint, render_template, request
from sistema.livros.models import Livro
from sistema.sedes.models import Sede
from sistema.novidades.models import Novidade
from sistema.livros.views import Livro
from sistema.sedes.views import Sede
from sistema.novidades.views import Novidade


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


## ROTA DE TESTE
@principal.route('/pesquisateste/')
def pesquisateste():
    result_livros = Livro.query.order_by(Livro.id.desc()).all()
    result_sedes = Sede.query.order_by(Sede.id.desc()).all()
    result_novidades = Novidade.query.order_by(Novidade.pub_date.desc()).all()
    # ÚLTIMA SEDE PARA RETIRAR A LINHA
    ultima_sede = Sede.query.order_by(Sede.id.asc()).first()
    return render_template('resultados.html', ultima_sede = ultima_sede, livros = result_livros, sedes = result_sedes, novidades = result_novidades)

@principal.route('/resultados/', methods=['GET', 'POST'])
def pesquisa():

    pesquisa = request.form['pesquisa']

    livros_pesquisados = Livro.query.filter(Livro.title.contains(str(pesquisa).strip().title())).all() + Livro.query.filter(Livro.author.contains(str(pesquisa).strip().title())).all()
    sedes_pesquisadas = Sede.query.filter(Sede.name.contains(str(pesquisa).strip().title())).all() + Sede.query.filter(Sede.address.contains(str(pesquisa).strip().title())).all()
    novidades_pesquisadas = Novidade.query.filter(Novidade.title.contains(str(pesquisa).strip().title())).all() + Novidade.query.filter(Novidade.author.contains(str(pesquisa).strip().title())).all() + Novidade.query.filter(Novidade.content.contains(str(pesquisa).strip().title())).all()
    # ÚLTIMA SEDE PARA RETIRAR A LINHA
    if sedes_pesquisadas:
        ultima_sede = sedes_pesquisadas[len(sedes_pesquisadas)-1]
    else:
        ultima_sede = None

    return render_template('resultados.html', ultima_sede = ultima_sede, livros=livros_pesquisados, sedes=sedes_pesquisadas, novidades=novidades_pesquisadas)
