import requests
from bs4 import BeautifulSoup as Soupe
import csv


linksList = []

def liens ():
    for nb in range(6):

        Url = ("https://lagrandefamilledesclowns.art/directory/index?page=" + str(nb) + "&profile_type=person")

        baseUrl = "https://lagrandefamilledesclowns.art"

        response = requests.get(Url)

        if response.ok:

            soupeOcailloux = Soupe(response.text, 'html.parser')
            
            ul = soupeOcailloux.find('div', {"id": "members_list"}) 
            soc = ul.findAll('div',{"class": "result"})

            for li in soc:

                a = li.find('a')
                
                try:
                    
                    linksList.append(baseUrl + a['href'])
                
                except:
                    pass

    return linksList


nom = ""
adresse = ""
contacte = ""

Clowns = []

def retrieve (lien):

    lienR = requests.get(lien)
    
    if lienR.ok:    
        soupeOchoux = Soupe(lienR.text, 'html.parser')

        head = soupeOchoux.find('div', {"class": "head"})
        
        try:    
            nom = str(head.find('h1'))
        except:
            nom = "ERROR_NONE"

        content = soupeOchoux.find('div', {"class" : "content"})

        try:
            loc = content.find('div', {"class" : "icon-loc"})
            adresse = str(loc.find('p'))
        except:
            adresse = "ERROR_NONE"

        try:    
            cont = content.find('div', {"class" : "icon-contact"})
            contacte = str(cont.findAll('p'))
        except:
            contacte = "ERROR_NONE"
        
    Clowns.append([nom, adresse, contacte])
    return Clowns     


listeLiens = liens()


for i in range (len(listeLiens)):
    retrieve(listeLiens[i])
    print("Retrieving for id : " + str(i))


#Partie CSV

try:

    data = [['ID', 'Name', 'Localisation', 'Adress', 'Link'],['0', 'Alexandre Quilian-Delaistre, alias SwoupGang', 'à Coachella ou Tommorowland', 'ERROR_NONE', 'Pas besoin de liens, il est au dessus de ça']]

    longeur = len(listeLiens)

    for i in range (0, longeur):
        tmp = []
        tmp.append(str((i+1)))
        tmp.extend(Clowns[i])
        tmp.append(linksList[i])
        
        data.append(tmp)

        print("Getting ID : " + str(i))
   
    with open('Scrap_results.csv', 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, delimiter='|')
        
        my_writer.writerows(data)
        

except:
    print("erreur")

finally:
    print("Doc fermé")
    print("DONE")
        


