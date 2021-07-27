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
    piso varchar(10) not null,
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

CREATE TABLE IF NOT EXISTS Reservacion(
	id_reservacion int not null auto_increment,
    id_clientes int not null,
    id_empleado int not null,
    id_habitacion int not null,
    id_estacionamiento int,
    fecha_ingreso date not null,
	fecha_salida date, 
    fecha_reservacion date not null,
    lugar_estacionamiento varchar(25) not null,
    estatus varchar(25) not null,
    primary key(id_reservacion),
    foreign key(id_clientes) references Clientes(id_clientes),
    foreign key(id_empleado) references Empleados(id_empleado),
    foreign key(id_habitacion) references Habitaciones(id_habitacion),
    foreign key(id_estacionamiento) references Estacionamiento(id_estacionamiento)
);


select * from Empleados;

insert into Empleados values(1,"Elon","Musk","River","Masculino","1998-01-13","2021-07-23","351-280-0928","admin","admin","Administrador","Activo","MOGU130198","elon.jpg");
insert into Empleados values(2,"Carlos","Esparza","De Anda","Masculino","1999-11-08","2021-07-23","351-215-0483","Carlos","123","Administrador","Activo","MOGU130198","elon.jpg");
insert into Empleados values(3,"Luz","Gallardo","Gutierrez","Femenino","1996-08-14","2021-07-23","351-112-5514","Luz","123","General","Activo","MOGU130198","elon.jpg");

insert into Habitaciones values(1,1,"A","Desocupado","Chica","Activo");
insert into Habitaciones values(2,2,"A","Desocupado","Mediana","Activo");
insert into Habitaciones values(3,2,"B","Desocupado","Grande","Activo");

insert into Estacionamiento values(1,"1","A","Desocupado","Activo");
insert into Estacionamiento values(2,"Extrerior","A","Desocupado","Activo");
insert into Estacionamiento values(3,"Exterior","B","Desocupado","Activo");

insert into Clientes values(1,"Pedro","Esparza","Navarrete","2021-07-23","351-280-0928","hola@123.com","Calle #1 blabla","Activo");
insert into Clientes values(2,"Ramiro","Esparza","Gutierrez","2021-06-22","351-280-0548","adios@123.com","Calle #2 bleble","Activo");
insert into Clientes values(3,"Clara","De Anda","Esparza","2021-08-10","351-890-0921","prueba@123.com","Calle #3 blubly","Activo");

CREATE USER IF NOT EXISTS 'admin'@'database-1.cwgfqihazsc6.us-west-2.rds.amazonaws.com/' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON Hotel.* TO 'admin'@'database-1.cwgfqihazsc6.us-west-2.rds.amazonaws.com';