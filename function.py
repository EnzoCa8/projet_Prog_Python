import os
def list_of_files(directory, extension):

    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def recup_nom_president(files_names):

    '''On supprime le .txt du nom du fichier'''
    nom_sans_extension = os.path.splitext(nom_fichier)[0]

    '''Diviser le nom du fichier en parties en utilisant '_' comme séparateur'''
    parties_nom = nom_sans_extension.split('_')

    '''Récupère le nom du président, qui est la deuxième partie du nom du fichier'''
    nom_president = parties_nom[1]

    return nom_president

def prenom_president():

    if recup_nom_president(nom_fichier) == "Chirac" :
        return "Jaques"
    elif recup_nom_president(nom_fichier) == "Giscard" :
        return "Valérie"
    elif recup_nom_president(nom_fichier) == "Hollande" :
        return "François"
    elif recup_nom_president(nom_fichier) == "Macron" :
        return "Emmanuel"
    elif recup_nom_president(nom_fichier) == "Mitterand" :
        return "François"
    elif recup_nom_president(nom_fichier) == "Sarkozy" :
        return"Nicolas"

