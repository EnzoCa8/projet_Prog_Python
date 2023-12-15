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
        idf_scores[mot] = math.log(total_documents / (nb_documents_contenant))

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
                mots = contenu.split()

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

#PARTIE 2

def tokenisation(question):

    question = nettoyer_texte(question)
    question = question.lower()
    mots_question = question.split()

    return mots_question

def commun_question_corpus(question):
    #sortir les mots uniques de tous les fichiers
    corpus = "cleaned"
    mots_corpus = set()
    for fichier in os.listdir(corpus):
        corpus = os.path.join(corpus, fichier)
        if os.path.isfile(corpus):
            with open(corpus, "r", encoding="utf-8") as f:
                contenu = f.read()
                mots_fichier = set(contenu.split())
                mots_corpus.update((mots_fichier))
    mots_question = set(tokenisation(question))
    mots_communs = mots_question.intersection(mots_corpus)

    return list(mots_communs)


#VECTEUR TF-IDF DE LA QUESTION
def calcul_tf(question):
    # Calculer la fréquence de chaque mot manuellement
    mots = tokenisation(question)
    tf = {}
    for mot in mots:
        tf[mot] = tf.get(mot, 0) + 1  #de façon similaire à notre fonction dico_TF

    # Normaliser la fréquence en divisant par le nombre total de mots dans la question
    total_mots = len(mots)
    tf_normalized = {mot: freq / total_mots for mot, freq in tf.items()}

    return tf_normalized
def vecteur_tfidf(question, directory):
    TF_mots_Question = calcul_tf(question)
    IDF_corpus = calculer_idf(directory)

    TF_IDF_Matrice2 = []
    for clef, valeur in IDF_corpus.items():

        if clef in TF_mots_Question:
            score_TF = TF_mots_Question[clef]
        else:
            score_TF = 0

        score_TF_IDF = valeur * score_TF
        TF_IDF_Matrice2.append([clef, score_TF_IDF])

    return TF_IDF_Matrice2

