import re,random,string
from flask import Flask
from flask import Flask,render_template,request,redirect,url_for,abort
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from modelo.models import Empleados,Habitaciones,Estacionamiento,Clientes
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
import os

app = Flask(__name__)
app.secret_key = "s3cr3t"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:password@database-1.cwgfqihazsc6.us-west-2.rds.amazonaws.com/Hotel'
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

#Empieza Empleados---------------------------------------------------------------------------------------------------

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

@app.route('/ModEmpleado')
def GetAllEmpleado():
    Empleado=Empleados()
    datos=Empleado.consultaGeneral()
    return render_template('Empleados/GetAllEmpleado.html',datos=datos)
   
@app.route('/DelEmpleado/<int:id>')
def DelEmpleado(id):
    Empleado=Empleados()
    Empleado.id_empleado=id
    Empleado.consultaIndividual()
    Empleado.estatus_usuario="Inactivo"
    Empleado.actualizar()
    return redirect(url_for('GetAllEmpleado'))

@app.route('/enviarEmpleaadoAUpdate/<int:id>')
def enviarEmpleaadoAUpdate(id):
    Empleado=Empleados()
    Empleado.id_empleado=id
    datos=Empleado.consultaIndividual()
    return render_template('Empleados/UpdateEmpleado.html',datos=datos)


@app.route('/actualizarEmpleadoBD', methods=['POST'])
def actualizarEmpleadoBD():

    empleado=Empleados() 
    empleado.id_empleado=request.form['inputId']
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
    empleado.actualizar()
    return redirect(url_for('GetAllEmpleado'))


#Empieza Habitaciones---------------------------------------------------------------------------------------------

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
    hab.id_habitacion=id
    hab.consultaIndividual()
    hab.estatus="Inactivo"
    hab.actualizar()
    return redirect(url_for('GetAllHabitacion'))
   


@app.route('/enviarHabitacionAUpdate/<int:id>')
def enviarHabitacionAUpdate(id):
    hab=Habitaciones()
    hab.id_habitacion=id
    datos=hab.consultaIndividual()
    return render_template('Habitaciones/UpdateHabitaciones.html',datos=datos)
   


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

@app.route('/actualizarHabitacionDB', methods=['POST'])
def actualizarHabitacionDB():
    habitacion=Habitaciones()
    habitacion.id_habitacion=request.form['idhabi']
    habitacion.piso=request.form['inputPiso']
    habitacion.numerohabitacion=request.form['inputHabi']
    habitacion.tipohabitacion=request.form['inputTipo']
    print(habitacion)
    habitacion.actualizar()
    return redirect(url_for('GetAllHabitacion'))

#Empieza Estacionamiento------------------------------------------------------------------------------------------------

@app.route('/AddEstacionamiento')
def ventanaRegistroEstacionamiento():
   return render_template('Estacionamiento/AddEstacionamiento.html')
   
@app.route('/ModEstacionamiento')
def GetAllEstacionamiento():
    estacionamiento=Estacionamiento()
    datos=estacionamiento.consultaGeneral()
    return render_template('Estacionamiento/GetAllEstacionamiento.html',datos=datos)

@app.route('/deleteEstacionamiento/<int:id>')
def deleteEstacionamiento(id):
    estacionamiento=Estacionamiento()
    estacionamiento.id_estacionamiento=id
    estacionamiento.consultaIndividual()
    estacionamiento.estatus="Inactivo"
    estacionamiento.actualizar()
    return redirect(url_for('GetAllEstacionamiento'))
    
@app.route('/enviarEstacionamientoAUpdate/<int:id>')
def enviarEstacionamientoAUpdate(id):
    estacionamiento=Estacionamiento()
    estacionamiento.id_estacionamiento=id
    datos=estacionamiento.consultaIndividual()
    return render_template('Estacionamiento/UpdateEstacionamiento.html',datos=datos)
   


@app.route('/agregarEstacionamientoDB', methods=['POST'])
def agregarEstacionamientoDB():
    estacionamiento=Estacionamiento()
    estacionamiento.piso=request.form['inputPiso']
    estacionamiento.numerolugar=request.form['inputLugar']
    estacionamiento.disponibilidad='Desocupado'
    estacionamiento.estatus="Activo"
    estacionamiento.insertar()
    return redirect(url_for('GetAllEstacionamiento'))

@app.route('/actualizarEstacionamientoDB', methods=['POST'])
def actualizarEstacionamientoDB():
    estacionamiento=Estacionamiento()
    estacionamiento.id_estacionamiento=request.form['idEsta']
    estacionamiento.piso=request.form['inputPiso']
    estacionamiento.numerolugar=request.form['inputLugar']
    print(estacionamiento)
    estacionamiento.actualizar()
    return redirect(url_for('GetAllEstacionamiento'))


#Empieza Clientes-------------------------------------------------------------------------------------------------

@app.route('/AddCliente')
def ventanaAddCliente():
    return render_template('Clientes/AddCliente.html')


@app.route('/ModCliente')
def ventanaModificarCliente():
    cliente=Clientes()
    datos=cliente.consultaGeneral()
    return render_template('Clientes/GetAllClientes.html',datos=datos)
   

@app.route('/enviarClienteAUpdate/<int:id>')
def enviarClienteAUpdate(id):
    cliente=Clientes()
    cliente.id_clientes=id
    datos=cliente.consultaIndividual()
    return render_template('Clientes/UpdateClientes.html',datos=datos)




@app.route('/deleteCliente/<int:id>')
def deleteCliente(id):

    cliente=Clientes()
    cliente.id_clientes=id
    cliente.consultaIndividual()
    cliente.estatus_cliente="InActivo"
    cliente.actualizar()
    return redirect(url_for('ventanaModificarCliente'))
   
@app.route('/enviarClienteDB', methods=['POST'])
def enviarClienteDB():
    cliente=Clientes()
    cliente.nombre=request.form['inputNombre']
    cliente.apellido_paterno=request.form['inputApellidoPaterno']
    cliente.apellido_materno=request.form['inputApellidoMaterno']
    cliente.fecha_registro=request.form['inputFechaRegistro']
    cliente.telefono=request.form['inputTelefono']
    cliente.correo=request.form['inputcorreo']
    cliente.direccion=request.form['inputDireccion']
    cliente.estatus_cliente="Activo"
    cliente.insertar()
    return redirect(url_for('ventanaAddCliente'))
    
@app.route('/actualizarClienteDB', methods=['POST'])
def actualizarClienteDB():
    cliente=Clientes()
    cliente.id_clientes=request.form['inputId']
    cliente.nombre=request.form['inputNombre']
    cliente.apellido_paterno=request.form['inputApellidoPaterno']
    cliente.apellido_materno=request.form['inputApellidoMaterno']
    cliente.fecha_registro=request.form['inputFechaRegistro']
    cliente.telefono=request.form['inputTelefono']
    cliente.correo=request.form['inputcorreo']
    cliente.direccion=request.form['inputDireccion']
    cliente.estatus_cliente="Activo"
    cliente.actualizar()
    return redirect(url_for('ventanaModificarCliente'))









   



if __name__ == '__main__':
    app.run(debug = True)
