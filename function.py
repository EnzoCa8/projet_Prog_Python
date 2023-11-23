
import string


import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
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

# mettre en minuscule les textes

def convertir_en_minuscules(input_dir, output_dir, file_names, file_names_cleaned):
    # Assurez-vous que le répertoire de sortie existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Parcourez chaque fichier d'entrée et de sortie
    for input_name, output_name in zip(file_names, file_names_cleaned):
        input_path = os.path.join(input_dir, input_name)
        output_path = os.path.join(output_dir, output_name)

        # Vérifiez si le fichier d'entrée existe
        if os.path.isfile(input_path):
            with open(input_path, 'r', encoding='utf-8') as input_file:
                # Lire le contenu du fichier et le convertir en minuscules
                content = input_file.read().lower()

                # Écrire le contenu dans le fichier de sortie
                with open(output_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(content)





def sup_pontuation(nom_fichier):

    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        texte = fichier.read()

    texte_sans_ponctuation = ''.join(caractere if caractere not in string.punctuation else ' ' for caractere in texte)

    texte_final = ' '.join(mot.replace('-', ' ').replace('\'', ' ') if '-' in mot or '\'' in mot else mot for mot in texte_sans_ponctuation.split())

    with open(nom_fichier, 'w', encoding='utf-8') as fichier:
        fichier.write(texte_final)

directory = './cleaned'

# Parcourir tous les fichiers dans le répertoire "cleaned"
for nom_fichier in os.listdir(directory):
    nom_fichier = sup_pontuation(nom_fichier)



## Début Matrice TF-IDF ##

    # TF
def dictionnaire(input_name, input_dir, file_names_cleaned, occurrence=None):

    # Parcourez chaque fichier
    for input_name in file_names_cleaned:
        input_path = os.path.join(input_dir)

        # Vérifiez si le fichier d'entrée existe
        if os.path.isfile(input_path):
            with open(input_path, 'r', encoding='utf-8') as dictionary:
                content = dictionary.read()

                mots = dictionary.split
                occurrence = {}
                for ligne in dictionary:
                    for mot in mots:
                        if mot in occurrence:
                            occurrence[mot] += 1
                        else :
                            occurrence[mot] = 1

                    occurrence_triees = dict(sorted(occurrence.items(), key=lambda x: x[1], reverse=True))

            for mot,occ in occurrence_triees.items():
                return f"Mot : {mot}, Occurrences : {occ}"


if __name__== '__main__':
    input_dir = "cleaned"

    dictionnaire(input_dir)

















