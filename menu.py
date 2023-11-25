from function import *
from main import *
from tkinter import *

#creer la fenetre
window = Tk()
window.geometry("720x460")
window.title("Password")
window.iconbitmap("logo.ico")
window.config(background="#052389")

''''#création du menu
menu_bar = Menu(window)

file_menu = Menu(menu_bar,tearoff=0)
file_menu.add(label="Nom Fichier", command=mots_moins_importants(matrice_tfidf, mots_uniques))

#configurer la barre menu dans la window
window.config(menu=menu_bar)'''


# ouvrir fenetre
window.mainloop()