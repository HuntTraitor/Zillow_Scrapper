import os
from dotenv import load_dotenv
from pymongo import MongoClient
from parse_data import getAveragePrice
from datetime import date
import time
import re

load_dotenv('.env')
username: str = os.getenv('DB_USERNAME')
password: str = os.getenv('DB_PASSWORD')
cluster = "mongodb+srv://{}:{}@cluster0.fpuuluq.mongodb.net/test?retryWrites=true&w=majority".format(username, password)
client = MongoClient(cluster)
db = client.Zillow

def addData(data):
    print("updating database...")
    houses = db.houses
    start_time = time.time()
    for house in data:
        houses.replace_one({"address": house.get("address")}, house, upsert=True)
    print("database successfully updated in ----%s seconds----" % (time.time() - start_time))

def addZipData(data):
    data = getAveragePrice(data)
    for key, value in data.items():
        collection_name = key
        print(collection_name)
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print(f"Collection '{collection_name}' created.")

        collection = db[collection_name]
        current_date = date.today().isoformat()
        existing_record = collection.find_one({"date": current_date})
        record = {"date":current_date, "averagePrice": value}

        if existing_record:
            collection.update_one({"date": current_date}, {"$set":{"averagePrice": value}})
            print(f"Record for date {current_date} updated")
        else:
            collection.insert_one(record)
            print(f"Record for date {current_date} inserted.")

def getHouses():
    collection = db.houses
    data = collection.find({})
    return data

def extractZip(zip):
    collection = db[zip]
    data = collection.find({})
    return data

def getZips():
    zipArr = []
    collection_names = db.list_collection_names()
    pattern = re.compile(r'^\d{5}$')
    for zip in collection_names:
        if pattern.match(zip):
            zipArr.append(zip)
    return zipArr