from flask import Blueprint, render_template, request, redirect
from sistema import db
from sistema.sedes.models import Sede

sedes = Blueprint('sedes', __name__, template_folder="templates")


@sedes.route('/')
def index():
    sedes = Sede.query.order_by(Sede.id.desc()).all()
    return render_template('sedes.html', sedes_front=sedes)


@sedes.route('/sede_esp/')
def sede_esp():
    return render_template('sede_esp.html')


@sedes.route('/adicionar-sede/', methods=['GET', 'POST'])
def adicionar_sede():
    if request.method == 'POST':
        sede_name = request.form['sede-name']
        sede_phone = request.form['address']
        sede_address = request.form['phone']
        new_sede = Sede(sede_name, sede_address, sede_phone, sede_name)

        db.session.add(new_sede)
        db.session.commit()
        return redirect('/sedes/adicionar-sede/')

    else:
        return render_template('adicionar-sede.html')
