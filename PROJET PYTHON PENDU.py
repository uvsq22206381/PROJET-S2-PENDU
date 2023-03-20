import tkinter as tk
import random as rd
from tkinter import ttk
from tkinter import messagebox

# création d'une liste de mots à deviner

themes   =    {'Animaux': ['chien', 'chat', 'lion', 'tigre', 'elephant'],
               'Fruits': ['ppomme', 'banane', 'orange', 'kiwi', 'mangue'],
               'Couleurrs': ['rouge', 'bleu', 'vert', 'jaune', 'violet']}


#crétion de l'interface du jeu

racine = tk.Tk()
racine.title("PENDU")
racine.attributes('-fullscreen', True)
racine.update()
WIDTH = racine.winfo_width()
HEIGHT = racine.winfo_height()
racine.config(bg = "#282828")



menu = tk.Frame(racine, bg="#282828")
menu.pack(pady = 50)
title = tk.Label(menu, text = 'HangMan', font = 'jokerman 60 bold italic', bg = "#282828")
title.pack(pady = 20)


#création liste de themes
choisir_theme = tk.Label(menu, text = 'Choisir un thème de mot:', font = 'helvetica 20 italic', fg = 'white', bg ="#282828")
choisir_theme.pack(pady = 10)
theme_options = StringVar()
choix_theme = ttk.Combobox(menu, textvariable= theme_options, width = 20, state="readonly")                    
choix_theme['values'] = list(themes.keys())
choix_theme.current(0)
choix_theme.pack(pady = 10)

#création liste longueur de mot
choisir_long_mot = tk.Label(menu, text = 'Choisir la longueur du mot:', font = 'helvetica 20 italic', fg = 'white', bg ="#282828")
choisir_long_mot.pack(pady = 10)
longueur_mot = []                                               
a = list(themes.values())
for i in a:
        for j in i:
                longueur_mot.append(len(j))
longueur_mot = set(sorted(longueur_mot))
choix_longueur = ttk.Combobox(menu, width = 20, state="readonly")
choix_longueur['values'] = list(longueur_mot)
choix_longueur.current(0)
choix_longueur.pack(pady = 10)
longueur_selec = choix_longueur.get()
sortie = tk.Button(menu, text="Exit", font=("Helvetica", 20, "bold"), fg="white", bg="#F44336", command = racine.destroy)

def transition():
        menu.pack_forget()
        keyboard_frame.pack(side= "bottom", pady=20)
        sortie.pack(padx = 300)
        x1  = 530
        y1  = 450
        for i in range(len(Mot_séparé)):                      #Création des tirets correspondant à chaque lettre

                List_dash.append(tk.Label(racine, text = "_", font = "times, 80", bg ="#282828"))
                List_dash[i].place(x = x1, y = y1)
                x1+= 60

play_button = tk.Button(menu, text="Commencer", font=("Helvetica", 20, "bold"), fg="white", bg="#4CAF50", command = transition)
play_button.pack(pady=20)

        # exit button
exit_button = tk.Button(menu, text="Exit", font=("Helvetica", 20, "bold"), fg="white", bg="#F44336", command = racine.destroy)
exit_button.pack(pady=20)



        # set up the game canva
game_canvas = Canvas(menu, bg="#282828", highlightthickness=0)
game_canvas.pack(fill=BOTH, expand=True)

        # set up the keyboard
keyboard_frame = tk.Frame(racine, bg="#282828")

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
buttons = []
for letter in letters:
         button = tk.Button(keyboard_frame, text=letter, font=("Helvetica", 18), bg="#333333", width=3, height=1, command= lambda: letter_check(letter))
         buttons.append(button)
for i in range(3):
            for j in range(8):
                button = buttons[i*9+j]
                button.grid(row=i, column=j, padx=3, pady=3)

canvas = tk.Canvas(racine, bg ='white', width = 400, height = 400)
canvas.pack(side = "top", pady = 20)



theme_selec = theme_options.get() 

Mot = rd.choice(themes[theme_selec])     #Choix du mot à deviner au hasard
Mot_séparé = [x for x in Mot]        
List_dash = []
guesses = set(Mot_séparé.copy())




def affichage_lettre(event):            #Fonction qui affiche une lettre correctement choisie
        for i in range(len(List_dash)):   
                if Mot_séparé[i] == event.char:
                    List_dash[i].config(text = (event.char).upper(), font = "times, 60", fg = 'white')
        guesses.remove(event.char)
        if list(guesses) == []:
                messagebox.showinfo("Félicitations", "c'est gagné!!!")
                racine.destroy()


def etape1():                           #Dessin de la potence

        canvas.create_line((80,360),(320,360), fill = 'black', width = 5)
        canvas.create_line((120,360),(120,40),(240,40),(240,72), fill = 'black', width = 5)
        canvas.create_line((120,80),(152,40), fill = 'black', width = 5)

def etape2():                           #Dessin de la tête

        canvas.create_oval((208,72),(272,136), outline = 'black', width = 5)

def etape3():                           #Dessin du corps

        canvas.create_line((240,136),(240,256), fill = 'black', width = 5)

def etape4():                           #Dessin de la main gauche

        canvas.create_line((240,184),(192,144), fill = 'black', width = 5)

def etape5():                           #Dessin de la main droite

        canvas.create_line((240,184),(288,144), fill = 'black', width = 5)

def etape6():                           #Dessin du pied gauche

        canvas.create_line((240,254),(200,296), fill = 'black', width = 5)

def etape7():                           #Dessin du pied droit

        canvas.create_line((240,254),(280,296), fill = 'black', width  = 5)

def etape8():                           #Dessin du visage du pendu

        canvas.create_oval((224, 92),(232,100), fill = 'black', width = 2)
        canvas.create_oval((248,92),(256, 100), fill = 'black', width = 2)
        canvas.create_line((222, 124),(240,112),(259,124), fill = 'black', width = 5)

Etapes = [etape1, etape2, etape3, etape4, etape5, etape6, etape7, etape8]
echec = 0

def affichage_pendu():                  #Fonction qui affiche les membres du pendu
        global echec
        Etapes[echec]()
        echec +=1
        if echec ==8 :
                messagebox.showinfo("Vous avez échoué","PENDU!!!")
                racine.destroy()

def letter_check(lettre):             #Fonction qui vérifie si la lettre choisie appartient au mot
        if lettre.char in Mot_séparé:
            affichage_lettre(lettre)
        else:
            affichage_pendu()
            chances = chances -1
        

racine.bind("<KeyPress>", letter_check)
racine.mainloop()
