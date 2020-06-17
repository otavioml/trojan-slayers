from flask import Blueprint, render_template


home = Blueprint('home', __name__)

@home.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@home.route('/contato/')
def contato():
    return render_template('contato.html')


@home.route('/sobre/')
def sobre():
    return render_template('sobre.html')
