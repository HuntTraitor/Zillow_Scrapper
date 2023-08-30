from backend.db import addData, addZipData
from backend.graph import updateGraph, updateZipGraphs
from backend.utils.helpers import getData

def main():
    url='https://www.zillow.com/seattle-wa/{page}_p/'
    data = getData(url)
    addData(data)
    addZipData(data)
    updateGraph()
    updateZipGraphs()

if __name__ == '__main__':
    main()

