CREATE DATABASE IF NOT EXISTS Hotel;
USE Hotel;

CREATE TABLE IF NOT EXISTS Empleados(
  id_empleado INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  apellido_paterno VARCHAR(100) NOT NULL,
  apellido_materno VARCHAR(100) NOT NULL,
  genero VARCHAR(100) not null,
  fecha_nacimiento DATE NOT NULL,
  fecha_registro DATE NOT NULL,
  telefono VARCHAR(15) NOT NULL,
  usuario VARCHAR(45) NOT NULL,
  passwd VARCHAR(45) NOT NULL,
  tipo VARCHAR(35) NOT NULL,
  estatus_usuario VARCHAR(35) NOT NULL,
  clave varchar(100) not null,
  foto varchar(100) not null,
  PRIMARY KEY (id_empleado)
);

CREATE TABLE IF NOT EXISTS Clientes(
	id_clientes INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
	apellido_paterno VARCHAR(100) NOT NULL,
	apellido_materno VARCHAR(100) NOT NULL,
    fecha_registro DATE NOT NULL,
	telefono VARCHAR(15) NOT NULL,
    correo varchar(80) not null,
    direccion varchar(80) not null,
    estatus_cliente varchar(50) not null,
    primary key(id_clientes)
);


CREATE TABLE IF NOT EXISTS Estacionamiento(
	id_estacionamiento INT NOT NULL AUTO_INCREMENT,
    piso varchar(15) not null,
    numerolugar varchar(10) not null,
    disponibilidad varchar(50) not null,
    estatus varchar(25) not null,
    primary key (id_estacionamiento)
);


CREATE TABLE IF NOT EXISTS Habitaciones(
	id_habitacion INT NOT NULL AUTO_INCREMENT,
    piso int not null,
    numerohabitacion varchar(10) not null,
    disponibilidad varchar(50) not null,
    tipohabitacion varchar(75) not null,
    estatus varchar(25) not null,
    primary key (id_habitacion)
);


insert into Empleados values(1,"Elon","Musk","River","Masculino","1998-01-13","2021-07-23","3512800928","admin","admin","Administrador","Activo","MOGU130198","elon.jpg");
CREATE USER IF NOT EXISTS 'admin'@'database-1.cwgfqihazsc6.us-west-2.rds.amazonaws.com/' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON Hotel.* TO 'admin'@'database-1.cwgfqihazsc6.us-west-2.rds.amazonaws.com';