from function import*


valeur = int(input("Quelles fonctionnalité voulez vous utilisez ? Taper 1 pour la liste des mots les moins importants, 2 pour les mots ayant le score TD-IDF le plus élevé, 3 pour le mot le plus répété par Chirac dans ses discours, 4 pour savoir quel président a le plus parlé de la nation"
      "5 pour savoir quel président a parlé de l'écologie ou du climat en premier et 6 pour les mots communs à tous les présidents"))
matrice_tfidf, mots_uniques = calculer_tf_idf_matrix(repertoire_corpus, file_names_cleaned)
if valeur < 1:
    valeur = int(input("Quelles fonctionnalité voulez vous utilisez ? Taper 1 pour la liste des mots les moins importants, 2 pour les mots ayant le score TD-IDF le plus élevé, "
                       "3 pour le mot le plus répété par Chirac dans ses discours, 4 pour savoir quel président a le plus parlé de la nation"
                       "5 pour savoir quel président a parlé de l'écologie ou du climat en premier et 6 pour les mots communs à tous les présidents"))

#fonctionalité 1
# Appeler la fonction pour obtenir la liste des mots moins importants
elif valeur == 1 :
    mots_non_importants = mots_moins_importants(matrice_tfidf, mots_uniques)
    print("Mots non importants:", mots_non_importants)

#fonctionalité 2
# Appeler la fonction pour afficher les mots ayant le score TD-IDF le plus élevé
elif valeur == 2:
    mots_importants_tfidf, scores_max_tfidf = mots_plus_importants_tfidf(matrice_tfidf, mots_uniques)

    # Afficher les résultats
    print("Mots ayant le score TF-IDF le plus élevé :", mots_importants_tfidf)
    print("Scores TF-IDF correspondants :", scores_max_tfidf)

#fonctionalité 3
#Appeler la fonction indiquant le mot le plus répété par Chirac dans ses discours
elif valeur ==3:
    mots_plus_repetes_par_chirac(repertoire_corpus, file_names_cleaned)

##4eme fonctionnalité
# Utilisation de la fonction qui indique quel président a le plus parlé de la nation
elif valeur == 4:
    president_avec_plus_parle_de_nation(repertoire_corpus, file_names_cleaned)

##5eme fonctionnalité
# Utilisation de la fonction indiquant quel président a parlé de l'écologie ou du climat en premier
elif valeur == 5:
    matrice_tfidf, mots_uniques = calculer_tf_idf_matrix(repertoire_corpus, file_names_cleaned)
    president_plus_tot_a_parler_climat_ecologie(matrice_tfidf, mots_uniques, file_names_cleaned)

##6ème fonctionnalité
# fonction des mots communs à tous les présidents
elif valeur == 6:
    file_names_cleaned = ["Nomination_Chirac1_cleaned.txt", "Nomination_Chirac2_cleaned.txt",
                          "Nomination_Giscard dEstaing_cleaned.txt",
                          "Nomination_Hollande_cleaned.txt", "Nomination_Macron_cleaned.txt",
                          "Nomination_Mitterrand1_cleaned.txt", "Nomination_Mitterrand2_cleaned.txt",
                          "Nomination_Sarkozy_cleaned.txt"]
    mots_communs_tous_presidents(mots_uniques, file_names_cleaned,'./cleaned')

