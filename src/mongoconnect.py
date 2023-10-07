from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def connect(uri):
    return MongoClient(uri, server_api=ServerApi("1"))


def close(client):
    client.close()
