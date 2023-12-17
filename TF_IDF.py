import os
import math
from fonctionnalité_TF_IDF import *
from fonctions_de_base import *


'''Ce fichier comporte les fonctions nécessaire à la création et à l'affichage de la matrice TF-IDF du corpus de textes'''
## Début Matrice TF-IDF ##

    # TF

def dico_TF(input_dir, file_names_cleaned): #fonction qui crée le dictionnaire des scores TF de la liste des fichiers désirés
    occurrence = {}

    for input_name in file_names_cleaned:
        input_path = os.path.join(input_dir, input_name)
        if os.path.isfile(input_path):
            with open(input_path, 'r', encoding='utf-8') as fichier:
                content = fichier.read()
                mots = content.split()                 #diviser le contenu en mots

                for mot in mots:                #parcourir chaque mot et mettre a jour le dictionnaire
                    if input_name not in occurrence:
                        occurrence[input_name] = {}
                    occurrence[input_name][mot] = occurrence[input_name].get(mot, 0) + 1

    return occurrence

#IDF

def calculer_idf(repertoire_corpus):    #fonction qui calcule le score IDF du répertoire entré en paramètre

    doc_contenant_mot = {}  #créer dictionnaire qui stocke le nombre de doc contenant chaque mot
    total_doc = 0       #total de documents dans le corpus

    for nom_fichier in os.listdir(repertoire_corpus):       #parcourir tous les fichiers du corpus
        chemin_fichier = os.path.join(repertoire_corpus, nom_fichier)

        if os.path.isfile(chemin_fichier):      #verifier si le chemin est un fichier
            total_doc += 1

            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()

                mots = contenu.split()

                mots_uniques = set(mots) #crée un set des mots afin de n'avoir aucun doublons

                for mot in mots_uniques:
                    doc_contenant_mot[mot] = doc_contenant_mot.get(mot, 0) + 1

    idf_scores = {}     #calcul du score IDF pour chaque mot
    for mot, nb_documents_contenant in doc_contenant_mot.items():
        idf_scores[mot] = math.log(total_doc / (nb_documents_contenant))

    return idf_scores


#matrice TF-IDF

def calculer_tf_idf_matrix(repertoire_corpus, file_names_cleaned):  #crée la matrice TF_IDF du répertoire mis en paramèetre avec la liste des fichiers à traiter

    tf_dict = dico_TF(repertoire_corpus, file_names_cleaned)    #calcul le dictionnaire TF

    idf_dict = calculer_idf(repertoire_corpus)      #calcul du dictionnaire IDF

    mots_uniques = list(set(tf_dict.keys()).union(idf_dict.keys()))     #converti le set de mots en liste qui ne contient donc pas de doublosn

    matrice_tfidf = [[0.0] * len(file_names_cleaned) for _ in range(len(mots_uniques))]    #initialise la matrice TF-IDF avec des zéros

    for i, mot in enumerate(mots_uniques):      #remplissage la matrice TF-IDF en multipliant les valeurs correspondantes de TF et IDF
        for j, file_name in enumerate(file_names_cleaned):
            tf_value = tf_dict.get(file_name, {}).get(mot, 0)
            idf_value = idf_dict.get(mot, 0)
            matrice_tfidf[i][j] = tf_value * idf_value  #stock uniquement le score TF-IDF

    matrice_tfidf_transposee = transposee_matrice(matrice_tfidf)    #calcule la transposée de la matrice

    return matrice_tfidf_transposee, mots_uniques



def transposee_matrice(matrice):    #fonction qui prend en paramètre la matrice et en calcule la transposée
    nb_lignes, nb_colonnes = len(matrice), len(matrice[0])
    matrice_transposee = []

    for j in range(nb_colonnes):
        nouvelle_colonne = []
        for i in range(nb_lignes):
            nouvelle_colonne.append(matrice[i][j])
        matrice_transposee.append(nouvelle_colonne)

    return matrice_transposee



def afficher_matrice(matrice_tfif, file_names, mots_uniques):   #fonction prend en paramètre la matrice, la liste des
                                                                #mots unique et les noms des fichiers pour afficher la matrice d'une certaine façon
    header = [""] + mots_uniques
    print(" ; ".join(header))

    for i, ligne in enumerate(matrice_tfif):    #parcourir chaque ligne de la matrice (correspondant à un fichier)
        print(file_names[i], end=" : ")  #afficher le nom du fichier

        for valeur in ligne:            #afficher les valeurs TF-IDF pour chaque mot
            print(round(valeur, 2), end=" ; ")

        print()  #passe à la ligne suivante
