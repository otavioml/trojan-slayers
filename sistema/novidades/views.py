from flask import Blueprint, render_template, request, redirect, url_for
from sistema import db
from sistema.novidades.models import Novidade

novidades = Blueprint('novidades', __name__, template_folder="templates")


@novidades.route('/')
def index():
    novidades = Novidade.query.order_by(Novidade.id.desc()).all()
    return render_template('novidades.html', novidades_front=novidades)


@novidades.route('/adicionar-novidade/', methods=['GET', 'POST'])
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
