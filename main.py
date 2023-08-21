import requests
import re
import json
import pandas as pd
from datetime import date
from db import addData

url='https://www.zillow.com/seattle-wa/{page}_p/'
lst=[]
today = date.today()

def getData(url):
    for page in range(1,21):
        r = requests.get(url.format(page=page),headers = {'User-Agent':'Mozilla/5.0'})
        data = json.loads(re.search(r'<script id="__NEXT_DATA__" type="application/json">(\{"props".*?)</script>', r.text).group(1))

        for item in data['props']['pageProps']['searchPageState']['cat1']['searchResults']['listResults']:
            price= item['price']
            street=item['addressStreet'] 
            zip=item['addressZipcode']
            sqrft=item['area']
            date=today
            lst.append({'date': date.isoformat(), 'address': street, 'price': price, 'zip': zip, 'SQRFT': sqrft})
    return lst

data = getData(url)
addData(data)

