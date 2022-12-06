import psycopg2
import requests
from random import randint
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '   '
DATABASE = 'postgres'

def country_api():
    request =requests.get('https://restcountries.com/v2/all')
    request=request.json()
    return request

data=country_api()


connection=psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor=connection.cursor()
for i in range (10):
    country=data[randint(1,200)]
    query=f"INSERT INTO pays(names,flag,subregion,population)VALUES ('{country['name']}','{country['flag']}','{country['subregion']}',{country['population']})"
    cursor.execute(query)
connection.commit()
connection.close()

