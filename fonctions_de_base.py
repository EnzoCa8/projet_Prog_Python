import string
import os

'''Ici, nous avons réalisé les toutes premières fonctions du projet servant notamment à mettre les texte au bin format'''

def list_of_files(directory, extension): #fonction qui fait la liste des fihciers du corpus
                                         # (directory est le chemin à prendre, ici cleaned, et extenion correspond au .txt)
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):    #on vérifie si le nom du fichier comporte la bonne extension (.txt)
            files_names.append(filename)
    return files_names


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

#mettre en minuscule les textes
def convertir_en_minuscules(input_dir, output_dir, file_names, file_names_cleaned): #prend en paramètre un fichier d'entrée et un
                                                                # autre de sortie puis le nom (ou la liste) du/des fichiers traités
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for input_name, output_name in zip(file_names, file_names_cleaned): #parcourir chaque fichier d'entrée et de sortie
        input_path = os.path.join(input_dir, input_name)
        output_path = os.path.join(output_dir, output_name)

        if os.path.isfile(input_path):  #vérifier si le fichier d'entrée existe
            with open(input_path, 'r', encoding='utf-8') as input_file:
                content = input_file.read().lower()

                with open(output_path, 'w', encoding='utf-8') as output_file:   #mettre le contenu dans le fichier de sortie b
                    output_file.write(content)



# enlever ponctuation

def nettoyer_texte(texte):  #fonction qui prend en paramètre le texte d'un président et le renvoie sans ponctuation

    ponctuation = string.punctuation       #on utilise la bibliothèque string pour &voir toute la ponctuation
    texte_nettoye = ''.join(caractere if caractere not in ponctuation else ' ' for caractere in texte)
    return texte_nettoye    #retourner le texte sans la ponctuation

def traiter_fichier(nom_fichier):   #applique la fonction nettoyer_texte sur un fichier pris en paramètre
    chemin_fichier = os.path.join('cleaned', nom_fichier)   #déclarer comment on accède au fichier

    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:    #ouvrir le fichier en mode lecture
        texte = fichier.read()
        texte_nettoye = nettoyer_texte(texte)

    with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
        fichier.write(texte_nettoye)


def parcourir_repertoire(): #appliquer la fonction traiter_fichier sur un repertoire
    repertoire = 'cleaned'
    for nom_fichier in os.listdir(repertoire):     #boucle pour parcourir tous les fichiers du répertoire cleaned
        if nom_fichier.endswith('.txt'):
            traiter_fichier(nom_fichier)


def mots_unique():
    mots_uniques = set()

    for fichier_nom in os.listdir('cleaned'):       #parcourir tous les fichiers du répertoire
        if fichier_nom.endswith(".txt"):
            chemin_fichier = os.path.join("cleaned", fichier_nom)
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()

            mots = contenu.translate(str.maketrans("", "", string.punctuation)).lower().split()     #supprimer la ponctuation et diviser le contenu en mots
            mots_uniques.update(mots)
    return list(mots_uniques)