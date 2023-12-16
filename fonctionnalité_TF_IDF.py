from fonctions_de_base import *
from TF_IDF import*


#fonctionnalité TFIDF

def mots_moins_importants(matrice_tfidf, repertoire_corpus):
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

    mots_non_importants = []

    # Parcourir les mots uniques
    for i, mot in enumerate(mots_uniques):

        # Récupérer les indices du mot dans la matrice
        indice_mot = [indice for indice, valeur in enumerate(matrice_tfidf) if valeur[0] == mot]

        # Vérifier si le TD-IDF est nul dans tous les fichiers
        if all(matrice_tfidf[indice][1] == 0 for indice in indice_mot):
            mots_non_importants.append(mot)

    return mots_non_importants

def mots_tfidf_zero_list(matrice_tfidf,file_names_cleaned, repertoire_corpus):
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
                mots = contenu.spit()

                # Identifier les mots uniques dans le fichier
                mots_uniques = set(mots)
    mots_tfidf_zero = []

    # Parcourir les indices de mots uniques
    for i, mot in enumerate(mots_uniques):
        # Vérifier si l'indice i est dans les limites de la matrice
        if i < len(matrice_tfidf):
            # Obtenir les scores TF-IDF pour le mot courant
            tfidf_scores = [float(score) for score in matrice_tfidf[i]]

            # Vérifier si tous les scores TF-IDF sont égaux à zéro
            if all(score == 0.0 for score in tfidf_scores):
                mots_tfidf_zero.append(mot)

    return mots_tfidf_zero


def mots_plus_importants_tfidf(matrice_tfidf, mots_uniques):
    mots_importants_tfidf = []
    scores_max_tfidf = []

    # Parcourir chaque colonne de la matrice (correspondant à un mot)
    for i, mot_tfidf in enumerate(matrice_tfidf):
        # Trouver le score TF-IDF maximal et le mot correspondant
        max_tfidf = max(mot_tfidf)
        mot_max_tfidf = mots_uniques[mot_tfidf.index(max_tfidf)]

        # Ajouter le mot et le score maximal aux listes correspondantes
        mots_importants_tfidf.append(mot_max_tfidf)
        scores_max_tfidf.append(max_tfidf)

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
            print("Le fichier de Jacques Chirac", "(fichier_chirac)", "n'a pas été trouvé dans le corpus.")

    # Afficher les résultats
    for fichier, mots_plus_repetes in mots_plus_repetes_par_fichier:
        print("Le(s) mot(s) le(s) plus répété(s) par le président Chirac dans le fichier", fichier, ":", mots_plus_repetes)




#fonction indiquant quel président a le plus parlé de la nation


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
    print("Le président qui a le plus parlé de la nation est", president_max_occurrences, "avec", nb_occurrences_max,"occurrences.")



#fonction quel président a parlé en premier du climat et/ou de l'écologie

def president_plus_tot_a_parler_climat_ecologie(matrice_tfidf, mots_uniques, file_names_cleaned):
    # Initialiser un dictionnaire pour stocker la première occurrence de parler de climat ou d'écologie par président
    premier_parler = {}

    # Parcourir les fichiers
    for j, file_name in enumerate(file_names_cleaned):
        # Parcourir les mots uniques
        for i, mot in enumerate(mots_uniques):

            # Vérifier si les indices sont dans les limites de la matrice
            if i < len(matrice_tfidf) and j < len(matrice_tfidf[i]):
                # Extraire le mot et sa valeur TF-IDF de la matrice
                mot_tfidf = matrice_tfidf[i][j]

                # Vérifier si le mot concerne le climat ou l'écologie
                if any(keyword in mot.lower() for keyword in ["climat", "écologie"]):
                    # Vérifier si le président est déjà dans le dictionnaire
                    if file_name not in premier_parler:
                        premier_parler[file_name] = {"mot": mot, "valeur_tfidf": float(mot_tfidf[1])}

    # Vérifier si des présidents ont été trouvés
    if premier_parler:
        # Trouver le président qui a parlé en premier
        premier_president = min(premier_parler, key=lambda x: premier_parler[x]["valeur_tfidf"])

        # Afficher le résultat
        print("Le président qui a parlé en premier du climat ou de l'écologie est", premier_president," avec le mot", premier_parler[premier_president]['mot'], " et une valeur TF-IDF de", premier_parler[premier_president]['valeur_tfidf'])
        return premier_president
    else:
        print("Aucun président n'a été trouvé parlant du climat ou de l'écologie dans la matrice TD-IDF.")
        print("Aucun président n'a été trouvé parlant du climat ou de l'écologie dans la matrice TD-IDF.")
        return None



#fonction des mots communs à tous les présidents

def mots_communs_tous_presidents(directory):
    # Liste pour stocker les mots de chaque président
    mots_par_president = []

    # Parcourir les fichiers
    for file_name in list_of_files(directory, '.txt'):
        # Lire le fichier et extraire les mots uniques
        with open(os.path.join(directory, file_name), 'r', encoding='utf-8') as file:
            mots_president = set(file.read().split())
            mots_par_president.append(mots_president)

    # Trouver l'intersection des ensembles de mots de chaque président
    mots_communs = set.intersection(*mots_par_president)

    # Afficher le résultat final
    print("Mots communs à tous les présidents :", mots_communs)

    return mots_communs
