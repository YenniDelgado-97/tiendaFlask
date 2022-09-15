from crypt import methods
from curses import flash
from sqlite3 import Cursor
from urllib import request
from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from .models.ModeloCompra import ModeloCompra
from .models.ModeloUsuario import ModeloUsuario
from .models.ModeloComic import ModeloComic

from .models.entidades.Compra import Compra
from .models.entidades.Comic import Comic
from .models.entidades.Usuario import Usuario
from .consts import *

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModeloUsuario.obtener_por_id(db, id)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """
    print(request.method)
    print(request.form["usuario"])
    print(request.form["password"])
    """
    if request.method == 'POST':
        usuario = Usuario(
            None, request.form['usuario'], request.form['password'], None)
        usuario_logeado = ModeloUsuario.login(db, usuario)
        if usuario_logeado != None:
            login_user(usuario_logeado)
            flash(MENSAJE_BIENVENIDA, 'success')
            return redirect(url_for('index'))
        else:
            flash(LOGIN_CREDENCIALESINVALIDAS, 'warning')
            return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")


@app.route('/logout')
def logout():
    logout_user()
    flash(LOGOUT, 'success')
    return redirect(url_for('login'))


@app.route("/")
@login_required
def index():
    if current_user.is_authenticated:
        if current_user.tipousuario.id == 1:
            comics_vendidos = []
            data = {
                'titulo': 'Comics Vendidos',
                'comics_vendidos': comics_vendidos
            }
        else:
            compras = ModeloCompra.listar_compras_usuario(db,current_user)
            data = {
                'titulo': 'Mis compras',
                'compras': compras
            }
        return render_template("index.html", data=data)
    else:
        return redirect(url_for('login'))


@app.route('/comics')
@login_required
def listar_comics():
    try:
        comics = ModeloComic.listar_comics(db)
        data = {
            'titulo': 'Listado de comics',
            'comics': comics
        }
        return render_template('listado_comics.html', data=data)

    except Exception as ex:
        return render_template('errores/error.html', mensaje=format(ex))


@app.route('/comprarComic', methods=['POST'])
@login_required
def comprar_comic():
    data_request = request.get_json()
    data = {}
    try:
        comic = Comic(data_request['isbn'],None,None,None,None)
        compra= Compra(None,comic,current_user)
        data['exito'] = ModeloCompra.registrar_compra(db,compra)
    except Exception as ex:
        data['mensaje'] = format(ex)
        data['exito'] = False
    return jsonify(data)


def pagina_no_encontrada(error):
    return render_template("errores/404.html"), 404


def pagina_no_autorizada(error):
    return redirect(url_for('login'))


def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(401, pagina_no_autorizada)
    app.register_error_handler(404, pagina_no_encontrada)
    return app
