
import requests
from pymongo import MongoClient
import couchdb

   

URL = 'http://admin:burbuja02@localhost:5984'

try:
response = requests.get(URL)
if response.status_code == 200:
  print('Coneccion CouchDB: Acceso')
  if response.status_code == 401:
    print('Coneccion CouchDB: fallo', response.json())
    except requests.ConnectionError as e:
      raise e
    server=couchdb.Server(URL)
    HEADERS = {'Accept': 'application/json','Content-Type': 'application/json'}
    db = server['covid']
  
   

CLIENT = MongoClient('mongodb://localhost:27017')
  try:
    CLIENT.admin.command('ismaster')
    print('Coneccion MongoDB: Acceso')
      
  except ConnectionFailure as cf:
    print('Coneccion MongoDB: fallo', cf)

    
DBS = CLIENT.get_database('covid')
db1 = DBS.covid

for id in db:
  if(db1.find_one({'_id' : db[id].id})):
    print('Ya existe el documento')
else:
  db1.insert_one(db[id])
 

   
 
  

   
