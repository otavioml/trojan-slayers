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

    #resultados de livros pesquisados
    search_livros_title = Livro.query.filter(Livro.title.contains(str(pesquisa).strip().title())).all()
    search_livros_author = Livro.query.filter(Livro.author.contains(str(pesquisa).strip().title())).all()
    search_livros_gender = Livro.query.filter(Livro.gender.contains(str(pesquisa).strip().title())).all()

    titulo_l = set(search_livros_title)
    autor_l = set(search_livros_author)
    genero_l = set(search_livros_gender)

    interc_l1 = autor_l - genero_l
    apenas_autor = list(interc_l1) + search_livros_gender
    autor_e_genero_l = set(apenas_autor)
    interc_l2 = autor_e_genero_l - titulo_l

    livros_pesquisados =  list(interc_l2) + search_livros_title

    #resultados de sedes pesquisados
    search_sedes_nome = Sede.query.filter(Sede.name.contains(str(pesquisa).strip().title())).all()
    search_sede_endereco = Sede.query.filter(Sede.address.contains(str(pesquisa).strip().title())).all()
    nome_s = set(search_sedes_nome)
    endereco_s = set(search_sede_endereco)
    interc_s = endereco_s - nome_s
    sedes_pesquisadas =  list(interc_s) + search_sedes_nome

    #resultados de sedes pesquisados
    search_sedes_nome = Sede.query.filter(Sede.name.contains(str(pesquisa).strip().title())).all()
    search_sede_endereco = Sede.query.filter(Sede.address.contains(str(pesquisa).strip().title())).all()
    nome_s = set(search_sedes_nome)
    endereco_s = set(search_sede_endereco)
    interc_s = endereco_s - nome_s
    sedes_pesquisadas = list(interc_s) + search_sedes_nome

    #resultados de novidades pesquisadas
    search_novidades_titulo = Novidade.query.filter(Novidade.title.contains(str(pesquisa).strip().title())).all() 
    search_novidades_autor = Novidade.query.filter(Novidade.author.contains(str(pesquisa).strip().title())).all()
    search_novidades_texto = Novidade.query.filter(Novidade.content.contains(str(pesquisa).strip().title())).all()
    titulo_n = set(search_novidades_titulo)
    autor_n = set(search_novidades_autor)
    texto_n = set(search_novidades_texto)

    interc_n1 = texto_n - titulo_n
    title_no_repeat = list(interc_n1) + search_novidades_titulo
    titulo_e_texto_n = set(title_no_repeat)

    interc_n2 = titulo_e_texto_n - autor_n
    novidades_pesquisadas = list(interc_n2) + search_novidades_autor

    # ÚLTIMA SEDE PARA RETIRAR A LINHA
    if sedes_pesquisadas:
        ultima_sede = sedes_pesquisadas[len(sedes_pesquisadas)-1]
    else:
        ultima_sede = None

    return render_template('resultados.html', ultima_sede = ultima_sede, livros=livros_pesquisados, sedes=sedes_pesquisadas, novidades=novidades_pesquisadas)
