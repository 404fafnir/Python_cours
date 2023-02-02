import requests
from bs4 import BeautifulSoup as Soupe
import re

baseUrl = "https://404fafnir.dev"

response = requests.get(baseUrl)

if response.ok:

    soupeOcailloux = Soupe(response.text, 'html.parser')
    
    ul = soupeOcailloux.find('ul') #pour chercher des classes particulières -->     ,{"class": ""} 
    soc = ul.findAll('li')

    
    for li in soc:

        a = li.find('a')
        
        try:
            print(baseUrl + a['href'])
        except:
            pass
                
print(response)

