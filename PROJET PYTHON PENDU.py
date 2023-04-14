import tkinter as tk
import random as rd
from tkinter import ttk
from tkinter import messagebox

# création d'une liste de mots à deviner

themes   =    {'Animaux': ['chien', 'chat', 'lion', 'tigre', 'elephant'],
               'Fruits': ['pomme', 'banane', 'orange', 'kiwi', 'mangue'],
               'Couleurs': ['rouge', 'bleu', 'vert', 'jaune', 'violet']}


#création de l'interface du jeu

racine = tk.Tk()
racine.title("PENDU")
racine.attributes('-fullscreen', True)
racine.update()
WIDTH = racine.winfo_width()
HEIGHT = racine.winfo_height()
racine.config(bg = "#282828")


def menu_principal():      #création de l'écran principal du jeu
    global menu
    menu = tk.Frame(racine, bg="#282828")
    menu.pack(pady = 30)
    title = tk.Label(menu, text='le Jeu du Pendu', font = 'jokerman 60 bold italic', bg = "#282828")
    title.pack(pady = 20)
    liste_de_themes()
    combo_themes.current(0)
    liste_de_longueurs()
    play_button = tk.Button(menu, text="Commencer", font=("Helvetica", 20, "bold"), fg="white", bg="#4CAF50", command = transition)
    play_button.pack(pady=20)           #création du bouton pour commencer la partie
    exit_button = tk.Button(menu, text="Quitter", font=("Helvetica", 20, "bold"), fg="white", bg="#F44336", command = racine.destroy)
    exit_button.pack(pady=20)           #création du bouton de sortie du jeu
    
def liste_de_themes():      #fonction qui permet à l'utilisateur de choisir le thème des mots à deviner
    global combo_themes
    choisir_theme = tk.Label(menu, text = 'Choisir un thème de mot:', font = 'helvetica 20 italic', fg = 'white', bg ="#282828")
    choisir_theme.pack(pady = 10)
    theme_options = tk.StringVar()
    combo_themes = ttk.Combobox(menu, textvariable= theme_options, width = 20, state="readonly")                    
    combo_themes['values'] = list(themes.keys())
    combo_themes.pack(pady = 10)
    combo_themes.bind("<<ComboboxSelected>>",  sélection_thème)

def extraction_des_longueurs():       #fonction qui permet d'extraire toutes les longueurs de mots possibles pour un thème donné
    global longueur_des_mots   
    longueur_des_mots = []                      
    mots_du_theme = themes[thème]
    for i in mots_du_theme:
        longueur_des_mots.append(len(i))
    longueur_des_mots = list(set(longueur_des_mots))
    longueur_des_mots.sort()
    
def liste_de_longueurs():       #fonction qui permet à l'utilisateur de choisir la longueur du mot à deviner
    global combo_long
    choisir_long_mot = tk.Label(menu, text = 'Choisir la longueur du mot:', font = 'helvetica 20 italic', fg = 'white', bg ="#282828")
    choisir_long_mot.pack(pady = 10)
    combo_long = ttk.Combobox(menu, width = 20, state="readonly")
    combo_long.pack(pady = 10)
    combo_long.bind("<<ComboboxSelected>>",  sélection_long)

def sélection_thème(event):     ##fonction qui permet de retourner le thème de mots choisi par l'utilisateur
    global thème
    thème = combo_themes.get()
    extraction_des_longueurs()
    combo_long['values'] = list(longueur_des_mots)
    combo_long.current(0)
    
def sélection_long(event):       #fonction qui permet de retourner la longueur du mot choisi par l'utilisateur
    global longueur  
    longueur = combo_long.get()    
    
def transition():       #transition vers le jeu principal
    global jeu
    menu.destroy()
    jeu = tk.Frame(racine, bg="#282828")
    jeu.pack(pady=30)
    cadre_pendu()
    mot_caché()
    dessin_mot()
    clavier_lettres()
    nouvelle_partie()
    jeu.focus_set()
    jeu.bind("<KeyPress>", clavier_ordi)
        
def nouvelle_partie():          #permet de générer une nouvelle partie
    global guesses, wrong_guesses, right_guesses
    dessin_pendu.delete('all')
    wrong_guesses= 0
    guesses = 0
    mot_caché()
    right_guesses = list(set(Mot_séparé))
    List_dash.config(text = ' '.join(["_" if letter!= ' ' else ' ' for letter in Mot]))
    for button in buttons:
        button.config(state = 'normal', relief = 'raised', bg = "#333333")
         
def cadre_pendu():          #crée le cadre dans lequel se formera le pendu
    global dessin_pendu
    dessin_pendu = tk.Canvas(jeu, bg ='white', width = 400, height = 400)
    dessin_pendu.pack(side ="top")

def mot_caché():        #génère le mot aléatoire qu'il faudra deviner
    global Mot, Mot_séparé
    Mot = ''
    while len(Mot) != int(longueur):
        Mot = rd.choice(themes[thème])
    Mot_séparé = [x.upper() for x in Mot]
    
def dessin_mot():                   #Dessine les traits du mots qu'il faudra deviner
    global List_dash
    dessin = tk.Frame(jeu, bg = "LightGoldenrod2", width = 550, height = 100, highlightbackground= 'midnightblue', bd= 10, relief = 'raised')
    dessin.pack(pady=30, anchor = 'center')
    List_dash = tk.Label(jeu, text = ' '.join(["_" if letter!= ' ' else ' ' for letter in Mot]), font = ('helvetica', 50), fg = 'black', bg ='LightGoldenrod2')
    List_dash.place(in_=dessin, relx =0.5, rely = 0.5, anchor = 'center')

def clavier_lettres():          #construit un clavier contenant des boutons pour chacune des 26 lettres de l'alphabet 
    global alphabet, buttons
    clavier = tk.Frame(jeu, bg="#282828", bd = 2, relief = 'sunken')
    clavier.pack(pady = 0, anchor = 'center')
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    buttons = []
    for letter in alphabet:
            button = tk.Button(clavier, text=letter, font=("Helvetica", 18), bg="#333333", command = lambda letter = letter: lettre_check(letter), width=3, height=1 ,relief = 'raised')
            buttons.append(button)
    for i in range(12):
        buttons[i].grid(row = 0, column = i)
    for i in range(8):
        buttons[12+i].grid(row = 1, column = i+2)
    for i in range(6):
        buttons[20+i].grid(row = 2, column = i+3)

def clavier_ordi(event):                     #vérifie si la lettre tapée sur l'ordinateur est bien dans le mot
    if event.char.upper() in alphabet:
        lettre_check(event.char.upper())

#étapes du dessin du pendu
def etape1():                           #Dessin de la potence

        dessin_pendu.create_line((80,360),(320,360), fill = 'black', width = 5)
        dessin_pendu.create_line((120,360),(120,40),(240,40),(240,72), fill = 'black', width = 5)
        dessin_pendu.create_line((120,80),(152,40), fill = 'black', width = 5)

def etape2():                           #Dessin de la tête

        dessin_pendu.create_oval((208,72),(272,136), outline = 'black', width = 5)

def etape3():                           #Dessin du corps

        dessin_pendu.create_line((240,136),(240,256), fill = 'black', width = 5)

def etape4():                           #Dessin de la main gauche

        dessin_pendu.create_line((240,184),(192,144), fill = 'black', width = 5)

def etape5():                           #Dessin de la main droite

        dessin_pendu.create_line((240,184),(288,144), fill = 'black', width = 5)

def etape6():                           #Dessin du pied gauche

        dessin_pendu.create_line((240,254),(200,296), fill = 'black', width = 5)

def etape7():                           #Dessin du pied droit

        dessin_pendu.create_line((240,254),(280,296), fill = 'black', width  = 5)

def etape8():                           #Dessin du visage du pendu

        dessin_pendu.create_oval((224, 92),(232,100), fill = 'black', width = 2)
        dessin_pendu.create_oval((248,92),(256, 100), fill = 'black', width = 2)
        dessin_pendu.create_line((222, 124),(240,112),(259,124), fill = 'black', width = 5)

def lettre_check(lettre):             #Fonction qui vérifie si la lettre choisie appartient au mot
    global nouveau, guesses
    guesses += 1
    if lettre in Mot_séparé:
        right_guesses.remove(lettre)
        affichage_lettre(lettre)
        buttons[alphabet.index(lettre)].config(relief= 'sunken', bg="#93C572", state="disabled")
        victoire()
    else:
        affichage_pendu()
        buttons[alphabet.index(lettre)].config(relief= 'sunken', bg="#FF5252", state="disabled")
        défaite()
        
def affichage_lettre(lettre):            #Fonction qui affiche une lettre correctement choisie
    global nouveau_texte
    for i in range(len(Mot_séparé)):   
        if Mot_séparé[i] == lettre:
            nouveau_texte = List_dash.cget('text')[:2*i]+ lettre + List_dash.cget('text')[2*i+1:]
            List_dash.config(text = nouveau_texte)

def affichage_pendu():                 #Fonction qui affiche les membres du pendu
    global wrong_guesses, Etapes
    Etapes = [etape1, etape2, etape3, etape4, etape5, etape6, etape7, etape8]
    Etapes[wrong_guesses]()
    wrong_guesses +=1

def défaite():                          #Fonction qui affiche un message lorsque le joueur a perdu et lui demande s'il veut rejouer
   if wrong_guesses == len(Etapes):
        resultat = messagebox.askquestion("Défaite", "Vous avez perdu! Le bon mot était " + Mot.upper() + ".\nSouhaitez-vous rejouer?")
        if resultat == messagebox.YES:
             nouvelle_partie()
        else:
             racine.destroy()

def victoire():                         #Fonction qui affiche un message de victoire au joueur et lui demande s'il veut rejouer
    if right_guesses == []:
        resultat = messagebox.askquestion("Victoire", "Bien Joué, vous avez trouvé le mot et sauvé le pendu!\nSouhaitez-vous rejouer?")
        if resultat == messagebox.YES:
             nouvelle_partie()
        else:
             racine.destroy()

menu_principal()
racine.mainloop()

