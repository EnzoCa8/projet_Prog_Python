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
#convertir_en_minuscules(input_directory, output_directory)

if __name__ == "__main__":
    parcourir_repertoire()


## Début Matrice TF-IDF ##

# TF



