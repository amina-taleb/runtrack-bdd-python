CREATE DATABASE zoo;
USE zoo;
CREATE TABLE cage (id_cage INT PRIMARY KEY, superficie INT NOT NULL, capacite INT NOT NULL);
CREATE TABLE animal (id_animal INT PRIMARY KEY, nom VARCHAR(45) NOT NULL, race VARCHAR(45) NOT NULL, id_cage INT, FOREIGN KEY (id_cage) REFERENCES cage(id_cage));