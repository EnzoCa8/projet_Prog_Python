from function import *
from tkinter import *

#creer la fenetre
window = Tk()
window.geometry("720x460")
window.title("Password")
window.iconbitmap("logo.ico")
window.config(background='#4064A4')

#creer le menu
menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label= "Score TD-IDF")
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

#afficher menu
window.config(menu=menu_bar)



# ouvrir fenetre
window.mainloop()