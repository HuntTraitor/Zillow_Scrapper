import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv('.env')
username: str = os.getenv('DB_USERNAME')
password: str = os.getenv('DB_PASSWORD')
cluster = "mongodb+srv://{}:{}@cluster0.fpuuluq.mongodb.net/test?retryWrites=true&w=majority".format(username, password)
client = MongoClient(cluster)
db = client.Zillow

def addData(data):
    houses = db.houses
    print("updating database...")
    for house in data:
        houses.replace_one({"address": house.get("address")}, house, upsert=True)
    print("database successfully updated")


