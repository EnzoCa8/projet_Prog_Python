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
        nouvelle_colonne = []
        for i in range(nb_lignes):
            nouvelle_colonne.append(matrice[i][j])
        matrice_transposee.append(nouvelle_colonne)

    return matrice_transposee



def afficher_matrice(matrice):
    for ligne in matrice:
        print(ligne)


#fonctionnalité TFIDF

def mots_moins_importants(matrice_tfidf, mots_uniques):
    mots_non_importants = []

    # Parcourir les mots uniques
    for i, mot in enumerate(mots_uniques):
        try:
            # Récupérer l'indice du mot dans la matrice
            indice_mot = [j for j, valeur in enumerate(matrice_tfidf) if valeur[0] == mot]

            # Vérifier si le TD-IDF est nul dans tous les fichiers
            if all(matrice_tfidf[indice][1] == '0' for indice in indice_mot):
                mots_non_importants.append(mot)
        except IndexError:
            print(f"Erreur d'indice pour le mot {mot}. Matrice TD-IDF : {len(matrice_tfidf)} x {len(matrice_tfidf[0])}")
            continue  # Continuer la boucle après avoir traité l'erreur



    return mots_non_importants


def mots_plus_importants_tfidf(matrice_tfidf, mots_uniques):
    mots_importants_tfidf = []
    scores_max_tfidf = []

    # Parcourir les indices de mots uniques
    for i in range(len(mots_uniques)):
        try:
            # Obtenir les scores TF-IDF pour le mot courant
            tfidf_scores = [float(score[1]) for score in matrice_tfidf[i]]

            # Vérifier si la liste des scores n'est pas vide
            if tfidf_scores:
                # Trouver le score TF-IDF le plus élevé
                max_tfidf = max(tfidf_scores)

                # Vérifier si max_tfidf est un nombre positif
                if isinstance(max_tfidf, (int, float)) and max_tfidf > 0:
                    # Ajouter le mot et le score correspondant aux listes résultantes
                    index_max_tfidf = tfidf_scores.index(max_tfidf)
                    mot_max_tfidf = mots_uniques[i]
                    mots_importants_tfidf.append(mot_max_tfidf)
                    scores_max_tfidf.append(max_tfidf)

        except IndexError:
            print(f"Erreur d'indice pour l'indice {i}. Matrice TD-IDF : {len(matrice_tfidf)} x {len(matrice_tfidf[0])}")
            continue  # Continuer la boucle après avoir traité l'erreur

    # Ajouter des impressions supplémentaires
    print(f"Mots ayant le score TF-IDF le plus élevé : {mots_importants_tfidf}")
    print(f"Scores TF-IDF correspondants : {scores_max_tfidf}")

    return mots_importants_tfidf, scores_max_tfidf


#Fonction indiquant quel mot chirac répète le plus dans ses discours
def mots_plus_repetes_par_chirac(repertoire_corpus, file_names_cleaned):
    # Calculer le dictionnaire TF
    tf_dict = dico_TF(repertoire_corpus, file_names_cleaned)

    # Identifier les fichiers de Jacques Chirac
    fichiers_chirac = ["Nomination_Chirac1_cleaned.txt", "Nomination_Chirac2_cleaned.txt"]

    # Liste pour stocker les résultats pour chaque fichier
    mots_plus_repetes_par_fichier = []

    # Parcourir les fichiers de Chirac
    for fichier_chirac in fichiers_chirac:
        # Vérifier si le fichier de Jacques Chirac est présent dans le corpus
        if fichier_chirac in tf_dict:
            occurrences_chirac = tf_dict[fichier_chirac]

            # Trouver le(s) mot(s) le(s) plus répété(s)
            mots_plus_repetes = [mot for mot, occ in occurrences_chirac.items() if occ == max(occurrences_chirac.values())]

            # Ajouter les résultats à la liste
            mots_plus_repetes_par_fichier.append((fichier_chirac, mots_plus_repetes))
        else:
            print(f"Le fichier de Jacques Chirac ({fichier_chirac}) n'a pas été trouvé dans le corpus.")

    # Afficher les résultats
    for fichier, mots_plus_repetes in mots_plus_repetes_par_fichier:
        print(f"Le(s) mot(s) le(s) plus répété(s) par le président Chirac dans le fichier {fichier} : {mots_plus_repetes}")




#fonction indiquant quel président a le plus parlé de la nation

from collections import Counter
import re

def president_avec_plus_parle_de_nation(repertoire_corpus, file_names_cleaned):
    # Calculer le dictionnaire TF
    tf_dict = dico_TF(repertoire_corpus, file_names_cleaned)

    # Liste des présidents et de leurs fichiers correspondants
    presidents = {
        "Chirac": ["Nomination_Chirac1_cleaned.txt", "Nomination_Chirac2_cleaned.txt"],
        "Giscard d'Estaing": ["Nomination_Giscard dEstaing_cleaned.txt"],
        "Hollande": ["Nomination_Hollande_cleaned.txt"],
        "Macron": ["Nomination_Macron_cleaned.txt"],
        "Mitterrand": ["Nomination_Mitterrand1_cleaned.txt", "Nomination_Mitterrand2_cleaned.txt"],
        "Sarkozy": ["Nomination_Sarkozy_cleaned.txt"]
    }

    # Dictionnaire pour stocker le nombre d'occurrences du mot "nation" par président
    occurrences_par_president = {}

    # Parcourir les présidents et leurs fichiers
    for president, fichiers in presidents.items():
        total_occurrences = 0
        for fichier in fichiers:
            # Vérifier si le fichier est présent dans le corpus
            if fichier in tf_dict:
                # Ajouter le nombre d'occurrences du mot "nation" dans le fichier
                total_occurrences += tf_dict[fichier].get("nation", 0)

        # Stocker le total des occurrences pour le président
        occurrences_par_president[president] = total_occurrences

    # Trouver le président avec le plus d'occurrences du mot "nation"
    president_max_occurrences = max(occurrences_par_president, key=occurrences_par_president.get)
    nb_occurrences_max = occurrences_par_president[president_max_occurrences]

    # Afficher le résultat
    print(f"Le président qui a le plus parlé de la nation est {president_max_occurrences} avec {nb_occurrences_max} occurrences.")





