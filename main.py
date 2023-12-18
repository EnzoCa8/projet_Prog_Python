from TF_IDF import *
from partie2 import *





directory = "./speeches"
files_names = list_of_files(directory, "txt")
#print(files_names)


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

#print(liste_sans_doublons)

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
#print(resultat_dico_tf)

#IDF


repertoire_corpus = 'cleaned'
idf_resultats = calculer_idf(repertoire_corpus)
print(idf_resultats)


#matrice TF IDF*P


repertoire_corpus = 'cleaned'
files_to_process_input = input("Entrez la liste des fichiers à traiter séparés par des espaces: ")
files_to_process = files_to_process_input.split()


#matrice_tfidf_resultat, mots_uniques = calculer_tf_idf_matrix(repertoire_corpus, files_to_process)
#print("Mots uniques:", mots_uniques)
#print("Matrice TF-IDF:", matrice_tfidf_resultat)
matrice_tfidf_transposee, mots_uniques = calculer_tf_idf_matrix(repertoire_corpus, file_names_cleaned)
afficher_matrice(matrice_tfidf_transposee, file_names_cleaned, mots_uniques)

#fonctionnalités matrice TFIDF

matrice_tfidf, mots_uniques = calculer_tf_idf_matrix(repertoire_corpus, file_names_cleaned)


#fonctionnalités matrice TFIDF

valeur = int(input("Quelles fonctionnalité voulez vous utilisez ?\n"
                       " 1 pour la liste des mots les moins importants,\n"
                       " 2 pour les mots ayant le score TD-IDF le plus élevé,\n"
                       " 3 pour le mot le plus répété par Chirac dans ses discours,\n"
                       " 4 pour savoir quel président a le plus parlé de la nation,\n"
                       " 5 pour savoir quel président a parlé de l'écologie ou du climat\n"
                       " 6 pour le chat bot"))
matrice_tfidf, mots_uniques = calculer_tf_idf_matrix(repertoire_corpus, file_names_cleaned)
if valeur < 1:
    valeur = int(input("Quelles fonctionnalité voulez vous utilisez ?\n"
                       " 1 pour la liste des mots les moins importants,\n"
                       " 2 pour les mots ayant le score TD-IDF le plus élevé,\n"
                       " 3 pour le mot le plus répété par Chirac dans ses discours,\n"
                       " 4 pour savoir quel président a le plus parlé de la nation,\n"
                       " 5 pour savoir quel président a parlé de l'écologie ou du climat\n"
                       " 6 pour le chat bot"))

#fonctionalité 1
# Appeler la fonction pour obtenir la liste des mots moins importants
elif valeur == 1 :
    '''mots_pas_importants = mots_pas_importants(matrice_tfidf, repertoire_corpus)

    # Afficher les résultats

    print("Mots ayant le score TF-IDF le moins élevé :", mots_pas_importants)
    print(len(mots_pas_importants))'''
    mot_pas_important2 = mot_pas_important2(matrice_tfidf)
    print("Mots ayant le score TF-IDF le moins élevé :", mot_pas_important2)


#fonctionalité 2
# Appeler la fonction pour afficher les mots ayant le score TD-IDF le plus élevé
elif valeur == 2:
    mots_importants_tfidf, scores_max_tfidf = mots_plus_importants_tfidf(matrice_tfidf, mots_uniques)

    # Afficher les résultats
    mots_importants_tfidf, scores_max_tfidf = mots_plus_importants_tfidf(matrice_tfidf_transposee, mots_uniques)
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
# président qui ont parlé au moins une foie de climat ou d'écologie
elif valeur == 5:
    président_qui_ont_parlé_climat_ou_ecologie(repertoire_corpus, file_names_cleaned)

elif valeur == 6:


#fonctionnalité PARTIE 2

#TOKENISATION
    question1 = "Le climat est-il important"
    print(question1)
#print(tokenisation(question1))
#print(calcul_tf(question1))
#matrice1= matrice_tfidf_transposee

#MOTS COMMUNS QUESTION/CORPUS

    mots_en_commun = commun_question_corpus(question1)
    print(mots_en_commun)

#VECTEUR TF-IDF
    vecteur_question1 = vecteur_tfidf(question1, 'cleaned')
    print(vecteur_question1)


    vecteur_corpus = vecteur_tfidf_texte('cleaned',matrice_tfidf,mots_uniques, file_names_cleaned[0])
    print(vecteur_corpus)
    print(len(vecteur_corpus))

#PRODUIT SCALAIRE


    produit_scalaire = produit_vectoriel(vecteur_question1,vecteur_corpus)
    print(produit_scalaire)

'''matrice1= matrice_tfidf_transposee
produit_scalaire = prod_scalaire(vecteur_question1, matrice1)
print(produit_scalaire)


#Norme du vecteur question

norme_vecteur_question = norme_vecteur_question(question1)
print(f"La longueur du vecteur {vecteur_question1} est : {norme_vecteur_question}")

# Norme du vecteur corpus
norme_vecteur_corpus = norme_vecteur_corpus(vecteur)
print(f"La longueur du vecteur {vecteur_question1} est : {norme_vecteur_corpus}")

# Calule similarity
similary = calcul_similarity()'''
