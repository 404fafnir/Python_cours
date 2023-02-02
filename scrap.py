import requests
from bs4 import BeautifulSoup as Soupe
import re

baseUrl = "https://lagrandefamilledesclowns.art/directory/index?profile_type=person"

response = requests.get(baseUrl)

if response.ok:

    soupeOcailloux = Soupe(response.text, 'html.parser')
    
    ul = soupeOcailloux.find('div', {"id": "members_list"}) #pour chercher des classes particulières -->     ,{"class": ""} 
    soc = ul.findAll('div',{"class": "result"})

    
    for li in soc:

        a = li.find('a')
        
        try:
            print(baseUrl + a['href'])
        except:
            pass
                
print(response)

