from flask import Blueprint, render_template


principal = Blueprint('principal', __name__)

@principal.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@principal.route('/contato/')
def contato():
    return render_template('contato.html')


@principal.route('/sobre/')
def sobre():
    return render_template('sobre.html')
