
import mysql.connector
from mysql.connector import errorcode #pour gérer les erreurs engendrés par sql

#connection à la base de données (mettre les info dans un dictionnaire): 
config = {
    'user' : 'root',
    'password' : 'root',
    'host' : 'localhost', #sur l'ordi local
    'database' : 'store',
    'raise_on_warnings' : True  #activer l'affichage des avertissement MySQL
}

#Créer une connection avec les informations fournies dans le dictionnaire config:
try :
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err :
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR :
        print('Invalid user or password !')
    elif err.errno == errorcode.ER_BAD_DB_ERROR :
        print("Database doesn't exist !")
    else :
        print('error')
    exit()  #ne pas continuer si jamais y a une erreur de connection

requete = 2    #déclarer une variable (pour choisir le requête SQL à exécuter)

#Récuperer des informations de la BDD :
if requete == 1 : 
    print("La liste des fruits")

    cursorSel = cnx.cursor() #un curseur est une structure de données qui contient des info qui permettent d'interroger une BDD, il contient également les informations récupérées de la BDD
     #cursorSel = cursor + SELECT (la requete select de sql)
    selectAction = ("SELECT * FROM product WHERE id_category = %s")  #créer une structure de tuple contenant ma requête, on peut déclarer cette ligne une seule fois puis personnaliser ma réponse dans selectValue
    selctValue = ("2",) # doit être un tuple (avec une virgule)

    cursorSel.execute(selectAction, selctValue)   #executer ma requête
    resultSelect = cursorSel.fetchall() #récuperer les informations avec la fonction fetchall et les stocker dans resultSelect

    for i in resultSelect : 
        print(i[1]) #afficher les lignes de la 2 eme colonne
    cursorSel.close()  #fermer le curseur pour ne pas garder en mémoir les données d'entrées et de sortie (libérer la mémoire)

#Inserer des informations dans ma BDD :
if requete == 2 : 

    data_product1 = {
        'id1' : 7, 
        'nom1' : 'salade',
        'descript1' : 'vert et neuf', 
        'price1' : 1, 
        'quantity1' : 15, 
        'id_category1' : 1
    }
    cursorInsert = cnx.cursor()

    add_product = ("INSERT INTO product"
                   "(id, nom, descript, price, quantity, id_category) "
                   "VALUES(%(id1)s, %(nom1)s, %(descript1)s, %(price1)s, %(quantity1)s, %(id_category1)s)"
                   )
    cursorInsert.execute(add_product, data_product1)
    print("Le nombre de produits insérés est ", cursorInsert.rowcount)  #donne combien de produits insérés

    cnx.commit()  #pour valider une requête (il faut toujour le mettre)

    #On peut mettre autant de requêtes qu'on veut
    cursorInsert.close()

cnx.close()  #fermer la base de données (si on ferme pas, la mémoire va saturer au bout d'un moment, si on ouvre plusieurs BDD et on ne les ferme pas)