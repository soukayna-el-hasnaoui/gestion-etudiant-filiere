from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

import mysql.connector as mysql

from SButton import SButton
from SEntry import SEntry
from SLabel import SLabel


class GF(Tk):
    def __init__(self):
        Tk.__init__(self)
        self['bg'] = 'white'
        self.resizable(False, False)
        self.title('Gestion Filière')
        # le tableau qui contiendra la liste des etudiant
        self.cadre_main = Frame(master=self, bg='#aec4c7')
        self.cadre_main.pack(expand=YES, ipadx=50, ipady=50, pady=20, padx=20, fill=X)

        # les bouttons d'interaction
        self.cadre_btn = Frame(master=self.cadre_main, bg='#aec4c7')
        self.ajouter = SButton(master=self.cadre_btn, text='Ajouter', command=self.gestion_ajout)
        self.ajouter.pack(fill=X, padx=5, side=LEFT)
        self.modification = SButton(master=self.cadre_btn, text='Appliquer les modifs')
        self.modification.bind('<Button-1>', GF.gestion_modif_save)
        self.modification.tk_info = self
        self.modification.pack(fill=X, padx=5, side=LEFT)
        self.cadre_btn.pack(side=BOTTOM, expand=YES, padx=5)

        #
        self.input_elements = []
        self.cadre_interaction_ajout = Frame(self.cadre_main, bg='#e2f1f8', padx=5)
        self.make_ajout_form(self.cadre_interaction_ajout)

        #
        self.cadre_interaction_afficher = Frame(self.cadre_main, bg='#e2f1f8')
        self.make_tab_afficage(self.cadre_interaction_afficher)
        #

    def update_affichage_zone(self):
        self.cadre_interaction_afficher.destroy()
        self.cadre_interaction_afficher = Frame(self.cadre_main, bg='#e2f1f8')
        self.make_tab_afficage(self.cadre_interaction_afficher)

    def update_ajout_zone(self):
        self.cadre_interaction_ajout.destroy()
        self.cadre_interaction_ajout = Frame(self.cadre_main, bg='#e2f1f8', padx=5)
        self.make_ajout_form(self.cadre_interaction_ajout)

    def gestion_ajout(self):
        try:
            db = mysql.connect(
                host='localhost',
                user='root',
                passwd='',
                database='cours_python'
            )
            cursor = db.cursor()
            query = 'insert into filiere (nom) values (%s)'
            values = []
            for i in self.input_elements:
                values.append(i.get())
            #
            ok = True
            for i in values:
                if i is None or i == '':
                    ok = False
            if ok:
                cursor.execute(query, values)
                cursor.close()
            else:
                showerror('Erreur', "Les champs doivent etre correctement  remplie")
            self.update_ajout_zone()
            self.update_affichage_zone()
        except:
            showerror('Erreur', "Une erreur c'est produit !")

    def gestion_modif_save(event):
        try:
            db = mysql.connect(
                host='localhost',
                user='root',
                passwd='',
                database='cours_python'
            )
            cursor = db.cursor()
            query = 'update filiere set nom = %s  where id = %s '
            values = []
            for i in event.widget.tk_info.input_elements:
                values.append(i.get())
            values.append(event.widget.id)
            #
            ok = True
            for i in values:
                if i is None or i == '':
                    ok = False
            if ok:
                cursor.execute(query, values)
                cursor.close()
            else:
                showerror('Erreur', "Les champs doivent etre correctement  remplie")
            event.widget.tk_info.update_ajout_zone()
            event.widget.tk_info.update_affichage_zone()
        except:
            showerror('Erreur', "Cet etudiant n'existe pas")

    def make_ajout_form(self, cadre_interaction_ajout):
        self.input_elements = []
        # nom
        nom_label_ajout = SLabel(master=cadre_interaction_ajout, text='Nom')
        nom_label_ajout.grid(row=0, column=1, pady=5)
        nom_input_ajout = SEntry(cadre_interaction_ajout)
        nom_input_ajout.grid(row=1, column=1, ipady=3, padx=3)
        self.input_elements.append(nom_input_ajout)

        cadre_interaction_ajout.pack(side=TOP, expand=YES, pady=10, ipady=10)

    def make_tab_afficage(self, tab_container):
        pad_x = 7
        pad_y = 5
        entete = SLabel(tab_container, text='Id')
        entete.grid(row=0, column=0, padx=pad_x, pady=pad_y)

        entete = SLabel(tab_container, text='Nom')
        entete.grid(row=0, column=1, padx=pad_x, pady=pad_y)
        ligne = 1
        for i in GF.get_filieres():
            for j in range(2):
                entete = SLabel(tab_container, text=i[j])
                entete.grid(row=ligne, column=j, padx=pad_x, pady=pad_y)
            entete = SButton(tab_container, text='Modifier')
            entete.tk_info = self
            entete.id = i[0]
            entete.bind('<Button-1>', GF.modifier)
            entete.grid(row=ligne, column=3, padx=pad_x, pady=pad_y)
            entete = SButton(tab_container, text='Supprimer')
            entete.id = i[0]
            entete.tk_info = self
            entete.bind('<Button-1>', GF.supprimer)
            entete.grid(row=ligne, column=4, padx=pad_x, pady=pad_y)
            ligne += 1
        tab_container.pack(side=LEFT, expand=YES, ipady=10, ipadx=10)

    def supprimer(event):
        try:
            db = mysql.connect(
                host='localhost',
                user='root',
                passwd='',
                database='cours_python'
            )
            cursor = db.cursor()
            cursor.execute('delete from filiere where id = %s', [event.widget.id])
            cursor.close()
            event.widget.tk_info.update_affichage_zone()
        except:
            showerror('Erreur', "Une erreur s'est produit")

    def modifier(event):
        event.widget.tk_info.modification.id = event.widget.id
        row = event.widget.tk_info.get_filiere(event.widget.id)
        event.widget.tk_info.update_ajout_zone()
        event.widget.tk_info.update_affichage_zone()
        pos = 1
        for i in event.widget.tk_info.input_elements:
            i.insert(0, row[0][pos])
            pos += 1

    @staticmethod
    def get_filieres():
        db = mysql.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cours_python'
        )
        cursor = db.cursor()
        cursor.execute('SELECT * FROM filiere')
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def get_filiere(self, id_):
        db = mysql.connect(
            host='localhost',
            user='root',
            passwd='',
            database='cours_python'
        )
        cursor = db.cursor()
        cursor.execute('SELECT * FROM filiere where id = %s', [id_])
        rows = cursor.fetchall()
        cursor.close()
        return rows
