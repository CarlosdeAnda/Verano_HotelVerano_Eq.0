import re
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


@app.route('/AddEmpleado')
def ventanaAddEmpleado():
    return render_template('Empleados/AddEmpleado.html')


@app.route('/AddHabitacion')
def ventanaRegistroHabitacion():
   return render_template('Habitaciones/AddHabitacion.html')


@app.route('/ModHabitacion')
def GetAllHabitacion():
    hab=Habitaciones()
    datos=hab.consultaGeneral()
    return render_template('Habitaciones/GetAllHabitaciones.html',datos=datos)

@app.route('/deleteHabitacion/<int:id>')
def deleteHabitacion(id):

    hab=Habitaciones()
    hab.estatus="Inactivo"
    hab.actualizar()
    return redirect(url_for('GetAllHabitacion'))
   


@app.route('/enviarHabitacionAUpdate')
def enviarHabitacionAUpdate():


    return render_template()
   


@app.route('/agregarHabitacionDB', methods=['POST'])
def agregarHabitacionDB():
    habitacion=Habitaciones()
    habitacion.piso=request.form['inputPiso']
    habitacion.numerohabitacion=request.form['inputHabi']
    habitacion.tipohabitacion=request.form['inputTipo']
    habitacion.disponibilidad='Desocupado'
    habitacion.estatus="Activo"
    habitacion.insertar()
    return redirect(url_for('GetAllHabitacion'))

if __name__ == '__main__':
    app.run(debug = True)