import re,random,string
from flask import Flask
from flask import Flask,render_template,request,redirect,url_for,abort
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from modelo.models import Empleados,Habitaciones
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
import os

app = Flask(__name__)
app.secret_key = "s3cr3t"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:password@databasechida.cwgfqihazsc6.us-west-2.rds.amazonaws.com/Hotel'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 100
app.config['UPLOAD_FOLDER'] = "static/uploads/"
loginManager=LoginManager()
loginManager.init_app(app)
loginManager.login_view="ventanaLogin"
db = SQLAlchemy(app)


@loginManager.user_loader
def load_user(id):
    return Empleados.query.get(int(id))

@app.route('/login')
def ventanaLogin():
    return render_template('Login.html')

@app.route("/login",methods=['POST'])
def iniciarSesion():
    Us=Empleados()
    Us=Us.validar(request.form['username'],request.form['pass'])
    if(Us!=None and Empleados.is_active(Us)):
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

#Empieza Empleados
@app.route('/AddEmpleado')
def ventanaAddEmpleado():
    return render_template('Empleados/AddEmpleado.html')

@app.route('/agregarEmpleadoBD', methods=['POST'])
def agregarEmpleadoBD():

    empleado=Empleados()
    empleado.nombre=request.form['inputNombre']
    empleado.apellido_paterno=request.form['inputApellidoPaterno']
    empleado.apellido_materno=request.form['inputApellidoMaterno']
    empleado.genero=request.form['inputGenero']
    empleado.fecha_nacimiento=request.form['inputFechaNacimiento']
    empleado.fecha_registro=request.form['inputFechaRegistro']
    empleado.telefono=request.form['inputTelefono']
    empleado.tipo=request.form['inputTipo']
    empleado.usuario=request.form['inputUsuario']
    empleado.passwd=request.form['inputPassword1']
    empleado.foto=request.form['inputFoto']
    empleado.estatus_usuario="Activo"
    Clave= empleado.apellido_paterno[:2]+empleado.apellido_materno[:1]+empleado.nombre[:1]+str(empleado.fecha_nacimiento.split("-")[0][2:])+str(empleado.fecha_nacimiento.split("-")[1])+empleado.fecha_nacimiento.split("-")[2]+random.choice(string.ascii_letters)+str(random.randrange(10))+random.choice(string.ascii_letters)
    empleado.clave=Clave
    empleado.insertar()
    return redirect(url_for('ventanaAddEmpleado'))





#Empieza Habitaciones
@app.route('/AddHabitacion')
def ventanaRegistroHabitacion():
   return render_template('Habitaciones/AddHabitacion.html')



@app.route('/agregarHabitacionDB', methods=['POST'])
def agregarHabitacionDB():

    habitacion=Habitaciones()
    habitacion.piso=request.form['inputPiso']
    habitacion.numerohabitacion=request.form['inputHabi']
    habitacion.tipohabitacion=request.form['inputTipo']
    habitacion.disponibilidad='Desocupado'
    habitacion.insertar()
    return redirect(url_for('ventanaRegistroHabitacion'))


if __name__ == '__main__':
    app.run(debug = True)