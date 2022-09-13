from crypt import methods
from sqlite3 import Cursor
from urllib import request
from flask import Flask,render_template,request,url_for,redirect
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

from .models.ModeloUsuario import ModeloUsuario

from .models.ModeloComic import ModeloComic

from .models.entidades.Usuario import Usuario

app = Flask(__name__)

csrf= CSRFProtect()
db= MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")





@app.route("/login",methods=['GET','POST'])
def login():
    """
    print(request.method)
    print(request.form["usuario"])
    print(request.form["password"])
    """
    if request.method == 'POST':
        #print(request.form["usuario"])
        #print(request.form["password"])
        
        #esta es la variable usuario
        usuario= Usuario(None,request.form['usuario'],request.form['password'],None)
        usuario_logeado = ModeloUsuario.login(db,usuario)
        if usuario_logeado != None:
            return redirect(url_for('index'))
        else:
            return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")

@app.route('/comics')
def listar_comics():
    try:
        comics=ModeloComic.listar_comics(db)
        data= {
            'comics': comics
        } 
        return render_template('listado_comics.html', data=data)
    
    except Exception as ex:
        print(ex)

def pagina_no_encontrada(error):
    return render_template("errores/404.html"),404


def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404,pagina_no_encontrada)
    return app 
