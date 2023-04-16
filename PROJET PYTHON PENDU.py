import tkinter as tk
import random as rd
from tkinter import ttk
from tkinter import messagebox

# création d'une liste de mots à deviner

themes   =    {'Animaux': ['chien', 'chat', 'lion', 'tigre', 'éléphant'],
               'Fruits': ['pomme', 'banane', 'orange', 'kiwi', 'mangue'],
               'Couleurs': ['rouge', 'bleu', 'vert', 'jaune', 'violet']}

dict_accents =  {           #dictionnaire des lettres avec accents les plus courantes en francais 
        'à': 'a',
        'â': 'a',
        'ä': 'a',
        'ç': 'c',
        'é': 'e',
        'è': 'e',
        'ê': 'e',
        'ë': 'e',
        'î': 'i',
        'ï': 'i',
        'ô': 'o',
        'ö': 'o',
        'ù': 'u',
        'û': 'u',
        'ü': 'u',
    }
#Création et caractérisation de la racine de l'inte
racine = tk.Tk()
racine.title("PENDU")
racine.attributes('-fullscreen', True)
racine.update()
WIDTH = racine.winfo_width()
HEIGHT = racine.winfo_height()
racine.config(bg = "#282828")
menu = tk.Frame(racine, bg="#282828")       #écran du menu principal

def menu_principal():      #création de l'écran principal du jeu
    global texte_instructions, theme_et_long
    menu.pack(pady = 30)
    title = tk.Label(menu, text='le Jeu du Pendu', font = 'jokerman 60 bold italic', bg = "#F3E5AB")
    title.pack(pady = 20, ipadx = WIDTH/2)
    lire_les_regles()
    texte_instructions = tk.Label(menu, width = WIDTH, height = 6, bd =4, relief = 'raised', bg = 'black', text = texte, font= 'Monolisa, 10', fg = 'red')
    texte_instructions.pack(pady = 5, ipady = 5)
    choix_mode()
    theme_et_long = tk.Frame(menu, width = WIDTH, height = 150, bg = "#282828")
    theme_et_long.pack(pady = 50)
    jouer_quitter()

def lire_les_regles():          #fonction permettant de lire et d'afficher les règles du jeu 
    global texte
    règles = open('C:/PROJET PYTHON PENDU/PROJET-S2-PENDU/instructions.txt', 'r',  encoding='utf-8')
    ligne = règles.readline()
    texte = ''
    while (ligne.strip() != ''):
        texte += ligne 
        ligne = règles.readline()
    règles.close()
    return texte

def choix_mode():           #toute l'interface concernant les modes dans le menu
    global modes
    bande_de_modes = tk.Frame(menu, width = WIDTH, height = 100, bg = "#282828") 
    bande_de_modes.pack(pady = 10)
    choisir_mode = tk.Label(bande_de_modes, text = 'Choisir un mode :', font = 'times 30 italic', fg = 'white', bg = "#282828")
    choisir_mode.place(anchor = 'w', relx = 0.03, rely = 0.5)
    mode_normal = tk.Button(bande_de_modes, text = 'Normal', font = 'helvetica 20 bold', bg = "#F3E5AB",  command = lambda: instructions_mode(mode_normal))
    mode_normal.place(relx = 0.4, rely = 0.5, anchor= 'center')
    mode_chrono = tk.Button(bande_de_modes, text = 'Chrono', font = 'helvetica 20 bold', bg = "#F3E5AB", command = lambda: instructions_mode(mode_chrono))
    mode_chrono.place(relx = 0.6, rely = 0.5, anchor= 'center')
    mode_infini = tk.Button(bande_de_modes, text = 'Infini', font = 'helvetica 20 bold', bg = "#F3E5AB", command = lambda: instructions_mode(mode_infini))
    mode_infini.place(relx = 0.8, rely = 0.5, anchor= 'center')
    modes = [mode_chrono, mode_infini, mode_normal]

def chrono():               #création du chronomètre
    global temps, texte_tps
    temps = 120
    texte_tps = tk.StringVar()
    texte_tps.set("02:00")
    cercle = tk.Canvas(jeu, width=255, height=255, bg="#282828", bd=0, highlightthickness=0)
    cercle.place(relx = 0.17, rely = 0.3, anchor= 'center')
    cercle.create_oval((10, 10),(250, 250), outline="#F5A623", width=10)
    tps = tk.Label(cercle, textvariable=texte_tps, font=("Arial", 75, "bold"), bg="#282828", fg="#F5A623")
    tps.place(relx=0.5, rely=0.5, anchor="center")

def passage_temps():        #passage du temps au chrono
    global temps, score
    temps -= 1
    minutes, seconds = temps//60, temps%60
    texte_tps.set(f"{minutes:02d}:{seconds:02d}")
    if temps == 0:
        resultat = messagebox.askquestion("le temps est écoulé!, Vous avez réussi à sauver le pendu" + str(score) + "fois!\nSouhaitez-vous rejouer?")
        if resultat == messagebox.YES:
            particularités_mode()
        else:
             racine.destroy()
        
    else:
        racine.after(1000, passage_temps)

def jouer_quitter():       #toute l'interface concernant les boutons jouer et quitter dans le menu
    play_exit = tk.Frame(menu , width = WIDTH, height = 100, bg = "#282828")
    play_exit.pack(pady = 5)
    play_button = tk.Button(play_exit, text="Commencer", font=("Helvetica", 20, "bold"), fg="white", bg="#4CAF50", command = transition)
    play_button.place(relx = 0.7, rely = 0.5, anchor = 'center')
    exit_button = tk.Button(play_exit, text="Quitter", font=("Helvetica", 20, "bold"), fg="white", bg="#F44336", command = racine.destroy)
    exit_button.place(relx = 0.3, rely = 0.5, anchor = 'center') 

def instructions_mode(button):      #fonction qui permet de lire et d'afficher les instructions en relation avec chaque mode
  global instr_mode, mode
  button.config(relief = 'sunken')
  for boutton in modes:
    if boutton != button:
      boutton.config(relief = 'raised')
      for widget in theme_et_long.winfo_children():
        widget.place_forget()
  mode = button['text']
  instr_mode = ''
  règles = open('C:/PROJET PYTHON PENDU/PROJET-S2-PENDU/instructions.txt', 'r',  encoding='utf-8')
  lignes = règles.readline()
  while lignes.strip() != mode:
    lignes = règles.readline()
  lignes = règles.readline()
  while lignes.strip() != '':
    instr_mode += lignes
    lignes = règles.readline()
  règles.close()
  paramètres_modes()
  texte_instructions.config(text = instr_mode)

def affich_combo():         #fonction qui affiche les paramètres du mode normal
  choisir_theme.place(relx = 0.3, rely = 0.1, anchor = 'center')
  combo_themes.place(relx= 0.3, rely =0.4, anchor = 'center')
  choisir_long_mot.place(relx = 0.7, rely = 0.1, anchor= 'center')
  combo_long.place(relx = 0.7, rely =0.4, anchor='center')

def liste_de_themes():      #fonction qui permet à l'utilisateur de choisir le thème des mots à deviner
  global combo_themes, choisir_theme
  choisir_theme = tk.Label(theme_et_long, text = 'Choisir un thème de mot:', font = 'helvetica 20 italic', fg = 'white', bg ="#282828")
  theme_options = tk.StringVar()
  combo_themes = ttk.Combobox(theme_et_long, textvariable= theme_options, width = 20, state="readonly")                    
  combo_themes['values'] = list(themes.keys())
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
  global combo_long, choisir_long_mot
  choisir_long_mot = tk.Label(theme_et_long, text = 'Choisir la longueur du mot:', font = 'helvetica 20 italic', fg = 'white', bg ="#282828")    
  combo_long = ttk.Combobox(theme_et_long, width = 20, state="readonly")
  combo_long.bind("<<ComboboxSelected>>",  sélection_long)

def sélection_thème(event):     #fonction qui permet de retourner le thème de mots choisi par l'utilisateur
  global thème
  thème = combo_themes.get()
  extraction_des_longueurs()
  combo_long['values'] = list(longueur_des_mots)
  combo_long.current(0)
    
def sélection_long(event):       #fonction qui permet de retourner la longueur du mot choisi par l'utilisateur
  global longueur  
  longueur = combo_long.get()

def affich_combo_theme():         #fonction qui affiche le paramètre thème(pour les modes chrono et infini) 
    choisir_theme.place(relx = 0.5, rely = 0.1, anchor = 'center')
    combo_themes.place(relx= 0.5, rely =0.4, anchor = 'center')

def paramètres_modes():
    liste_de_themes()
    combo_themes.current(0)
    liste_de_longueurs()
    if mode == 'Normal':
        affich_combo()
    elif mode == 'Chrono':
        affich_combo_theme()
    else:
        affich_combo_theme()

def particularités_mot():
    if mode == 'Normal':
        mot_caché_Normal()
    else:
        mot_caché_Autres()            

#création de l'interface du jeu
    
def transition():       #transition vers le jeu principal
    global jeu, Etapes, txt_score, score
    menu.destroy()
    jeu = tk.Frame(racine, bg="#282828", width = WIDTH, height = HEIGHT)
    jeu.pack()
    Etapes = [etape1, etape2, etape3, etape4, etape5, etape6, etape7, etape8]
    txt_score = tk.StringVar()
    txt_score.set("00")
    label_score = tk.Label(jeu, text = 'Votre Score est:', font = 'helvetica,40', fg = 'black', bg = 'white')
    affichage_score = tk.Label(jeu, textvariable= txt_score, font = 'helvetica,26', fg = 'black')
    label_score.place(relx = 0.8, rely = 0.2, anchor='center')
    affichage_score.place(relx = 0.8, rely = 0.3, anchor='center')
    score = 0
    particularités_mot()
    cadre_pendu()
    dessin_mot()
    clavier_lettres()
    nouvelle_partie()
    jeu.focus_set()
    jeu.bind("<KeyPress>", clavier_ordi)
    particularités_mode()
         
def particularités_mode():
    if mode == 'Chrono':
        score = 0
        chrono()
        racine.after(1000,passage_temps)
    if mode == 'Infini':
        score = 0
           
def nouvelle_partie():          #permet de générer une nouvelle partie
    global guesses, wrong_guesses, right_guesses, alphabet_ordi
    dessin_pendu.delete('all')
    alphabet_ordi = alphabet.copy()
    wrong_guesses= 0
    guesses = 0
    score = 0
    particularités_mot()
    right_guesses = list(set(mot_séparé_normal))
    List_dash.config(text = ' '.join(["_" if letter!= ' ' else ' ' for letter in Mot]))
    for button in buttons:
        button.config(state = 'normal', relief = 'raised', bg = "#333333")
         
def cadre_pendu():          #crée le cadre dans lequel se formera le pendu
    global dessin_pendu
    dessin_pendu = tk.Canvas(jeu, bg ='white', width = 400, height = 400)
    dessin_pendu.place(relx = 0.5, rely = 0.3, anchor = 'center')

def mot_caché_Normal():        #génère le mot aléatoire qu'il faudra deviner
    global Mot, Mot_séparé
    Mot = ''
    while len(Mot) != int(longueur):
        Mot = rd.choice(themes[thème])
    Mot_séparé = [x.upper() for x in Mot]
    normalisation_mot()

def mot_caché_Autres():
    global Mot, Mot_séparé
    Mot = ''    
    Mot = rd.choice(themes[thème])
    Mot_séparé = [x.upper() for x in Mot]
    normalisation_mot()

def normalisation_mot():                #fonction qui permet de retirer tous les accents d'un mot pour faciliter la reconnaissance
    global mot_séparé_normal
    mot_séparé_normal = []
    for x in Mot_séparé:
        if x.lower() in dict_accents:
            mot_séparé_normal.append((dict_accents.get(x.lower())).upper())
        else:
            mot_séparé_normal.append(x.upper())

def dessin_mot():                   #Dessine les traits du mots qu'il faudra deviner
    global List_dash
    dessin = tk.Frame(jeu, bg = "LightGoldenrod2", width = 550, height = 100, highlightbackground= 'midnightblue', bd= 10, relief = 'raised')
    dessin.place(relx = 0.5, rely = 0.67, anchor = 'center')
    List_dash = tk.Label(jeu, text = ' '.join(["_" if letter!= ' ' else ' ' for letter in Mot]), font = ('helvetica', 50), fg = 'black', bg ='LightGoldenrod2')
    List_dash.place(in_=dessin, relx =0.5, rely = 0.5, anchor = 'center')

def clavier_lettres():          #construit un clavier contenant des boutons pour chacune des 26 lettres de l'alphabet 
    global alphabet, buttons, alphabet_ordi
    clavier = tk.Frame(jeu, bg="#282828", bd = 2, relief = 'sunken')
    clavier.place(relx = 0.5, rely = 0.88, anchor = 'center')
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alphabet_ordi = alphabet.copy()
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
    if event.char.upper() in alphabet_ordi:
        alphabet_ordi.remove(event.char.upper())
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
    if lettre in mot_séparé_normal:
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
    for i in range(len(mot_séparé_normal)):   
        if mot_séparé_normal[i] == lettre:
            nouveau_texte = List_dash.cget('text')[:2*i]+ Mot_séparé[i]+ List_dash.cget('text')[2*i+1:]
            List_dash.config(text = nouveau_texte)

def affichage_pendu():                 #Fonction qui affiche les membres du pendu
    global wrong_guesses, Etapes
    Etapes[wrong_guesses]()
    wrong_guesses +=1

def défaite():                          #Fonction qui affiche un message lorsque le joueur a perdu et lui demande s'il veut rejouer
   if mode == 'Normal':
        txt_score.set(f"{guesses:02d}")
   if wrong_guesses == len(Etapes):
        if mode =='Normal':
            resultat = messagebox.askquestion("Défaite", "Vous avez perdu! Le bon mot était " + Mot.upper() + ".\nSouhaitez-vous rejouer?")
            if resultat == messagebox.YES:
                nouvelle_partie()
            else:
                racine.destroy()
        elif mode =='Chrono':
            nouvelle_partie()
        elif mode =='Infini':
            resultat = messagebox.askquestion("Défaite", "Vous avez perdu! Vous avez deviner un total de " + str(score) + "mots.\nSouhaitez-vous rejouer?")
            if resultat == messagebox.YES:
                nouvelle_partie()
            else:
                racine.destroy()

def victoire():                         #Fonction qui affiche un message de victoire au joueur et lui demande s'il veut rejouer
    global score
    if mode == 'Normal':
        txt_score.set(f"{guesses:02d}")
    if right_guesses == []:
        if mode == 'Normal':
            score = 1
            resultat = messagebox.askquestion("Victoire", "Bien Joué, vous avez trouvé le mot et sauvé le pendu!\nSouhaitez-vous rejouer?")
            if resultat == messagebox.YES:
                nouvelle_partie()
            else:
                racine.destroy()
        else:
            score+=1
            txt_score.set(f"{score:02d}")
            nouvelle_partie()

menu_principal()
racine.mainloop()
