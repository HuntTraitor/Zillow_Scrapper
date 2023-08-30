from db import addData, addZipData
from graph import updateGraph, updateZipGraphs
from parse_data import getData

def main():
    url='https://www.zillow.com/seattle-wa/{page}_p/'
    data = getData(url)
    addData(data)
    addZipData(data)
    updateGraph()
    updateZipGraphs()

if __name__ == '__main__':
    main()

