import requests
from bs4 import BeautifulSoup as Soupe
import re



def liens ():
    

    baseUrl = ("https://www.cybersecurite-solutions.com/annuaire-cybersecurite/")

    response = requests.get(baseUrl)
    
    linksList = []

    if response.ok:

        soupeOcailloux = Soupe(response.text, 'html.parser')
        
        ul = soupeOcailloux.find('tbody') 
        soc = ul.findAll('td', {"class": "link"})

        for li in soc:

            a = li.find('a')
                
            try:
                
                linksList.append(baseUrl + a['href'])
                
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






                

