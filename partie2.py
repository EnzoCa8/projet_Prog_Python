from fonctions_de_base import *
from TF_IDF import*
from fonctionnalité_TF_IDF import *

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
    tf_question = {}
    for mot in mots:
        tf_question[mot] = tf_question.get(mot, 0) + 1  #de façon similaire à notre fonction dico_TF

    return tf_question
def vecteur_tfidf(question, directory):
    TF_mots_Question = calcul_tf(question)
    IDF_corpus = calculer_idf(directory)

    TF_IDF_Matrice2 = []
    for mot, idf_score in IDF_corpus.items():
        if mot in TF_mots_Question :
            score_tf = TF_mots_Question.get(mot, 0)
        else:
            score_tf = 0

        score_TF_IDF = idf_score * score_tf
        TF_IDF_Matrice2.append([mot, score_TF_IDF])

    return TF_IDF_Matrice2


#PRODUIT SCALAIRE

def vecteur_tfidf_texte(chemin_fichier, matrice_tfidf, mots_uniques):
    # Lire le contenu du fichier
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()

    # Diviser le contenu en mots
    mots_texte = contenu.split()

    # Initialiser le vecteur TF-IDF avec des zéros
    vecteur_tfidf = [0.0] * len(mots_uniques)

    # Remplir le vecteur TF-IDF en utilisant la matrice
    for i, mot in enumerate(mots_uniques):
        if mot in mots_texte:
            # Si le mot est présent dans le fichier texte, obtenir son indice dans la matrice
            indice_mot = mots_uniques.index(mot)
            vecteur_tfidf[i] = matrice_tfidf[indice_mot][0]  # Utiliser la valeur TF-IDF du mot dans la matrice

    return vecteur_tfidf

'''marche pas je vais péter mon crâne ça renvoie 0 à chaque fois'''
def prod_scalaire(vecteur_question, matrice):

    resultat = 0
    for tfidf_question, tfidf_matrice in zip(vecteur_question, matrice):
        resultat += tfidf_matrice * tfidf_question

    return resultat







