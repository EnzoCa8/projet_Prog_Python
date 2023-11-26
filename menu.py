import tkinter as tk
from function import *
from main import *

window = tk.Tk()
window.title("Menu pour les fonctionnalités")

# Boutons pour chaque fonctionnalité
button_mots_non_importants = tk.Button(window, text="1. Mots Non Importants", command=mots_non_importants)
button_mots_non_importants.pack(pady=10)

button_mots_importants_tfidf = tk.Button(window, text="2. Mots Importants TF-IDF", command=mots_importants_tfidf)
button_mots_importants_tfidf.pack(pady=10)

button_mots_repetes_par_chirac = tk.Button(window, text="3. Mots Plus Répétés (Chirac)", command=mots_plus_repetes_par_chirac(repertoire_corpus, file_names_cleaned))
button_mots_repetes_par_chirac.pack(pady=10)

button_president_plus_parle_nation = tk.Button(window, text="4. Président Plus Parlé de la Nation", command=president_avec_plus_parle_de_nation(repertoire_corpus, file_names_cleaned))
button_president_plus_parle_nation.pack(pady=10)

button_president_plus_tot_climat_ecologie = tk.Button(window, text="5. Président Plus Tôt (Climat/Écologie)", command=president_plus_tot_a_parler_climat_ecologie(matrice_tfidf, mots_uniques, file_names_cleaned))
button_president_plus_tot_climat_ecologie.pack(pady=10)

button_mots_communs_tous_presidents = tk.Button(window, text="6. Mots Communs Tous Présidents", command=mots_communs_tous_presidents(matrice_tfidf, mots_uniques, file_names_cleaned, seuil_presence))
button_mots_communs_tous_presidents.pack(pady=10)

# Étiquette pour afficher les résultats
result_label = tk.Label(window, text="")
result_label.pack(pady=20)

# Lancez la boucle principale de l'interface graphique
window.mainloop()

