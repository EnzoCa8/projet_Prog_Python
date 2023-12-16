import os
import math


## Début Matrice TF-IDF ##

    # TF

def dico_TF(input_dir, file_names_cleaned):
    #créer dictionnaire des occurrences
    occurrence = {}

    for input_name in file_names_cleaned:    #parcourir chaque fichier
        input_path = os.path.join(input_dir, input_name)
        if os.path.isfile(input_path):              #checker si le fichier d'entrée existe
            with open(input_path, 'r', encoding='utf-8') as fichier:
                content = fichier.read()
                mots = content.split()                 #diviser le contenu en mots

                for mot in mots:                #parcourir chaque mot et mettre a jour le dictionnaire
                    if input_name not in occurrence:                    # Mettre à jour le dictionnaire des occurrences
                        occurrence[input_name] = {}
                    occurrence[input_name][mot] = occurrence[input_name].get(mot, 0) + 1

    return occurrence

#IDF

def calculer_idf(repertoire_corpus):
    #créer dictionnaire qui stocke le nombre de doc contenant chaque mot
    doc_contenant_mot = {}

    #total de documents dans le corpus
    total_doc = 0

    #parcourir tous les fichiers du corpus
    for nom_fichier in os.listdir(repertoire_corpus):
        chemin_fichier = os.path.join(repertoire_corpus, nom_fichier)

        # Vérifier si le chemin est un fichier
        if os.path.isfile(chemin_fichier):
            total_doc += 1

            # Lire le contenu du fichier
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()

                # Diviser le contenu en mots
                mots = contenu.split()

                # Identifier les mots uniques dans le fichier
                mots_uniques = set(mots)

                # Mettre à jour le dictionnaire des documents contenant chaque mot
                for mot in mots_uniques:
                    doc_contenant_mot[mot] = doc_contenant_mot.get(mot, 0) + 1

    # Calculer le score IDF pour chaque mot
    idf_scores = {}
    for mot, nb_documents_contenant in doc_contenant_mot.items():
        idf_scores[mot] = math.log(total_doc / (nb_documents_contenant))

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
            matrice_tfidf[i][j] = tf_value * idf_value  # Stocker uniquement le score TF-IDF

    # Calculer la transposée de la matrice
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



def afficher_matrice(matrice, file_names, mots_uniques):
    header = [""] + mots_uniques
    print(" ; ".join(header))

    # Parcourir chaque ligne de la matrice (correspondant à un fichier)
    for i, ligne in enumerate(matrice):
        # Afficher le nom du fichier
        print(file_names[i], end=" : ")

        # Afficher les valeurs TF-IDF pour chaque mot
        for valeur in ligne:
            print(valeur, end=" ; ")

        print()  # Passer à la ligne suivante