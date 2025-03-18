CREATE DATABASE store;
USE store;
CREATE TABLE category(id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255));
CREATE TABLE product(id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), descript TEXT, price INT, quantity INT, id_category INT, FOREIGN KEY (id_category) REFERENCES category(id));
INSERT INTO category(id, nom) VALUES(1, 'Legumes'), (2, 'Fruits');
INSERT INTO product(id, nom, descript, price, quantity, id_category) VALUES(1, 'pomme', 'rouge et grande', 3, 100, 2), (2, 'climentine', 'petit et acide', 4, 100, 2), (3, 'tomate', 'rouge et petite', 2, 50, 1), (4, 'courgette', 'vert et longue', 4, 60, 1), (5, 'banane', 'jaune et mûr', 1, 45, 2);
SELECT * FROM product;
ALTER TABLE product MODIFY id INT AUTO_INCREMENT;
DESC product;
INSERT INTO product (nom, descript, price, quantity, id_category) 
VALUES ('pomme_de_terre', 'jaune et sableux', 2, 150, 1);