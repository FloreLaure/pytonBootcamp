# Partie 1
# 1
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '   '
DATABASE = 'resto'



class MenuItem:
    
    def __init__(self, id, nom, prix):
        self.id = id
        self.nom = nom
        self.prix = prix

    def exec_query(self,query):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        cursor.execute(query)
        resultat = cursor.fetchall()
        connection.close()
        return resultat

    # 2    
    def save(self):
        query = f"INSERT INTO Menu (Nom, Prix) VALUES ('{self.nom}', {self.prix})"
        return self.exec_query(query)


    def delete_from_db(self):
        query=f"DELETE FROM Menu where Nom ='{self.nom}'"
        return self.exec_query(query)
        
    def update_db(self,ancien):
        query=f"UPDATE Menu SET Nom = '{self.nom}' WHERE Nom = '{ancien}'"
        self.exec_query(query)
        query =f"UPDATE Menu SET Prix = {self.prix} WHERE Nom = '{self.nom}'" 
        self.exec_query(query)




    # 3
    def all_(self):
        query=f'SELECT Nom,Prix FROM Menu'
        resultat = self.exec_query(query)
        print(list(resultat))
        return resultat



    # 4 
    def get_by_name(self,name):
        query=f'select Nom from Menu where Nom ="{name}" '
        resultat= self.exec_query(query)
        if len(resultat) < 1:
            print('Pas de correspondant')
        else:    
            print(list(resultat))