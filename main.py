import requests
from bs4 import BeautifulSoup
l=list()
obj={}
url = 'https://www.zillow.com/seattle-wa/'

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'zguid=24|%24eabf3acd-d3b1-4dc6-9cb5-f6e538e1e88c; zjs_anonymous_id=%22eabf3acd-d3b1-4dc6-9cb5-f6e538e1e88c%22; zjs_user_id=null; zg_anonymous_id=%221cd78b14-b328-4de4-b141-4ac7dc4d18bd%22; x-amz-continuous-deployment-state=AYABeB+YcOPIDFYVCD6lHBLzEuMAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADFic4TnT5YJ0m+9aagAw+mHAcTSyECtDUGujGx20Wvc4VQemKemjqNHN85P2hJxL448K5D8+JhgpApG%2F1MrjAgAAAAAMAAQAAAAAAAAAAAAAAAAAAB8XyAQNqsRzV6x2P2IUBJz%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAw3%2FC0Ho8DX0lcYhOGlPOIyWy8cGGBZLYO+z0Mf; g_state={"i_p":1691959202977,"i_l":1}; pxcts=e3578247-3a6b-11ee-98b5-4f424d507063; _pxvid=e3577784-3a6b-11ee-98b5-99375ccac1d6; _px3=4a6656adc2d2525143cbf5509d79d8f121209de1c0a04beee6d795d8b6a3f773:VHTr+Kj96FVpKqLe96B18+E+8mClkuP8LLT5zw1rZhoBGY6EFtxkRUXfiaICGw85Uuz2LEDQohQy3doKulplaA==:1000:4P3anCURILuDaG104blxP6x1rJZDYNpovlJ/JLPvHZlea5zqEJd8lBAQk+QmUDH8iLIrYvrFugTbT5p5Xh9ou1SmNgnJT60gGMt9tShyQrWS6f5ueA7uVniLdAHd9i5geg5yJAJZIFRcXiSg7JjN8TGQAfwIVGbW/5to6vpSvAxETKTPdCsfQkG31hLlsxRvrXrgkcl4M++3YdUdiYc6KA==; zgsession=1|292cf0db-43d5-4088-992d-5dbd2b41adff; JSESSIONID=754B6D753B7312138B8238ED0D52A706; AWSALB=qpTZYXubF4sIj2CBN2Ls6eTbE75aP1TA695vL+84Y+wp379XbFIb80xhPFCVr+IyEwUi2XXhKbLiPrSgnOAw3MdW7n+wynQzW3L65RrZC2AnUVMWQ2XvUr5KRtnW; AWSALBCORS=qpTZYXubF4sIj2CBN2Ls6eTbE75aP1TA695vL+84Y+wp379XbFIb80xhPFCVr+IyEwUi2XXhKbLiPrSgnOAw3MdW7n+wynQzW3L65RrZC2AnUVMWQ2XvUr5KRtnW; search=6|1694588086838%7Crect%3D47.79522951099163%252C-121.94310837792969%252C47.43047194771355%252C-122.74648362207031%26rid%3D16037%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0916037%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Afalse%7D%09%09%09%09%09',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

for page in range(1,5):
    resp = requests.get("https://www.zillow.com/seattle-wa/{}_p/".format(page), headers=headers).text
    soup = BeautifulSoup(resp, 'html.parser')
    properties = soup.find_all("li",{"class":"ListItem-c11n-8-84-3__sc-10e22w8-0 StyledListCardWrapper-srp__sc-wtsrtn-0 iCyebE gTOWtl"})

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