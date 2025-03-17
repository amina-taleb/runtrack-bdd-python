CREATE DATABASE job07;
USE job07;
CREATE TABLE employe(id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255) NOT NULL, prenom VARCHAR(255) NOT NULL, salaire
DECIMAL NOT NULL, id_service INT NOT NULL);
DESCRIBE employe;
INSERT INTO employe(id, nom, prenom, salaire, id_service) VALUES(1, 'Taleb', 'Amina', 1500, 2), (2, 'Taleb1','Amina1', 3500, 2), (3, 'Taleb2','Amina2', 3200, 1);
SELECT * FROM employe WHERE salaire > 3000;
CREATE TABLE service(id INT AUTO_INCREMENT PRIMARY KEY, n
om VARCHAR(255) NOT NULL);
INSERT INTO service(id,nom) VALUES(1, 'informatique'), (2
, 'administratif');
SELECT * FROM employe WHERE id_service = 2;
SELECT id, nom, salaire, id_service FROM employe UNION SE
LECT id, nom, NULL FROM service;