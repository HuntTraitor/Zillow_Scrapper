from db import getHouses
import matplotlib.pyplot as plt
from collections import defaultdict
import re

def getAveragePrice(data):
    averages = {}
    zip = set()
    zipVprice = defaultdict(list)
    for item in data:
        zip.add(item['zip'])
        item['price'] = int(re.sub(r'[^0-9]','',item['price']))
        zipVprice[item['zip']].append(item['price'])

    for key, values in zipVprice.items():
        average = sum(values)/len(values)
        averages[key]=average
    return averages


def updateGraph():
    print("updating graph...")
    data = getHouses()
    average = getAveragePrice(data)
    x = list(average.keys())
    y = list(average.values())
    plt.figure(figsize=(20,6))
    plt.bar(x, y)
    plt.xlabel('zip')
    plt.ylabel('price')
    plt.title('Zip vs Price')
    plt.savefig('plots/plot.png')
    print("graph updated")
