import requests
from bs4 import BeautifulSoup
import json
import time
from selenium import webdriver

class ZillowScrapper():
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

    def fetch(self, url, params):
        proxy = {'http': '129.226.33.104:3218'}
        response = requests.get(url, headers=self.headers, params=params, proxies=proxy)
        return response
    
    def parse(self, response):
        content = BeautifulSoup(response.content, 'html.parser')
        deck = content.find('ul', {'class': 'List-c11n-8-84-3__sc-1smrmqp-0 StyledSearchListWrapper-srp__sc-1ieen0c-0 doa-doM fgiidE photo-cards photo-cards_extra-attribution'})
        print(deck.prettify())
        for card in deck.contents:
            script = card.find('script', {'type': 'application/ld+json'})
            if script:
                script_json = json.loads(script.text)
                print(script_json['name'])

    def run(self):
        url = "https://www.zillow.com/seattle-wa/"
        params = {
            'searchQueryState': '{"pagination":{},"mapBounds":{"north":47.795229510991625,"south":47.43047194771355,"east":-122.03992539453127,"west":-122.64966660546877},"mapZoom":11,"usersSearchTerm":"Seattle WA","regionSelection":[{"regionId":16037,"regionType":6}],"isMapVisible":false,"filterState":{"ah":{"value":true},"sort":{"value":"globalrelevanceex"}},"isListVisible":true}'
        }
        res = self.fetch(url, params)
        self.parse(res)

if __name__ == '__main__':
    scrapper = ZillowScrapper()
    scrapper.run()