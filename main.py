import requests
import re
import json
import pandas as pd
from datetime import date
from db import addData
from graph import updateGraph

def main():
    url='https://www.zillow.com/seattle-wa/{page}_p/'

    data = getData(url)
    addData(data)
    updateGraph()

def getData(url):
    print("parsing data...")
    lst=[]
    today = date.today()
    for page in range(1,21):
        r = requests.get(url.format(page=page),headers = {'User-Agent':'Mozilla/5.0'})
        data = json.loads(re.search(r'<script id="__NEXT_DATA__" type="application/json">(\{"props".*?)</script>', r.text).group(1))
        for item in data['props']['pageProps']['searchPageState']['cat1']['searchResults']['listResults']:
            price= item['price']
            street=item['addressStreet'] 
            zip=item['addressZipcode']
            sqrft=item['area']
            lst.append({'date': today.isoformat(), 'address': street, 'price': price, 'zip': zip, 'SQRFT': sqrft})
    print("parasing complete")
    return lst

if __name__ == '__main__':
    main()

