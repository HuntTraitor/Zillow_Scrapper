from .db import getHouses, getZips, extractZip
from .utils.helpers import getAveragePrice
import matplotlib.pyplot as plt

def updateGraph():
    print("updating graph...")
    data = getHouses()
    average = getAveragePrice(data)
    x = list(average.keys())
    y = list(average.values())
    plt.figure(figsize=(20,6))
    plt.bar(x, y)
    plt.xlabel('zip')
    plt.ylabel('average price')
    plt.title('Zip vs Price')
    plt.savefig('static/plots/plot.png')
    plt.close()
    print("graph updated")

def updateZipGraphs():
    print("updating zipcode graphs")
    zipList = getZips()
    for zip in zipList:
        points = {}
        data = extractZip(zip)
        for item in data:
            points[item['date']] = item['averagePrice']
        x = list(points.keys())
        y = list(points.values())
        plt.figure(figsize=(20,6))
        plt.plot(x,y)
        plt.xlabel('date')
        plt.ylabel('average price')
        plt.title(f"{zip} average price over time")
        plt.savefig(f'static/plots/zips/{zip}.png')
        plt.close()
    print("zip graphs updated")
        
