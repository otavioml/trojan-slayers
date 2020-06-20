import os
from flask import Blueprint, render_template, request, redirect, url_for
from sistema import app, db, allowed_image
from sistema.livros.models import Livro
from werkzeug.utils import secure_filename

livros = Blueprint('livros', __name__, template_folder="templates")


@livros.route('/')
def index():
    livros = Livro.query.order_by(Livro.id.desc()).all()
    return render_template('livros.html', livros=livros)


@livros.route('/livro-esp/<_id>')
def livro_esp(_id):
    livro = Livro.query.get_or_404(_id)
    return render_template('livro_esp.html', livro=livro)


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
        if request.form.get('available')== 'on':
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
        if ',' not in price:
            price = price + ',00'

        # Limpando espaço duplo
        price = price.replace("  ", " ")

        image = request.files['myfile']
        picture = image.filename

        if not allowed_image(image.filename):
            print("That image is not allowed")
            return redirect('/livros/adicionar-livro/')
        elif image:
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
            livro = Livro(titulo, genero, autor, price, date, available, filename)
            db.session.add(livro)
            db.session.commit()
            return redirect('/livros/')
        else:
            livro = Livro(titulo, genero, autor, price, date, available, filename)
            db.session.add(livro)
            db.session.commit()
            return redirect('/livros/')

        return redirect(url_for('livros.index'))

    return render_template('adicionar-livro.html')


@livros.route('/editar_livro/<_id>', methods=['GET', 'POST'])
def editar_livro(_id):

    livro = Livro.query.get_or_404(_id)

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        gender = request.form['gender']
        date = request.form['date']
        price = request.form['price']
        # É necessário converter as checkboxes em booleans, porque elas retornam strings.
        available = False
        if request.form.get('available') == 'on':
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
        if ',' not in price:
            price = price + ',00'

        # Limpando espaço duplo
        price = price.replace("  ", " ")

        image = request.files['myfile']

        if not allowed_image(image.filename) and image:
            print("That image is not allowed")
            return redirect(url_for('livros.editar_livro', _id=livro.id))
        elif image:
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

            livro.title = title
            livro.author = author
            livro.gender = gender
            livro.pub_date = date
            livro.price = price
            livro.available = available
            livro.cover = filename

            db.session.commit()

            return redirect(url_for('livros.livro_esp', _id=livro.id))
        else:
            livro.title = title
            livro.author = author
            livro.gender = gender
            livro.pub_date = date
            livro.price = price
            livro.available = available

            db.session.commit()
            return redirect(url_for('livros.livro_esp', _id=livro.id))

    return render_template('editar_livro.html', livro=livro)


@livros.route('/excluir_livro/<_id>', methods=['GET', 'POST'])
def excluir_livro(_id):
    livro = Livro.query.get_or_404(_id)

    if request.method == 'POST':
        db.session.delete(livro)
        db.session.commit()

        return redirect(url_for('livros.index'))
    return render_template('excluir_livro.html', livro=livro)
