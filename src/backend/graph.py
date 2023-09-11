from .db import getHouses, getZips, extractZip
from .utils.helpers import getAveragePrice
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patheffects import withStroke
from datetime import datetime

BLUE = "#076fa2"
RED = "#E3120B"
BLACK = "#202020"
GREY = "#a2a2a2"

def updateGraph():
    print("updating graph...")

    # Pulling data from the database
    data = getHouses()
    average = getAveragePrice(data)

    # Sorting data and storing that into a x and y axis array
    sorted_data = sorted(average.items(), key=lambda item: item[1])
    x = [item[1] for item in sorted_data]
    y = [item[0] for item in sorted_data]

    # Plotting the graph
    fig, ax = plt.subplots(figsize=(20,15))
    ax.barh(y, x, height=0.7, color=BLUE)
    ax.xaxis.tick_top()
    ax.set_xlim(0, max(x) * 1.1)
    ax.set_ylim(-0.5, len(y) - 0.5)

    # Setting vertical line positions for the x-axis
    line_positions=[500000, 1000000, 1500000, 2000000, 2500000, 3000000]
    for position in line_positions:
        ax.axvline(x=position, color='black', linestyle='-', linewidth=0.5)

    # Labeling different axis's
    plt.xlabel('average price in millions')
    plt.ylabel('zipcode')
    ax.xaxis.set_label_position('top')
    plt.title('Zipcode vs Price')
    plt.savefig('static/plots/plot.png', bbox_inches='tight')
    plt.close()
    print("graph updated")

def updateZipGraphs():
    print("updating zipcode graphs")
    zipList = getZips()

    # Extracting the data
    for zip in zipList:
        points = {}
        data = extractZip(zip)
        for item in data:
            date = datetime.strptime(item['date'], '%Y-%m-%d') # Converting to datetime object in python
            points[date] = item['averagePrice']
        if len(points) <= 1: # Skipping if there isn't enough data to create a proper graph
            print(f"Skipping graph for {zip}...")
            continue

        # Setting x and y values
        x = list(points.keys())
        y = list(points.values())
        fig, ax = plt.subplots(figsize=(20,6))
        ax.set_ylim(0,4000000)

        # Formatting the x-axis
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
        plt.xticks(rotation=45)

        # Plotting the graph and storing it into a folder
        ax.plot(x,y)
        ax.set_xlabel('date')
        ax.set_ylabel('average price in millions')
        ax.set_title(f"{zip} average price over time")
        plt.savefig(f'static/plots/zips/{zip}.png')
        plt.close()
    print("zip graphs updated")