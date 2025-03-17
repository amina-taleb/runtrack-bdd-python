# Import des modules nécessaires
import mysql.connector

# Connexion à la base de données
def connexion_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="gestion_zoo"
    )

# Création de la base de données et des tables
def creer_db():
    db = mysql.connector.connect(host="localhost", user="root", password="root")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS zoo;")
    cursor.execute("USE zoo;")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cage (
        id_cage INT PRIMARY KEY,
        superficie INT NOT NULL,
        capacite INT NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS animal (
        id_animal INT PRIMARY KEY,
        nom VARCHAR(45) NOT NULL,
        race VARCHAR(45) NOT NULL,
        id_cage INT,
        date_naissance DATE NOT NULL,
        pays_origine VARCHAR(45) NOT NULL,
        FOREIGN KEY (id_cage) REFERENCES cage(id_cage)
    );
    """)
    db.commit()
    cursor.close()
    db.close()

def ajouter_animal(id_animal, nom, race, id_cage, date_naissance, pays_origine):
    db = connexion_db()
    cursor = db.cursor()
    cursor.execute("""
    INSERT INTO animal (id_animal, nom, race, id_cage, date_naissance, pays_origine)
    VALUES (%s, %s, %s, %s, %s, %s)
    """, (id_animal, nom, race, id_cage, date_naissance, pays_origine))
    db.commit()
    cursor.close()
    db.close()

def supprimer_animal(id_animal):
    db = connexion_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM animal WHERE id_animal = %s", (id_animal,))
    db.commit()
    cursor.close()
    db.close()

def modifier_animal(id_animal, nom=None, race=None, id_cage=None, date_naissance=None, pays_origine=None):
    db = connexion_db()
    cursor = db.cursor()
    requete = "UPDATE animal SET "
    params = []

    if nom:
        requete += "nom = %s, "
        params.append(nom)
    if race:
        requete += "race = %s, "
        params.append(race)
    if id_cage:
        requete += "id_cage = %s, "
        params.append(id_cage)
    if date_naissance:
        requete += "date_naissance = %s, "
        params.append(date_naissance)
    if pays_origine:
        requete += "pays_origine = %s, "
        params.append(pays_origine)

    requete = requete.rstrip(", ") + " WHERE id_animal = %s"
    params.append(id_animal)

    cursor.execute(requete, tuple(params))
    db.commit()
    cursor.close()
    db.close()

def afficher_animaux():
    db = connexion_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM animal")
    for animal in cursor.fetchall():
        print(animal)
    cursor.close()
    db.close()

def superficie_totale():
    db = connexion_db()
    cursor = db.cursor()
    cursor.execute("SELECT SUM(superficie) FROM cage")
    superficie = cursor.fetchone()[0]
    print(f"Superficie totale des cages : {superficie} m²")
    cursor.close()
    db.close()

def menu():
    creer_db()
    while True:
        print("""
        1. Ajouter un animal
        2. Supprimer un animal
        3. Modifier un animal
        4. Afficher les animaux
        5. Calculer la superficie totale
        6. Quitter
        """)

        choix = input("Choisissez une option : ")

        if choix == '1':
            id_animal = int(input("ID de l'animal : "))
            nom = input("Nom : ")
            race = input("Race : ")
            id_cage = int(input("ID de la cage : "))
            date_naissance = input("Date de naissance (AAAA-MM-JJ) : ")
            pays_origine = input("Pays d'origine : ")
            ajouter_animal(id_animal, nom, race, id_cage, date_naissance, pays_origine)

        elif choix == '2':
            id_animal = int(input("ID de l'animal à supprimer : "))
            supprimer_animal(id_animal)

        elif choix == '3':
            id_animal = int(input("ID de l'animal à modifier : "))
            nom = input("Nouveau nom (laisser vide pour ne pas changer) : ") or None
            race = input("Nouvelle race (laisser vide pour ne pas changer) : ") or None
            id_cage = input("Nouvel ID de cage (laisser vide pour ne pas changer) : ")
            id_cage = int(id_cage) if id_cage else None
            date_naissance = input("Nouvelle date de naissance (AAAA-MM-JJ, laisser vide pour ne pas changer) : ") or None
            pays_origine = input("Nouveau pays d'origine (laisser vide pour ne pas changer) : ") or None
            modifier_animal(id_animal, nom, race, id_cage, date_naissance, pays_origine)

        elif choix == '4':
            afficher_animaux()

        elif choix == '5':
            superficie_totale()

        elif choix == '6':
            break

        else:
            print("Option invalide. Recommencez.")

if __name__ == "__main__":
    menu()
