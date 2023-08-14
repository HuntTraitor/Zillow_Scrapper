import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
l=list()
obj={}
url = 'https://www.zillow.com/seattle-wa/'
driver=webdriver.Chrome()
driver.get(url)

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'zguid=24|%24eabf3acd-d3b1-4dc6-9cb5-f6e538e1e88c; zjs_anonymous_id=%22eabf3acd-d3b1-4dc6-9cb5-f6e538e1e88c%22; zjs_user_id=null; zg_anonymous_id=%221cd78b14-b328-4de4-b141-4ac7dc4d18bd%22; zgsession=1|0d051d06-9d13-4c6d-92d4-37f1a217bc80; x-amz-continuous-deployment-state=AYABeB+YcOPIDFYVCD6lHBLzEuMAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADFic4TnT5YJ0m+9aagAw+mHAcTSyECtDUGujGx20Wvc4VQemKemjqNHN85P2hJxL448K5D8+JhgpApG%2F1MrjAgAAAAAMAAQAAAAAAAAAAAAAAAAAAB8XyAQNqsRzV6x2P2IUBJz%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAw3%2FC0Ho8DX0lcYhOGlPOIyWy8cGGBZLYO+z0Mf; g_state={"i_p":1691959202977,"i_l":1}; search=6|1694545953587%7Cregion%3Dseattle-wa%26rb%3DSeattle-WA%26rect%3D47.734145%252C-122.224433%252C47.491912%252C-122.465159%26disp%3Dmap%26mdm%3Dauto%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D1%26rs%3D0%26ah%3D0%09%0916037%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09; JSESSIONID=61AEFCCCE15E5EDCF80A3F133006ECF6; AWSALB=BCUZ9FenDn8SinAphXMax0y/24x7PWYbSj+l0JPt1Hgfk+/oiiOBfvZmU7ch/rCnUOD4fjSgxxWYU1Iuoc+8AECqOsMq647gOu7BEfFwcuwrA47n6r11gYWe7jlo; AWSALBCORS=BCUZ9FenDn8SinAphXMax0y/24x7PWYbSj+l0JPt1Hgfk+/oiiOBfvZmU7ch/rCnUOD4fjSgxxWYU1Iuoc+8AECqOsMq647gOu7BEfFwcuwrA47n6r11gYWe7jlo',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

for page in range(1,5):
    resp = requests.get('https://www.zillow.com/seattle-wa/{}_p'.format(page), headers=headers).text
    soup = BeautifulSoup(resp, 'html.parser')
    properties = soup.find_all("li",{"class":"ListItem-c11n-8-84-3__sc-10e22w8-0 StyledListCardWrapper-srp__sc-wtsrtn-0 iCyebE gTOWtl"})

    print(len(properties))

    for x in range(0,len(properties)):
        try:
            obj["pricing"]=properties[x].find("div",{"class":"StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 fDSTNn"}).text
        except:
            obj["pricing"]=None
        try:
            obj["size"]=properties[x].find("div",{"class":"StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 dbDWjx"}).text
        except:
            obj["size"]=None
        try:
            obj["address"]=properties[x].find("a",{"class":"StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 jnnxAW property-card-link"}).text
        except:
            obj["address"]=None
        l.append(obj)
        obj={}
print(l)