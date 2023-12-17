from fonctions_de_base import *
from TF_IDF import *

'''Sont ici, les fonctionnalités se servant d'utiliser la matrice TF-IDF précédemment réalisée'''

#fonctionnalité TFIDF

def mots_moins_importants(matrice_tfidf, repertoire_corpus): #fonction qui prend en paramètre la matrice et le
                                                             #répertoire pour renvoyer les mots avec le score TF-IDF le moins élevé
    mots_pas_importants = []
    scores_mini_tfidf = []

    for i, mot_tfidf in enumerate(matrice_tfidf):   #parcourir chaque colonne de la matrice
        mini_tfidf = min(mot_tfidf)      #trouver le score TF-IDF mminimal et le mot correspondant
        mot_mini_tfidf = mots_unique()[mot_tfidf.index(mini_tfidf)]

        mots_pas_importants.append((mot_mini_tfidf))    #ajouter le mot et le score minimal aux listes correspondantes
        scores_mini_tfidf.append(mini_tfidf)

    return mots_pas_importants, scores_mini_tfidf


def mots_plus_importants_tfidf(matrice_tfidf, mots_uniques):    #même principe qu'avant mais avec les scores les plus élevés
    mots_importants_tfidf = []
    scores_max_tfidf = []

    for i, mot_tfidf in enumerate(matrice_tfidf):       #parcourir chaque colonne de la matrice
        max_tfidf = max(mot_tfidf)      #trouver le score TF-IDF maximal et le mot correspondant
        mot_max_tfidf = mots_uniques[mot_tfidf.index(max_tfidf)]
        mots_importants_tfidf.append(mot_max_tfidf)     #ajouter le mot et le score maximal aux listes correspondantes
        scores_max_tfidf.append(max_tfidf)

    return mots_importants_tfidf, scores_max_tfidf


#Fonction indiquant quel mot chirac répète le plus dans ses discours
def mots_plus_repetes_par_chirac(repertoire_corpus, file_names_cleaned): #prend en paramètres le répertoire et la liste des fichiers

    tf_dict = dico_TF(repertoire_corpus, file_names_cleaned)

    fichiers_chirac = ["Nomination_Chirac1_cleaned.txt", "Nomination_Chirac2_cleaned.txt"]

    mots_plus_repetes_par_fichier = []

    for fichier_chirac in fichiers_chirac:    #parcourir les fichiers de Chirac
        if fichier_chirac in tf_dict:
            occurrences_chirac = tf_dict[fichier_chirac]

            mots_plus_repetes = [mot for mot, occ in occurrences_chirac.items() if occ == max(occurrences_chirac.values())]#trouver le(s) mot(s) le(s) plus répété(s)

            mots_plus_repetes_par_fichier.append((fichier_chirac, mots_plus_repetes))
        else:
            print("Le fichier de Jacques Chirac", "(fichier_chirac)", "n'a pas été trouvé dans le corpus.")

        for fichier, mots_plus_repetes in mots_plus_repetes_par_fichier:
            print("Le(s) mot(s) le(s) plus répété(s) par le président Chirac dans le fichier", fichier, ":", mots_plus_repetes)




#fonction indiquant quel président a le plus parlé de la nation


def president_avec_plus_parle_de_nation(repertoire_corpus, file_names_cleaned):#prend en paramètres le répertoire
                                                                               # et la liste de fichiers et renvoie le
                                                                               # nom du président qui a le plus parlé de
                                                                               # la nation
    tf_dict = dico_TF(repertoire_corpus, file_names_cleaned)

    presidents = {
        "Chirac": ["Nomination_Chirac1_cleaned.txt", "Nomination_Chirac2_cleaned.txt"],
        "Giscard d'Estaing": ["Nomination_Giscard dEstaing_cleaned.txt"],
        "Hollande": ["Nomination_Hollande_cleaned.txt"],
        "Macron": ["Nomination_Macron_cleaned.txt"],
        "Mitterrand": ["Nomination_Mitterrand1_cleaned.txt", "Nomination_Mitterrand2_cleaned.txt"],
        "Sarkozy": ["Nomination_Sarkozy_cleaned.txt"]
    }

    occurrences_par_president = {}

    for president, fichiers in presidents.items():
        total_occurrences = 0
        for fichier in fichiers:
            if fichier in tf_dict:
                total_occurrences += tf_dict[fichier].get("nation", 0)

        occurrences_par_president[president] = total_occurrences     #stock le total des occurrences pour le président

    #trouver le président avec le plus d'occurrences du mot "nation"
    president_max_occurrences = max(occurrences_par_president, key=occurrences_par_president.get)
    nb_occurrences_max = occurrences_par_president[president_max_occurrences]

    print("Le président qui a le plus parlé de la nation est", president_max_occurrences, "avec", nb_occurrences_max,"occurrences.")



#fonction quel président a parlé en premier du climat et/ou de l'écologie

def president_plus_tot_a_parler_climat_ecologie(matrice_tfidf, mots_uniques, file_names_cleaned):
#prend en paramètres la matrice, les mots, et la liste de fichiers pour renvoyer le nom du président qui a
#parlé le plus tôt de l'écologie si il y en a un
    premier_parler = {}

    for j, file_name in enumerate(file_names_cleaned):
        for i, mot in enumerate(mots_uniques):

            if i < len(matrice_tfidf) and j < len(matrice_tfidf[i]):#verifie si les indices sont dans les limites de la matrice
                mot_tfidf = matrice_tfidf[i][j]     #extraire le mot et sa valeur TF-IDF de la matrice

                if any(keyword in mot.lower() for keyword in ["climat", "écologie"]):   #verifie si le mot concerne le climat ou l'écologie
                    if file_name not in premier_parler:    #verifie si le président est déjà dans le dictionnaire
                        premier_parler[file_name] = {"mot": mot, "valeur_tfidf": float(mot_tfidf[1])}

    if premier_parler:  #verifie si des présidents ont été trouvés
        premier_president = min(premier_parler, key=lambda x: premier_parler[x]["valeur_tfidf"])

        #
        print("Le président qui a parlé en premier du climat ou de l'écologie est", premier_president," avec le mot", premier_parler[premier_president]['mot'], " et une valeur TF-IDF de", premier_parler[premier_president]['valeur_tfidf'])
        return premier_president
    else:
        print("Aucun président n'a été trouvé parlant du climat ou de l'écologie dans la matrice TD-IDF.")
        return None



#fonction des mots communs à tous les présidents

def mots_communs_tous_presidents(repertoire):    #prend en paramètre le répertoire et renvoie une liste des
                                                 # mots communs à tous les présidents
    mots_par_president = []

    for file_name in list_of_files(repertoire, '.txt'):
        with open(os.path.join(repertoire, file_name), 'r', encoding='utf-8') as file:
            mots_president = set(file.read().split())
            mots_par_president.append(mots_president)

    mots_communs = set.intersection(*mots_par_president)

    print("Mots communs à tous les présidents :", mots_communs)

    return mots_communs
