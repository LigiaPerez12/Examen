import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb

URL = 'http://admin:burbuja02@localhost:5984'
print(URL)

try:
    response = requests.get(URL)
    if response.status_code == 200:
        print('Coneccion CouchDB: acceso')
    if response.status_code == 401:
        print('Coneccion CouchDB: fallo', response.json())
except requests.ConnectionError as e:
    raise e

server=couchdb.Server(URL)
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

CLIENT = MongoClient('mongodb://localhost:27017')

try:
    CLIENT.admin.command('ismaster')
    print('Coneccion MongoDB: acceso')
except ConnectionFailure as cf:
    print('Coneccion MongoDB: fallo', cf)


DBS=['nintendo']


try:
    dbc=server.create('nueva')
except:
    dbc=server['nueva']
    

for db in DBS:
    if db not in ('admin', 'local','config'):  
        cols = CLIENT[db].list_collection_names()  
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in CLIENT[db][col].find():  
                try:
                    
                    documents=json.loads(json_util.dumps(x))

                    documents["_id"]=str(documents["_id"]["$oid"])


                    print(documents)
                    doc=dbc.save(documents)

                except TypeError as t:

                    print('current document raised error: {}'.format(t))
                    SKIPPED.append(x)  # creating list of skipped documents for later analysis
                    continue    # continue to next document
                except Exception as e:
                    raise e