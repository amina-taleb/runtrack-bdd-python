import mysql.connector
# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",       # Adresse du serveur MySQL (localhost si en local)
    user="root", # Remplace par ton nom d'utilisateur MySQL
    password="root",     # Remplace par ton mot de passe MySQL
    database="LaPlateforme" # Nom de ta base de données
)
# Création d'un curseur pour exécuter des requêtes
curseur = conn.cursor()

# Exécuter la requête pour récupérer tous les étudiants
curseur.execute("SELECT * FROM etudiant;")

# Afficher les résultats
etudiants = curseur.fetchall()
for etudiant in etudiants:
    print(etudiant)

# Fermer le curseur et la connexion
curseur.close()
conn.close()