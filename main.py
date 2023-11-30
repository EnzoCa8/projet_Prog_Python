from function import*


directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)


T = ["Nomination_Chirac1.txt", "Nomination_Chirac2.txt", "Nomination_Giscard dEstaing.txt",
     "Nomination_Hollande.txt", "Nomination_Macron.txt", "Nomination_Mitterrand1.txt", "Nomination_Mitterrand2.txt", "Nomination_Sarkozy.txt"]
L = []
for i in range(len(T)):
    titre = T[i]
    L.append(nom_pres(titre))

liste_sans_doublons = []
for element in L:
    if element not in liste_sans_doublons:
        liste_sans_doublons.append(element)

print(liste_sans_doublons)

# mettre en minuscule les textes
'''convertir_en_minuscules(input_directory, output_directory)'''

# Spécifiez les répertoires d'entrée et de sortie
input_dir = "speeches"
output_dir = "cleaned"

file_names = ["Nomination_Chirac1.txt", "Nomination_Chirac2.txt", "Nomination_Giscard dEstaing.txt",
              "Nomination_Hollande.txt", "Nomination_Macron.txt", "Nomination_Mitterrand1.txt",
              "Nomination_Mitterrand2.txt", "Nomination_Sarkozy.txt"]

file_names_cleaned = ["Nomination_Chirac1_cleaned.txt", "Nomination_Chirac2_cleaned.txt",
                      "Nomination_Giscard dEstaing_cleaned.txt",
                      "Nomination_Hollande_cleaned.txt", "Nomination_Macron_cleaned.txt",
                      "Nomination_Mitterrand1_cleaned.txt", "Nomination_Mitterrand2_cleaned.txt",
                      "Nomination_Sarkozy_cleaned.txt"]

# Appeler la fonction pour nettoyer et copier les fichiers
if __name__ == "__main__":
    parcourir_repertoire()


## Début Matrice TF-IDF ##

# TF

#liste des fichiers cleaned à copier coller au besoin entre dans files_to_process_input :
#Nomination_Chirac1_cleaned.txt Nomination_Chirac2_cleaned.txt Nomination_Giscard dEstaing_cleaned.txt Nomination_Hollande_cleaned.txt Nomination_Macron_cleaned.txt Nomination_Mitterrand1_cleaned.txt Nomination_Mitterrand2_cleaned.txt Nomination_Sarkozy_cleaned.txt


repertoire_corpus = 'cleaned'
files_to_process_input = input("Entrez la liste des fichiers à traiter séparés par des espaces: ")
files_to_process = files_to_process_input.split()

resultat_dico_tf = dico_TF(repertoire_corpus, files_to_process)
print(resultat_dico_tf)

#IDF

repertoire_corpus = 'cleaned'
idf_resultats = calculer_idf(repertoire_corpus)
print(idf_resultats)

#matrice TF IDF


repertoire_corpus = 'cleaned'
files_to_process_input = input("Entrez la liste des fichiers à traiter séparés par des espaces: ")
files_to_process = files_to_process_input.split()

matrice_tfidf_resultat, mots_uniques = calculer_tf_idf_matrix(repertoire_corpus, files_to_process)
print("Mots uniques:", mots_uniques)
print("Matrice TF-IDF:")
matrice_transposee = transposee_matrice(matrice_tfidf_resultat)
afficher_matrice(matrice_transposee)

#fonctionnalités matrice TFIDF

matrice_tfidf, mots_uniques = calculer_tf_idf_matrix(repertoire_corpus, file_names_cleaned)
##1er fonctionnalités
# Appeler la fonction pour obtenir la liste des mots moins importants
mots_non_importants = mots_moins_importants(matrice_tfidf, mots_uniques)
print("Mots non importants:", mots_non_importants)

##2ème fonctionnalité
# Appeler la fonction pour afficher les mots ayant le score TD-IDF le plus élevé
mots_importants_tfidf, scores_max_tfidf = mots_plus_importants_tfidf(matrice_tfidf, mots_uniques)

# Afficher les résultats
print("Mots ayant le score TF-IDF le plus élevé :", mots_importants_tfidf)
print("Scores TF-IDF correspondants :", scores_max_tfidf)

##3ème fonctionnalité
#Appeler la fonction indiquant le mot le plus répété par Chirac dans ses discours
mots_plus_repetes_par_chirac(repertoire_corpus, file_names_cleaned)

##4eme fonctionnalité
# Utilisation de la fonction qui indique quel président a le plus parlé de la nation
president_avec_plus_parle_de_nation(repertoire_corpus, file_names_cleaned)

##5eme fonctionnalité
# Utilisation de la fonction indiquant quel président a parlé de l'écologie ou du climat en premier
matrice_tfidf, mots_uniques = calculer_tf_idf_matrix(repertoire_corpus, file_names_cleaned)
president_plus_tot_a_parler_climat_ecologie(matrice_tfidf, mots_uniques, file_names_cleaned)

##6ème fonctionnalité
# fonction des mots communs à tous les présidents
#seuil_presence = 0.1
#resultat_mots_communs = mots_communs_tous_presidents(matrice_tfidf, mots_uniques, file_names_cleaned, seuil_presence)

mots_communs_tous_presidents('./cleaned/')