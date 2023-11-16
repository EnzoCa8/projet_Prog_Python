from function import*
L = []
titre = "Nomination_Chirac1.txt"
L.append(nom_pres(titre))

titre = "Nomination_Chirac2.txt"
L.append(nom_pres(titre))

titre = "Nomination_Giscard dEstaing.txt"
L.append(nom_pres(titre))

titre = "Nomination_Hollande.txt"
L.append(nom_pres(titre))

titre = "Nomination_Macron.txt"
L.append(nom_pres(titre))

titre = "Nomination_Mitterrand1.txt"
L.append(nom_pres(titre))

titre = "Nomination_Mitterrand2.txt"
L.append(nom_pres(titre))

liste_sans_doublons = []
for element in L:
    if element not in liste_sans_doublons:
        liste_sans_doublons.append(element)

print(liste_sans_doublons)

