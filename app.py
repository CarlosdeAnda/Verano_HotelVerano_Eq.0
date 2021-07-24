from flask import Flask
from flask import Flask,render_template,request,redirect,url_for,abort
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from modelo.models import Usuarios
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
import os

app = Flask(__name__)
app.secret_key = "s3cr3t"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin@localhost/Hotel'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 100
app.config['UPLOAD_FOLDER'] = "static/uploads/"
loginManager=LoginManager()
loginManager.init_app(app)
loginManager.login_view="ventanaLogin"
db = SQLAlchemy(app)


@loginManager.user_loader
def load_user(id):
    return Usuarios.query.get(int(id))

@app.route('/login')
def ventanaLogin():
    return render_template('Login.html')

@app.route("/login",methods=['POST'])
def iniciarSesion():
    Us=Usuarios()
    Us=Us.validar(request.form['username'],request.form['pass'])
    if(Us!=None and Usuarios.is_active(Us)):
        login_user(Us)
        return render_template('template.html')
    else:
        return "El usuario o la contraseña es invalido"

@app.route("/CerrarSesion")
def cerrarSes():
    if(current_user.is_authenticated):
         logout_user()
         return redirect(url_for("ventanaLogin"))
    else:
        abort(404)


@app.route('/template')
def ventanaTemplate():
   return render_template('template.html')



if __name__ == '__main__':
    app.run(debug = True)