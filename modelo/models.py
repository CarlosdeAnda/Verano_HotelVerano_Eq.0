from flask_sqlalchemy import SQLAlchemy                                                                                                                                                          
from sqlalchemy import Column,Integer,String,ForeignKey,Date,DateTime,BLOB,Float,Time
from sqlalchemy.orm import relationship                                                                                                                                                          
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db=SQLAlchemy()          

#Modelo Empleados-----------------------------------------------------------------------------------------
                                                                                                                                                                                                 
class Empleados(db.Model):
    __tablename__='Empleados'
    id_empleado=Column(Integer,primary_key=True)
    nombre=Column(String,nullable=False)
    apellido_paterno=Column(String,nullable=False)
    apellido_materno=Column(String,nullable=False)
    genero=Column(String,nullable=False) 
    fecha_nacimiento=Column(Date,nullable=False)
    fecha_registro=Column(Date,nullable=False)
    telefono=Column(String,nullable=False)
    usuario=Column(String,nullable=False)
    passwd=Column(String,nullable=False)
    tipo =Column(String,nullable=False)
    estatus_usuario=Column(String,nullable=False)
    clave=Column(String,nullable=False)
    foto=Column(String,nullable=False)
    
    def insertar(self):                                                                                                                                                                          
        db.session.add(self)                                                                                                                                                                     
        db.session.commit()                                                                                                                                                                      
    def consultaGeneral(self):                                                                                                                                                                   
        usuario=self.query.all()                                                                                                                                                                   
        return usuario
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        usuario=self.consultaIndividual()
        db.session.delete(usuario)
        db.session.commit()
    def consultaIndividual(self):
        usuario=self.query.get(self.id_empleado)
        return usuario

    @property
    def password(self):
        raise AttributeError('El atributo password no es de lectura')
    
    def validarPassword(self,passs):
        pwd = Empleados.query.filter_by(passwd=passs).first()
        return pwd

    def is_active(self):
        if self.estatus_usuario=='Activo':
            return True
        else:
            return False
    
    def is_authenticated(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return self.id_empleado
    
    def getTipo(self):
        return "Tipo"
    
    def validar(self,us,ps):
        emp=Empleados.query.filter_by(usuario=us).first()
        if(emp!=None):
            if(emp.validarPassword(ps)):
                return emp
            else:
                return None


#Modelos Habitaciones---------------------------------------------------------------------------------------------

class Habitaciones(db.Model):
    __tablename__='Habitaciones'
    id_habitacion=Column(Integer,primary_key=True)
    piso=Column(Integer,nullable=False)
    numerohabitacion=Column(String,nullable=False)
    disponibilidad=Column(String,nullable=False)
    tipohabitacion=Column(String,nullable=False)
    estatus=Column(String,nullable=False)
    


    def insertar(self):                                                                                                                                                                          
        db.session.add(self)                                                                                                                                                                     
        db.session.commit()                                                                                                                                                                      
    def consultaGeneral(self):                                                                                                                                                                   
        habitacion=self.query.all()                                                                                                                                                                   
        return habitacion
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        habitacion=self.consultaIndividual()
        db.session.delete(habitacion)
        db.session.commit()
    def consultaIndividual(self):
        habitacion=self.query.get(self.id_habitacion)
        return habitacion


#Modelo Estacionamiento-------------------------------------------------------------------------------------------

class Estacionamiento(db.Model):


     __tablename__='Estacionamiento'
     id_estacionamiento=Column(Integer,primary_key=True)
     piso=Column(String,nullable=False)
     numerolugar=Column(String,nullable=False)
     disponibilidad=Column(String,nullable=False)
     estatus=Column(String,nullable=False)
    


     def insertar(self):                                                                                                                                                                          
        db.session.add(self)                                                                                                                                                                     
        db.session.commit()                                                                                                                                                                      
     def consultaGeneral(self):                                                                                                                                                                   
        estacionamiento=self.query.all()                                                                                                                                                                   
        return estacionamiento
     def actualizar(self):
        db.session.merge(self)
        db.session.commit()
     def eliminar(self):
        estacionamiento=self.consultaIndividual()
        db.session.delete(estacionamiento)
        db.session.commit()
     def consultaIndividual(self):
        estacionamiento=self.query.get(self.id_estacionamiento)
        return estacionamiento
    
#Modelo Clientes-----------------------------------------------------------------------------------------------------

class Clientes(db.Model):
    __tablename__='Clientes'
    id_clientes=Column(Integer,primary_key=True)
    nombre=Column(String,nullable=False)
    apellido_paterno=Column(String,nullable=False)
    apellido_materno=Column(String,nullable=False)
    fecha_registro=Column(Date,nullable=False)
    telefono=Column(String,nullable=False)
    correo=Column(String,nullable=False)
    direccion=Column(String,nullable=False)
    estatus_cliente=Column(String,nullable=False)
    
    def insertar(self):                                                                                                                                                                          
        db.session.add(self)                                                                                                                                                                     
        db.session.commit()                                                                                                                                                                      
    def consultaGeneral(self):                                                                                                                                                                   
        cliente=self.query.all()                                                                                                                                                                   
        return cliente
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        cliente=self.consultaIndividual()
        db.session.delete(cliente)
        db.session.commit()
    def consultaIndividual(self):
        cliente=self.query.get(self.id_clientes)
        return cliente
    
#Modelo Reservaciones-----------------------------------------------------------------------------------------------------
class Reservacion(db.Model):
    __tablename__='Reservacion'
    id_reservacion=Column(Integer,primary_key=True)
    id_clientes=Column(Integer,primary_key=True)
    nombre=Column(String,nullable=False)
    apellido_paterno=Column(String,nullable=False)
    apellido_materno=Column(String,nullable=False)
    fecha_registro=Column(Date,nullable=False)
    telefono=Column(String,nullable=False)
    correo=Column(String,nullable=False)
    direccion=Column(String,nullable=False)
    estatus_cliente=Column(String,nullable=False)
    
    def insertar(self):                                                                                                                                                                          
        db.session.add(self)                                                                                                                                                                     
        db.session.commit()                                                                                                                                                                      
    def consultaGeneral(self):                                                                                                                                                                   
        reservacion=self.query.all()                                                                                                                                                                   
        return reservacion
    def actualizar(self):
        db.session.merge(self)
        db.session.commit()
    def eliminar(self):
        reservacion=self.consultaIndividual()
        db.session.delete(reservacion)
        db.session.commit()
    def consultaIndividual(self):
        reservacion=self.query.get(self.id_reservacion)
        return reservacion