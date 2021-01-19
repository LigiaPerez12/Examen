from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId

client = MongoClient('mongodb://localhost:27017')
try:
	client.admin.command('ismaster')
	print('Coneccion MongoDB: acceso')
except ConnectionFailure as conFail:
	print('MongoDB connection: failed', conFail)
DBS = ['nintendo']

client2 = MongoClient('mongodb+srv://esfot:esfot@cluster0.gpdvt.mongodb.net/libros?retryWrites=true&w=majority')
try:
	client2.admin.command('ismaster')
	print('Coneccion MongoDB: acceso')
except ConnectionFailure as conFail:
	print('Coneccion MongoDB: fallo', conFil)
DBS = client2.get_database('nintendo')
db2 = DBS.drama

