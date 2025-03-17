import mysql.connector

class EmployeDB:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS employe (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(255),
            prenom VARCHAR(255),
            salaire DECIMAL(10, 2),
            id_service INT
        )
        ""
        )

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS service (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(255)
        )
        ""
        )
        self.conn.commit()

    def insert_employe(self, nom, prenom, salaire, id_service):
        self.cursor.execute("""
        INSERT INTO employe (nom, prenom, salaire, id_service)
        VALUES (%s, %s, %s, %s)
        """, (nom, prenom, salaire, id_service))
        self.conn.commit()

    def insert_service(self, nom):
        self.cursor.execute("""
        INSERT INTO service (nom)
        VALUES (%s)
        """, (nom,))
        self.conn.commit()

    def get_employes_salaire_sup_3000(self):
        self.cursor.execute("""
        SELECT * FROM employe
        WHERE salaire > 3000
        ""
        )
        for row in self.cursor.fetchall():
            print(row)

    def get_employes_with_service(self):
        self.cursor.execute("""
        SELECT e.id, e.nom, e.prenom, e.salaire, s.nom AS service
        FROM employe e
        JOIN service s ON e.id_service = s.id
        ""
        )
        for row in self.cursor.fetchall():
            print(row)

    def update_employe(self, employe_id, nom=None, prenom=None, salaire=None, id_service=None):
        query = "UPDATE employe SET "
        updates = []
        params = []

        if nom:
            updates.append("nom = %s")
            params.append(nom)
        if prenom:
            updates.append("prenom = %s")
            params.append(prenom)
        if salaire:
            updates.append("salaire = %s")
            params.append(salaire)
        if id_service:
            updates.append("id_service = %s")
            params.append(id_service)

        query += ", ".join(updates) + " WHERE id = %s"
        params.append(employe_id)

        self.cursor.execute(query, params)
        self.conn.commit()

    def delete_employe(self, employe_id):
        self.cursor.execute("DELETE FROM employe WHERE id = %s", (employe_id,))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

# Exemple d'utilisation
db = EmployeDB(host='localhost', user='root', password='votre_mot_de_passe', database='entreprise')
db.create_tables()

# Insertion des services
db.insert_service('Informatique')
db.insert_service('Ressources Humaines')

# Insertion des employés
db.insert_employe('Dupont', 'Jean', 3500, 1)
db.insert_employe('Martin', 'Sophie', 2800, 2)
db.insert_employe('Durand', 'Paul', 4200, 1)

# Récupérer les employés avec un salaire > 3000 €
db.get_employes_salaire_sup_3000()

# Récupérer les employés et leur service
db.get_employes_with_service()

# Mise à jour d'un employé
db.update_employe(1, salaire=3700)

# Suppression d'un employé
db.delete_employe(2)

db.close()