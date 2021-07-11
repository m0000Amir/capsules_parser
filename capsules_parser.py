""" 
Vertuo Capsuless parser from https://www.nespresso.com/

m0000a    
"""
import json


import requests
from bs4 import BeautifulSoup as BS

if __name__ == "__main__":

    r = requests.get("https://www.nespresso.com/ru/en/coffee-capsules/vertuo")
    html = BS(r.content, "html.parser")

    products = html.select("div.product.name.product-item-name")

    im = html.select("div.product.photo.product-item-photo") 


    name_list = [item.text for item in products]
    image_list = [item.contents[1].attrs['src'] for item in im]


    dictionary = [{'name': capsule[0], 'img': capsule[1]} 
                for capsule in zip(name_list, image_list)]

    with open("capsules.json", "w") as outfile: 
        json.dump(dictionary, outfile, ensure_ascii=False)