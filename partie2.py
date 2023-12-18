from TF_IDF import*
from fonctionnalité_TF_IDF import *
import math

'''Ce fichier comporte toutes les fonctionnalités de la partie 2 du projet telles que la tokenisation 
d'une question ou la création de son vecteur TF-IDF'''

#PARTIE 2

def tokenisation(question): #prend en paramètre une question et renvoie une liste des mots de la question

    question = nettoyer_texte(question)
    question = question.lower()
    mots_question = question.split()

    return mots_question

def commun_question_corpus(question):   #prend en paramètre une question et renvoie la liste des mots communns
                                        # à la question et au corpus
    corpus = "cleaned"
    mots_corpus = set()         #sortir les mots uniques de tous les fichiers
    mots_uniques = mots_unique()
    mots_question = set(tokenisation(question))
    mots_communs = mots_question.intersection(mots_uniques)

    return list(mots_communs)


#VECTEUR TF-IDF DE LA QUESTION
def calcul_tf(question):    #prend en paramètre une question et renvoie le score TF de chaque mots
    mots = tokenisation(question)
    tf_question = {}
    for mot in mots:
        tf_question[mot] = tf_question.get(mot, 0) + 1  #de façon similaire à notre fonction dico_TF

    return tf_question
def vecteur_tfidf(question, repertoire): #prend une question et un repertoire pour en renvoyer le vecteur TF-IDF
    TF_mots_Question = calcul_tf(question)
    IDF_corpus = calculer_idf(repertoire)

    TF_IDF_Matrice2 = []
    for mot, idf_score in IDF_corpus.items():
        if mot in TF_mots_Question :
            score_tf = TF_mots_Question.get(mot, 1)
        else:
            score_tf = 0

        score_TF_IDF = idf_score * score_tf
        TF_IDF_Matrice2.append([mot, score_TF_IDF])

    return TF_IDF_Matrice2



# vecteur corpus texte
def vecteur_tfidf_texte(chemin_fichier, matrice_tfidf, mots_uniques, files_name):
    chemin_fichier = os.path.join('cleaned', files_name)

    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()

    mots_texte = contenu.split()

    # Créer un dictionnaire pour mapper les mots à leurs indices dans mots_uniques
    indice_mot_map = {mot: indice for indice, mot in enumerate(mots_uniques)}

    vecteur_tfidf = [0.0] * len(mots_uniques)

    for mot in mots_texte:
        # Utiliser le dictionnaire pour obtenir l'indice du mot
        indice_mot = indice_mot_map.get(mot, None)

        # Vérifier que l'indice est dans la plage de la liste matrice_tfidf
        if indice_mot is not None and 0 <= indice_mot < len(matrice_tfidf):
            score_tfidf = matrice_tfidf[indice_mot][0]
            vecteur_tfidf[indice_mot] = score_tfidf

    return vecteur_tfidf

# produit scalaire

def produit_vectoriel(vecteur_question1, vecteurs_corpus):
    # Extraire les vecteurs TF-IDF du tuple (mot, score) dans une liste
    vecteurs_tfidf = [score for mot, score in vecteurs_corpus]

    # Calculer le produit vectoriel
    resultat = sum(x * y for x, y in zip(vecteur_question1, vecteurs_corpus))

    return resultat


'''def prod_scalaire(vecteur_question, matrice,vecteur_tfidf_texte):   #prend en paramètres le vecteur de la question et d'un texte
                                                # et en renvoie le produit scalaire
    resultat = 0
    for tfidf_question, tfidf_matrice in zip(vecteur_question, matrice):
        resultat += float(tfidf_matrice[i]) * float(tfidf_question[i])

    return resultat

## Norme vecteur question
def norme_vecteur_question(vecteur_question1): #calcule la longueur (norme euclidienne) du vecteur question

    somme_carres = sum(componente**2 for componente in vecteur_question1)
    longueur = math.sqrt(somme_carres)
    return longueur


## Norme vecteur corpus

def norme_vecteur_texte():  #calcule la longueur (norme euclidienne) du vecteur corpus.

    somme_carres = sum(componente**2 for componente in vecteur_tfidf_texte('cleaned', vecteur_texte, mots_uniques))
    longueur = math.sqrt(somme_carres)
    return longueur

def calcul_similarite(norme_vecteur_question, norme_vecteur_corpus, produit_scalaire):
    #prend la norme des vecteurs question et corpus ainsi que leur produit scalaire pour en renvoyer l'angle de similarité
    similarite = produit_scalaire / norme_vecteur_question * norme_vecteur_corpus
    return similarite'''
