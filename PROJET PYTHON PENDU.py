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
    title = tk.Label(menu, text = 'le Jeu du Pendu', font = 'jokerman 60 bold italic', bg = "#282828")
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
    combo_themes.bind("<<ComboboxSelected>>",  sélection)

def extraction_des_longueurs():       #fonction qui permet d'extraire toutes les longueurs de mots possibles pour un thème donné
    global longueur_des_mots   
    longueur_des_mots = []                           
    mots_du_theme = list(themes.values())
    for i in mots_du_theme:
            for j in i:
                    longueur_des_mots.append(len(j))
    longueur_des_mots = list(set(longueur_des_mots))
    longueur_des_mots.sort()
    
def liste_de_longueurs():       #fonction qui permet à l'utilisateur de choisir la longueur du mot à deviner
    choisir_long_mot = tk.Label(menu, text = 'Choisir la longueur du mot:', font = 'helvetica 20 italic', fg = 'white', bg ="#282828")
    choisir_long_mot.pack(pady = 10)
    extraction_des_longueurs()
    combo_long = ttk.Combobox(menu, width = 20, state="readonly")
    combo_long['values'] = list(longueur_des_mots)
    combo_long.current(0)
    combo_long.pack(pady = 10)
    combo_long.bind("<<ComboboxSelected>>",  sélection)

def sélection(event, var):       #fonction qui permet de retourner la valeur des listes choisies par l'utilisateur
    event.widget.get()

def transition():       #transition vers le jeu principal
    global jeu
    menu.destroy()
    jeu = tk.Frame(racine, bg="#282828")
    jeu.pack(pady=30)
    cadre_pendu()

def cadre_pendu():          #crée le cadre dans lequel se formera le pendu
    global dessin_pendu
    dessin_pendu = tk.Canvas(jeu, bg ='white', width = 400, height = 400)
    dessin_pendu.pack(side ="top", fill='y', expand = True)

def mot_caché():        #génère le mot aléatoire qu'il faudra deviner
    theme_selec = theme_options.get() 
    Mot = rd.choice(themes[theme_selec])     #Choix du mot à deviner au hasard
    Mot_séparé = [x for x in Mot]        
    List_dash = []
    guesses = set(Mot_séparé.copy())
menu_principal()
racine.mainloop()


































