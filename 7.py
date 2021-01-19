import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb

URL = 'http://admin:burbuja02@localhost:5984'

server=couchdb.Server(URL)
try:
	response = requests.get(URL)
	if response.status_code == 200:
		print('CouchDB connection: Success')
	if response.status_code == 401:
		print('CouchDB connection: failed', response.json())
except requests.ConnectionError as e:
	raise e
dbc = server['nintendo']

