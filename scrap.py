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


LinkList = liens()


for i in range (len(LinkList)):
    retrieve(LinkList[i])
    print("Retrieving for id : " + str(i))

print(LinkList)

#CSV

try:

    data = [['ID', 'Name', 'Localisation', 'Adress', 'Link']]
    print("Fields Data List")

    longeur = len(LinkList)
    print("Assining Longeur")

    for i in range (0, longeur):
        tmp = []
        tmp.append(str(i))
        tmp.extend(Clowns[i])
        tmp.append(linksList[i])
        
        data.append(tmp)

        print("Getting ID : " + str(i))
   
    with open('Scrap_results.csv', 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, delimiter='|')
        print("Creating File")
        my_writer.writerows(data)
        print("Writing File")

except:
    print("erreur")

finally:
#   my_writer.close()
    print("Doc fermé")
    print("DONE")
        


