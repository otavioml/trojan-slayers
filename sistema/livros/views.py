from flask import Blueprint, render_template, request, redirect, url_for
from sistema import db
from sistema.livros.models import Livro

livros = Blueprint('livros', __name__, template_folder="templates")


@livros.route('/')
def index():
    livros = Livro.query.order_by(Livro.id.desc()).all()
    return render_template('livros.html', livros_front=livros)


@livros.route('/livro_esp/')
def livro_esp():
    return render_template('livro_esp.html')


@livros.route('/adicionar-livro/', methods=['GET', 'POST'])
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
