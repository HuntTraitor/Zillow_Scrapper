import requests
import re
import json
import pandas as pd
import pprint

url='https://www.zillow.com/seattle-wa/{page}_p/'
lst=[]
for page in range(1,21):
    r = requests.get(url.format(page=page),headers = {'User-Agent':'Mozilla/5.0'})
    data = json.loads(re.search(r'<script id="__NEXT_DATA__" type="application/json">(\{"props".*?)</script>', r.text).group(1))

    for item in data['props']['pageProps']['searchPageState']['cat1']['searchResults']['listResults']:
        price= item['price'] 
        lst.append({'price': price})
print(pd.DataFrame(lst))
df = pd.DataFrame(lst).to_csv('out.csv', index=False)