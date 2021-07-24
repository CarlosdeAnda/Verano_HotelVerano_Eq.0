CREATE DATABASE IF NOT EXISTS Hotel;
USE Hotel;

CREATE TABLE IF NOT EXISTS Usuarios(
  id_usuario INT NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (id_usuario)
);

insert into Usuarios values(1,"Elon","Musk","River","Masculino","1998-01-13","2021-07-23","3512800928","admin","admin","Administrador","Activo");

CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON Hotel.* TO 'admin'@'localhost';