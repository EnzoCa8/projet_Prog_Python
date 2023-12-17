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
def calcul_tf(question):    #prend en paramètre une question et renvoie le score TF de chaque mots
    mots = tokenisation(question)
    tf_question = {}
    for mot in mots:
        tf_question[mot] = tf_question.get(mot, 0) + 1  #de façon similaire à notre fonction dico_TF

    return tf_question
def vecteur_tfidf(question, directory): #prend une question et un repertoire pour en renvoyer le vecteur TF-IDF
    TF_mots_Question = calcul_tf(question)
    IDF_corpus = calculer_idf(directory)

    TF_IDF_Matrice2 = []
    for mot, idf_score in IDF_corpus.items():
        if mot in TF_mots_Question :
            score_tf = TF_mots_Question.get(mot, 1)
        else:
            score_tf = 0

        score_TF_IDF = idf_score * score_tf
        TF_IDF_Matrice2.append([mot, score_TF_IDF])

    return TF_IDF_Matrice2


#PRODUIT SCALAIRE

def vecteur_tfidf_texte(chemin_fichier, matrice_tfidf, mots_uniques): #prend le repertoire, la matrice et les mots
                                                                    # unique pour renvoyer le vecteur TF-IDF d'un texte
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()

    mots_texte = contenu.split()

    vecteur_tfidf = [0.0] * len(mots_uniques)

    for i, mot in enumerate(mots_uniques) :   #remplir le vecteur TF-IDF en utilisant la matrice
        if mot in mots_texte:
            indice_mot = mots_uniques.index(mot)    #si mot est présent dans le fichier, obtenir son indice dans la matrice
            vecteur_tfidf[i] = matrice_tfidf[indice_mot][0]

    return vecteur_tfidf

'''marche pas je vais péter mon crâne ça renvoie 0 à chaque fois'''
def prod_scalaire(vecteur_question, matrice):   #prend en paramètres le vecteur de la question et d'un texte
                                                # et en renvoie le produit scalaire
    resultat = 0
    for tfidf_question, tfidf_matrice in zip(vecteur_question, matrice):
        resultat += tfidf_matrice * tfidf_question

    return resultat

## Norme vecteur question
def norme_vecteur_question(vecteur_question1): #calcule la longueur (norme euclidienne) du vecteur question

    somme_carres = sum(componente**2 for componente in vecteur_question1)
    longueur = math.sqrt(somme_carres)
    return longueur


## Norme vecteur corpus

def norme_vecteur_corpus():  #calcule la longueur (norme euclidienne) du vecteur corpus.

    somme_carres = sum(componente**2 for componente in vecteur_tfidf_texte('cleaned', vecteur, mots_uniques))
    longueur = math.sqrt(somme_carres)
    return longueur

def calcul_similarity(norme_vecteur_question, norme_vecteur_corpus, produit_scalaire):
    #prend la norme des vecteurs question et corpus ainsi que leur produit scalaire pour en renvoyer l'angle de similarité

    similarity = produit_scalaire / norme_vecteur_question * norme_vecteur_corpus
    return similarity





