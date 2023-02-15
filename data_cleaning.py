import csv

path = "/Scrap_results.csv"

#Les fonctions sont dans l'ordre dans lequel elles doivent être appelées à la suite pour un clean efficace


#Elimine tout le marquage HTML

#Pour toutes les lignes sauf première et dernière dernière
def del_croco (ligne):

    newligne = ""

    incroco = False

    for i in range (0, len(ligne)):

        if (ligne[i] != '<') and not(incroco):
            newligne += ligne[i]
            incroco = False

        elif ligne[i] == '>':
            incroco = False

        else:
            incroco = True

    return newligne

#Elimine les quotes 

#Que pour la 3ieme colonne je crois 0|1|2|3|4
def del_quote (ligne):

    newligne = ""

    for i in range (0, len(ligne)):
        if ligne[i] != '"':
            newligne += ligne[i]  
        else:
            pass 
    
    return newligne

#Elimine les 17 premiers cara et le dernier ce qui correspond a [[email protected] Num_Tel ]

#Que pour la 3ieme colone 0|1|2|3|4 

def del_bracket (ligne):
    
    newligne = ""

    for i in range (0, (len(ligne)-1)):
        if i < 18:
            pass
        else:
            newligne += ligne[i]
    
    return newligne


#supprime les virgules non prévues 

#Que pour 2ieme et 3ieme colonne 0|1|2|3|4
def del_unexpectedcomma (ligne):

    newligne = ""

    for i in range (0, len(ligne)):
        if ligne[i] == ",":
            pass
        else:
            newligne += ligne[i]
    
    return newligne


#Delimiter "|"

input_file = "Scrap_results.csv"
output_file = "Scrap_results_cleaned.csv"


with open(input_file, 'r') as csv_input_file, open(output_file, 'w', newline='') as csv_output_file:
    
    reader = csv.reader(csv_input_file, delimiter='|')
    writer = csv.writer(csv_output_file, delimiter='|')

    
    for row in reader:
        
        new_row = []
        
        new_row.append(row[0])

        new_row.append(del_croco(row[1]))

        new_row.append(del_croco(row[2]))

        new_row.append(del_bracket(del_quote(del_croco(row[3]))))

        new_row.append(row[4])

        writer.writerow(new_row)

