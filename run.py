from tkinter import *
from GE import *
from GF import *

app = Tk()
app.title('Gestion etudiant | Gestion Filiere')
app.resizable(False, False)
app['bg'] = ''


# commandes
def gestion_e():
    GE().mainloop()


def gestion_f():
    GF().mainloop()

#
cadre_main = Frame(master=app, bg='#aec4c7')
cadre_main.pack(ipadx=150, ipady=150, pady=20, padx=20)
# pour centrer les deux bouttons
cadre = Frame(master=cadre_main, bg='#aec4c7')
cadre.pack(expand=YES, fill=X, padx=50)

btn_etudiant = Button(master=cadre, text="Gestion des étudiants", command=gestion_e, bg='white')
btn_etudiant['font'] = ('Times', 20)
btn_etudiant['relief'] = 'flat'
btn_etudiant.pack(pady=10, fill=X)

btn_filiere = Button(master=cadre, text="Gestion des filières", command=gestion_f, bg='white')
btn_filiere['font'] = ('Times', 20)
btn_filiere['relief'] = 'flat'
btn_filiere.pack(pady=10, fill=X)


# lancement de l'application
app.mainloop()
