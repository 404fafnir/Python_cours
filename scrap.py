import requests
from bs4 import BeautifulSoup as Soupe
import re



def liens ():
    for nb in range(6):

        baseUrl = ("https://lagrandefamilledesclowns.art/directory/index?page=" + str(nb) + "&profile_type=person")

        response = requests.get(baseUrl)

        linksList = []

        if response.ok:

            soupeOcailloux = Soupe(response.text, 'html.parser')
            
            ul = soupeOcailloux.find('div', {"id": "members_list"}) 
            soc = ul.findAll('div',{"class": "result"})

            for li in soc:

                a = li.find('a')
                
                try:
                    
                    linksList.extend(baseUrl + a['href'])
                
                except:
                    pass
    return linksList


nom = []
adresse = []
contacte = []


def retrieve (lien):

    lienR = requests.get(lien)
    
    if lienR.ok:    
        soupeOchoux = Soupe(lienR.text, 'html.parser')

        head = soupeOchoux.find('div', {"class": "head"})
        name = head.find('h1')
        nom.extend(name)

        content = soupeOchoux.find('div', {"class" : "content"})
        
        loc = content.find('div', {"class" : "icon-loc"})
        localisation = loc.find('p')
        adresse.extend(localisation)

        cont = content.find('div', {"class" : "icon-contact"})
        contact = cont.findAll('p')
        contacte.extend(contact)

    return nom, adresse, contacte


retrieve("https://webcache.googleusercontent.com/search?q=cache:https://lagrandefamilledesclowns.art/directory/874")

print(nom, adresse, contacte)






                

