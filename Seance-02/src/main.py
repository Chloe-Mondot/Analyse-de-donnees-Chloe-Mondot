#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def listedesterritoires(territoiretest, exportationUSD, importationUSD):
    listedesterritoires = [[territoiretest[0], 0]]
    pos = 0
    for element in range(0,len(territoiretest)):
        if territoiretest[element] != listedesterritoires[pos][0]:
            listedesterritoires.append([territoiretest[element], element])
            pos += 1
    lignes = []
    for element in range(1,len(listedesterritoires)):
        lignes.append(listedesterritoires[element][1] - 1)
    lignes.append(len(territoiretest))
    liste = []
    for element in range(0,len(listedesterritoires)):
        liste.append([listedesterritoires[element][0], listedesterritoires[element][1], lignes[element]])
    totalparterritoire = []
    for element in range(0,len(liste)):
        totalparterritoire.append([liste[element][0], exportationUSD[liste[element][1]:liste[element][2]].sum(), importationUSD[liste[element][1]:liste[element][2]].sum()])
    return totalparterritoire

def nettoyage(colonne):
    colonne2 = []
    for element in colonne:
        if element == 'Sans objet' or element =='-':
            colonne2.append(float(0))
        else:
            colonne2.append(float(element))
    return colonne2

def getliste(territoiretest):
    listedesterritoires = [[territoiretest[0], 0]]
    pos = 0
    for element in range(0,len(territoiretest)):
        if territoiretest[element] != listedesterritoires[pos][0]:
            listedesterritoires.append([territoiretest[element], element])
            pos += 1
    lignes = []
    for element in range(1,len(listedesterritoires)):
        lignes.append(listedesterritoires[element][1] - 1)
    lignes.append(len(territoiretest))
    liste = []
    for element in range(0,len(listedesterritoires)):
        liste.append([listedesterritoires[element][0], listedesterritoires[element][1], lignes[element]])
    return liste

# Question 4
print("Question 4")
# Source des données : https://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele_item.asp?id=37
with open("./data/Produits-alimentaires-2024.csv", "r", encoding="utf-8") as fichier:
    contenu = pd.read_csv(fichier)

# Question 5
print("Question 5")
print(contenu)

# Question 6
print("Question 6")
print("nb de lignes:", len(contenu))
print("nb de colonnes:", len(contenu.columns))

# Question 7
print("Question 7")
print("nom des colonnes:",contenu.head(0).columns)


# Question 8
print("Question 8")

# Contenu des colonnes
# "year" : année
# "origin_id" : territoire de référence
# "dest_id" : territoire partenaire
# "Dist_VO (km)" : distance intercentroïde entre les deux territoires
# "hs92_Section_id" : code Section du produit
# "hs92_HS02_id" : code 2-digit du produit
# "hs92_HS04_id" : code 4-digit du produit
# "hs92_HS06_id" : code 6-digit du produit
# "export_val" : valeur des exportations du territoire de référence vers le territoire partenaire en dollars courants
# "import_val" : valeur des importations du territoire partenaire vers le territoire de référence en dollars courants
# "export_ton" : valeur des exportations du territoire de référence vers le territoire partenaire en tonnes
# "import_ton" : valeur des importations du territoire partenaire vers le territoire de référence en tonnes

print(contenu.dtypes)

for colonne in contenu.columns:
    type_de_colonne = contenu[colonne].dtypes
    if type_de_colonne == 'float64':
        type_final = 'float'
    elif type_de_colonne == 'int64':
        type_final = 'int'
    else:
        type_final = 'str'
    print("Colonne:", colonne, "Type:", type_final)

# Question 9
print("Question 9")

exportations_tonnes = contenu["export_ton"]
importations_tonnes = contenu["import_ton"]
print("Exportations en tonnes:", exportations_tonnes)
print("Importations en tonnes:", importations_tonnes)

# Question 10
print("Question 10")

somme_exportations = 0

for element in exportations_tonnes:
    if element != "-":
        somme_exportations += float(element)

print("Somme des exportations en tonnes:", somme_exportations)

somme_importations = 0

for element in importations_tonnes:
    if element != "-":
        somme_importations += float(element)

print("Somme des importations en tonnes:", somme_importations)

# Question 11
print("Question 11")
# Appliquer la fonction listedesterritoires(...) sur vos colonnes ici

code_territoire = contenu["origin_id"]
exportationUSD = contenu["export_val"]
importationUSD = contenu["import_val"]

totalterritoire = listedesterritoires(
    code_territoire, 
    exportationUSD, 
    importationUSD
)

listedesterritoires = []
for element in totalterritoire:
    listedesterritoires.append(element[0])

for territoire in listedesterritoires:
    for element in totalterritoire:
        if element[0] == territoire:
            exportations = contenu[contenu["origin_id"] == territoire]["export_val"].sum()
            importations = contenu[contenu["origin_id"] == territoire]["import_val"].sum()
            
            plt.pie([exportations, importations], labels=["Exportations", "Importations"],)

            plt.title(territoire)
            plt.savefig("./img/" + territoire + ".png")
            plt.close()




# Questions 12 et 14
print("Questions 12 et 14")
# Application la fonction nettoyage(...) sur vos colonnes ici

# Appliquer la fonction :
# liste = getliste(...)

# Mettre le code nouveau DataFrame ici et appeler la liste donnees2

# Compléter la boucle à partir des différents éléments précédents. Le nom des listes est celle proposée dans les commentaires.
# parametres = []
# quartiles = []
# deciles = []
# for element in range(0,len(donnees2.columns)):
#     parametres2 = []
#     distanceinterquartile = []
#     distanceinterdecile = []
#     for element2 in range(0,len(liste)):
#         codeiso = liste[element2][0]
#         data2 = donnees2.iloc[liste[element2][1]:liste[element2][2],element]

#         moyenne = 
#         mediane = 
#         mode = 
#         ecarttype = 
#         ecartabsolumoyen = 
#         etendue = 
#         parametres2.append([codeiso, moyenne, mediane, mode, ecarttype, ecartabsolumoyen, etendue])

#         quartile = 
#         distanceinterquartile.append([codeiso, (quartile[0.75] - quartile[0.25]).round(decimals=2)])
#         decile = 
#         distanceinterdecile.append([codeiso, (decile[0.9] - decile[0.1]).round(decimals=2)])
#     parametres.append(parametres2)
#     quartiles.append(distanceinterquartile)
#     deciles.append(distanceinterdecile)

# Question 13
print("Question 13")

# Question 14
# print("Question 14")

# Question 15
print("Question 15")

# Question 16
print("Question 16")
# Source des données : BDCOM, https://www.apur.org/fr/open-data-cartes/open-data/base-donnees-commerces-parisiens
with open("./data/restaurants-paris-2023.csv", "r", encoding="utf-8") as fichier:
    contenu2 = pd.read_csv(fichier)

# Question bonus
print("Question bonus")
