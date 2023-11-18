
def nom_pres(titre):
    L = []
    titre = titre[:len(titre)-4]
    titre = titre[11:]
    if ord(titre[len(titre)-1]) <= 57:
        titre = titre[:-1]
    return titre

def prenom_pres(nom):
    prenom = ""
    if nom == "Chirac":
        prenom = "Jacques"
    if nom == "Giscard d'Estaing":
        prenom = "Valérie"
    if nom == "Hollande":
        prenom = "François"
    if nom == "Macron":
        prenom = "Emmanuel"
    if nom == "Mitterand":
        prenom = "François"
    if nom == "Sarkozy":
        prenom = "Nicolas"
    return prenom

# mettre en minuscule les textes

def convertir_en_minuscules(nom_fichier_entree, nom_fichier_sortie):
    with open(nom_fichier_entree, 'r', encoding='utf-8' ) as fichier_entree:
        contenu = fichier_entree.read()

    contenu_minuscule = contenu.lower()

    with open(nom_fichier_sortie, 'w', encoding='utf-8') as fichier_sortie:
        fichier_sortie.write(contenu_minuscule)





