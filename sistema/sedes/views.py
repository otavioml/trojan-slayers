import os
from flask import Blueprint, render_template, request, redirect, url_for
from sistema import app, db, allowed_image
from sistema.sedes.models import Sede
from werkzeug.utils import secure_filename

sedes = Blueprint('sedes', __name__, template_folder="templates")


@sedes.route('/')
def index():
    sedes = Sede.query.order_by(Sede.id.desc()).all()
    return render_template('sedes.html', sedes_front=sedes)


@sedes.route('/adicionar-sede/', methods=['GET', 'POST'])
def adicionar_sede():
    if request.method == 'POST':
        sede_name = request.form['sede-name']
        sede_phone = request.form['contact']
        sede_address = request.form['address']

        # PROCESSAMENTO DE IMAGEM
        image = request.files['myfile']
        picture = image.filename

        if not allowed_image(image.filename):
            print("That image is not allowed")
            return redirect('/sedes/adicionar-sede/')
        else:
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            new_sede = Sede(sede_name, sede_address, sede_phone, picture)
            db.session.add(new_sede)
            db.session.commit()
            return redirect('/sedes/')
        
    else:
        return render_template('adicionar-sede.html')


@sedes.route('/sede-especifica/<_id>', methods=['GET', 'POST'])
def sede_especifica(_id):
    sede = Sede.query.get_or_404(_id)

    return render_template('sede_esp.html', sede=sede)


@sedes.route('/excluir_sede/<_id>', methods=['GET', 'POST'])
def excluir_sede(_id):
    sede = Sede.query.get_or_404(_id)

    if request.method == 'POST':
        db.session.delete(sede)
        db.session.commit()

        return redirect(url_for('sedes.index'))
    return render_template('excluir_sede.html', sede=sede)
