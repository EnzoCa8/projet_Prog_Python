import string
import os
import math

def list_of_files(directory, extension):
    files_names = []    #on crée la liste des noms des fichiers
    for filename in os.listdir(directory):
        if filename.endswith(extension):    #on vérifie si le nom du fichier comporte la bonne extension (.txt)
            files_names.append(filename)
    return files_names              #on retourne la liste


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

def convertir_en_minuscules(input_dir, output_dir, file_names, file_names_cleaned):
    #vérifier que le répertoire de sortie existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #parcourir chaque fichier d'entrée et de sortie
    for input_name, output_name in zip(file_names, file_names_cleaned):
        input_path = os.path.join(input_dir, input_name)
        output_path = os.path.join(output_dir, output_name)

        #vérifier si le fichier d'entrée existe
        if os.path.isfile(input_path):
            with open(input_path, 'r', encoding='utf-8') as input_file:
                # Lire le contenu du fichier et le convertir en minuscules
                content = input_file.read().lower()

                #mettre le contenu dans le fichier de sortie b
                with open(output_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(content)



# enlever ponctuation

def nettoyer_texte(texte):

    ponctuation = string.punctuation       #on utilise la bibliothèque string pour &voir toute la ponctuation
    texte_nettoye = ''.join(caractere if caractere not in ponctuation else ' ' for caractere in texte)
    return texte_nettoye    #retourner le texte sans la ponctuation

#appliquer la fonction nettoyer_texte sur un fichier
def traiter_fichier(nom_fichier):
    chemin_fichier = os.path.join('cleaned', nom_fichier)   #déclarer comment on accède au fichier

    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:    #ouvrir le fichier en mode lecture
        texte = fichier.read()
        texte_nettoye = nettoyer_texte(texte)       #appliquer la fonction nettoyer_texte

    with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
        fichier.write(texte_nettoye)


#appliquer la fonction traiter_fichier sur un repertoire
def parcourir_repertoire():
    repertoire = 'cleaned'
    for nom_fichier in os.listdir(repertoire):     #boucle pour parcourir tous les fichiers du répertoire cleaned
        if nom_fichier.endswith('.txt'):
            traiter_fichier(nom_fichier)    #appliquer la fonction


def mots_unique():
    mots_uniques = set()

    # Parcourir tous les fichiers dans le répertoire
    for fichier_nom in os.listdir('cleaned'):
        if fichier_nom.endswith(".txt"):  # Assurez-vous que le fichier est un fichier texte
            chemin_fichier = os.path.join("cleaned", fichier_nom)

            # Lire le contenu du fichier
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()

            # Supprimer la ponctuation et diviser le contenu en mots
            mots = contenu.translate(str.maketrans("", "", string.punctuation)).lower().split()

            # Ajouter les mots à l'ensemble pour garantir l'unicité
            mots_uniques.update(mots)

    # Convertir l'ensemble en liste et la retourner
    return list(mots_uniques)


if __name__ == '__main__':
    repertoire_cleaned = 'cleaned'
    mots_uniques = mots_unique()

    print("Liste de mots uniques dans le répertoire:")
    print(mots_uniques)