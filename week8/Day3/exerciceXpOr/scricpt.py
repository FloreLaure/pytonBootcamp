# import psycopg2
import requests
# HOSTNAME = 'localhost'
# USERNAME = 'postgres'
# PASSWORD = '   '
# DATABASE = 'gif'

def api_pays():
    # request =requests.get('https://restcountries.com/v3.1/region/africa')
    # request =requests.get('https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My')
    request=request.json()
    return request

data=api_pays()

print(data[0])

# connection=psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
# cursor=connection.cursor()
# for i in range (100):
#     gif=data[i]
#     query=f"INSERT INTO gifs()VALUES ('{country['name']}','{country['flag']}','{country['subregion']}',{country['population']})"
#     cursor.execute(query)
# connection.commit()
# connection.close()