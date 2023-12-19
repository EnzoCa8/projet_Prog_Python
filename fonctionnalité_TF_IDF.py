from TF_IDF import *
from fonctions_de_base import *



'''Sont ici, les fonctionnalités se servant d'utiliser la matrice TF-IDF précédemment réalisée'''

#fonctionnalité TFIDF

def mot_pas_important(matrice_tfidf):
    mots_pas_importants = []
    for i, mot_tfidf in enumerate(matrice_tfidf):    #parcourir chaque ligne de la matrice (correspondant à un fichier)
        for valeur in mot_tfidf:            #afficher les valeurs TF-IDF pour chaque mot
            if valeur == 0.0:
                mots_pas_importants.append(mot_tfidf)
    return mots_pas_importants



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
def président_qui_ont_parlé_climat_ou_ecologie(repertoire_corpus, file_names_cleaned):
    tf_dict = dico_TF(repertoire_corpus, file_names_cleaned)
    presidents = {
        "Chirac": ["Nomination_Chirac1_cleaned.txt", "Nomination_Chirac2_cleaned.txt"],
        "Giscard d'Estaing": ["Nomination_Giscard dEstaing_cleaned.txt"],
        "Hollande": ["Nomination_Hollande_cleaned.txt"],
        "Macron": ["Nomination_Macron_cleaned.txt"],
        "Mitterrand": ["Nomination_Mitterrand1_cleaned.txt", "Nomination_Mitterrand2_cleaned.txt"],
        "Sarkozy": ["Nomination_Sarkozy_cleaned.txt"]
    }
    presidents_ecologie = []

    for president, fichiers in presidents.items():
        compte_ecologie = 0
        for fichier in fichiers:
            if fichier in tf_dict:
                # En supposant que dico_TF renvoie un dictionnaire avec les fréquences des termes
                compte_ecologie += tf_dict[fichier].get("écologie", 0) + tf_dict[fichier].get("climat", 0) + tf_dict[fichier].get("climatique",0)
        if compte_ecologie > 0:
            presidents_ecologie.append(president)

    print("Les présidents qui ont mentionné le mot climat ou écologie sont :", presidents_ecologie)


