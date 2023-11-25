import string
import os
import math
from collections import Counter
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

                # Écrire le contenu dans le fichier de sortie b
                with open(output_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(content)



# enlever ponctuation

def nettoyer_texte(texte):
    # Supprimer la ponctuation
    ponctuation = string.punctuation
    texte_nettoye = ''.join(caractere if caractere not in ponctuation else ' ' for caractere in texte)
    return texte_nettoye

#appliquer la fonction nettoyer_texte sur un fichier
def traiter_fichier(nom_fichier):
    chemin_fichier = os.path.join('cleaned', nom_fichier)

    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        texte = fichier.read()
        texte_nettoye = nettoyer_texte(texte)

    with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
        fichier.write(texte_nettoye)


#appliquer la fonction traiter_fichier sur un repertoire
def parcourir_repertoire():
    repertoire = 'cleaned'
    for nom_fichier in os.listdir(repertoire):
        if nom_fichier.endswith('.txt'):
            traiter_fichier(nom_fichier)





## Début Matrice TF-IDF ##

    # TF

def dico_TF(input_dir, file_names_cleaned):
    # Initialiser le dictionnaire des occurrences en dehors de la boucle
    occurrence = {}

    # Parcourir chaque fichier
    for input_name in file_names_cleaned:
        input_path = os.path.join(input_dir, input_name)

        # Vérifiez si le fichier d'entrée existe
        if os.path.isfile(input_path):
            with open(input_path, 'r', encoding='utf-8') as fichier:
                content = fichier.read()

                # Diviser le contenu en mots
                mots = content.split()

                # Parcourir chaque mot et mettre à jour le dictionnaire des occurrences
                for mot in mots:
                    # Mettre à jour le dictionnaire des occurrences
                    if input_name not in occurrence:
                        occurrence[input_name] = {}
                    occurrence[input_name][mot] = occurrence[input_name].get(mot, 0) + 1

    return occurrence


#IDF

def calculer_idf(repertoire_corpus):
    # Initialiser le dictionnaire pour stocker le nombre de documents contenant chaque mot
    documents_contenant_mot = {}

    # Nombre total de documents dans le corpus
    total_documents = 0

    # Parcourir chaque fichier dans le répertoire du corpus
    for nom_fichier in os.listdir(repertoire_corpus):
        chemin_fichier = os.path.join(repertoire_corpus, nom_fichier)

        # Vérifier si le chemin est un fichier
        if os.path.isfile(chemin_fichier):
            total_documents += 1

            # Lire le contenu du fichier
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()

                # Diviser le contenu en mots
                mots = contenu.split()

                # Identifier les mots uniques dans le fichier
                mots_uniques = set(mots)

                # Mettre à jour le dictionnaire des documents contenant chaque mot
                for mot in mots_uniques:
                    documents_contenant_mot[mot] = documents_contenant_mot.get(mot, 0) + 1

    # Calculer le score IDF pour chaque mot
    idf_scores = {}
    for mot, nb_documents_contenant in documents_contenant_mot.items():
        idf_scores[mot] = math.log(total_documents / (1 + nb_documents_contenant))

    return idf_scores


#matrice TF-IDF

def calculer_tf_idf_matrix(repertoire_corpus, file_names_cleaned):
    # Calculer le dictionnaire TF
    tf_dict = dico_TF(repertoire_corpus, file_names_cleaned)

    # Calculer le dictionnaire IDF
    idf_dict = calculer_idf(repertoire_corpus)

    # Initialiser la liste des mots uniques
    mots_uniques = list(set(tf_dict.keys()).union(idf_dict.keys()))

    # Initialiser la matrice TF-IDF avec des zéros
    matrice_tfidf = [[0.0] * len(file_names_cleaned) for _ in range(len(mots_uniques))]

    # Remplir la matrice TF-IDF en multipliant les valeurs correspondantes de TF et IDF
    for i, mot in enumerate(mots_uniques):
        for j, file_name in enumerate(file_names_cleaned):
            tf_value = tf_dict.get(file_name, {}).get(mot, 0)  # Correction ici
            idf_value = idf_dict.get(mot, 0)
            matrice_tfidf[i][j] = [mot, str(tf_value * idf_value)]  # Paires de mot et de valeur TF-IDF

    # Calculer la transposée de la matrice sans utiliser de fonction prédéfinie
    matrice_tfidf_transposee = transposee_matrice(matrice_tfidf)

    return matrice_tfidf_transposee, mots_uniques


def transposee_matrice(matrice):
    nb_lignes, nb_colonnes = len(matrice), len(matrice[0])
    matrice_transposee = []

    for j in range(nb_colonnes):
        nouvelle_ligne = []
        for i in range(nb_lignes):
            nouvelle_ligne.append(matrice[i][j])
        matrice_transposee.append(nouvelle_ligne)

    return matrice_transposee



def afficher_matrice(matrice):
    for ligne in matrice:
        print(ligne)


#fonctionnalité TFIDF

'''def mots_moins_importants(matrice_tfidf, mots_uniques):
    mots_non_importants = []

    # Vérifier si la matrice TF-IDF est vide
    if not matrice_tfidf or not matrice_tfidf[0]:
        print("La matrice TF-IDF est vide ou mal formée.")
        return mots_non_importants

    # Parcourir la liste des mots uniques
    for i, mot in enumerate(mots_uniques):
        # Vérifier si l'indice est dans la plage de la matrice TF-IDF
        if i < len(matrice_tfidf):
            # Vérifier si le TF-IDF est égal à 0 dans tous les fichiers
            if all(tfidf == 0 for tfidf in matrice_tfidf[i]):
                mots_non_importants.append(mot)
        else:
            print("L'indice", i, "dépasse la longueur de la matrice TF-IDF.")

    return mots_non_importants'''

def mots_moins_importants(matrice_tfidf, mots_uniques):
    mots_non_importants = []

    # Parcourir les indices de mots uniques
    for i in range(len(mots_uniques)):
        try:
            # Vérifier si le TD-IDF est nul dans tous les fichiers
            if all(tfidf == 0 for tfidf in matrice_tfidf[i]):
                mots_non_importants.append(mots_uniques[i])
                # Ajouter des impressions supplémentaires pour visualiser les valeurs de TD-IDF
                print(f"Mot non important : {mots_uniques[i]}")
                print(f"Valeurs de TD-IDF pour ce mot : {matrice_tfidf[i]}")
        except IndexError:
            print(f"Erreur d'indice pour l'indice {i}. Matrice TD-IDF : {len(matrice_tfidf)} x {len(matrice_tfidf[0])}")
            continue  # Continuer la boucle après avoir traité l'erreur

    # Ajouter des impressions supplémentaires
    print(f"Longueur des mots non importants : {len(mots_non_importants)}")
    print(f"Mots non importants : {mots_non_importants}")

    return mots_non_importants