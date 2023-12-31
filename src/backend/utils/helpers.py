from collections import defaultdict
import re
import requests
import json
from datetime import date

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
        average = round(average, 2)
        averages[key]=average
    return averages

def getData(url):
    print("parsing data...")
    lst=[]
    today = date.today()
    for page in range(1,21):
        r = requests.get(url.format(page=page),headers = {'User-Agent':'AppleWebKit/605.1.15'})
        print(r)
        data = json.loads(re.search(r'<script id="__NEXT_DATA__" type="application/json">(\{"props".*?)</script>', r.text).group(1))
        for item in data['props']['pageProps']['searchPageState']['cat1']['searchResults']['listResults']:
            price= item['price']
            street=item['addressStreet'] 
            zip=item['addressZipcode']
            sqrft=item['area']
            lst.append({'date': today.isoformat(), 'address': street, 'price': price, 'zip': zip, 'SQRFT': sqrft})
    print("parasing complete")
    return lst

