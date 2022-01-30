from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from unittest.mock import mock_open
import time
from matplotlib.pyplot import pause

def printDirection(x):
    "Aide au Debug: Affichage des directions"
    global direction
    if directant==0:
        print('haut',end=" ")
    elif directant==3:
        print('droite',end=" ")
    elif directant==2:
        print('bas',end=" ")
    else:
        print('gauche',end=" ")
    if x:
       print('-->',end=" ") 
    else:
        print(" ") 

def nextMoove(dir):
    "On déplace la fourmie (le rond orange)"
    global ant, directant
    if directant==0:
        ant-=dir
    elif directant==3:
        ant-=t*dir
    elif directant==2:
        ant+=dir
    else:
        ant+=t*dir

#case noir fourmis=pion_b
def StopMooveAnt():
    global pause
    if pause:
        pause=False
    else:
        pause=True

    
def MooveAnt():
    "Déplacement de la fourmie"
    global ant, case_n, directant, etapes
    #-- Etapes txt--
    txt1.configure(text=' Etape : '+str(etapes))
    etapes+=1
    
    #-- direction :--
    #   haut : 0  // bas : 2
    #   gauche : 1 // droite : 3 
    #printDirection(1)
    if (ant in case_n):
        removecase_n()
        nextMoove(1)
        directant=(directant+1)%4
    else:
        case_n.append(ant)
        nextMoove(-1)
        directant=(directant+3)%4
    #printDirection(0)
    draw()
    positionAnt()

def quickMooveAnt():
    "Permet de faire une animation rapide" #Non fini, en cours
    global pause, ant
    while (pause==False and (ant>-1 and ant<t*t)):
        MooveAnt()
        #time.sleep(0.005)
        

def removecase_n():
    "Change une case noire en une case blanche"
    global ant, case_n
    del case_n[case_n.index(ant)]
    x = ((ant%t))   
    y = (ant//t)
    can1.create_rectangle(x*case, y*case, (x*case)+case, (y*case)+case, fill='dark grey')

def draw():
    "On dessine le damier"
    global case_n, ant
    for rec in case_n:
        if rec != -1:
            #coordonées du point
            x = ((rec%t))   
            y = (rec//t)
            can1.create_rectangle(x*case, y*case, (x*case)+case, (y*case)+case, fill='black')




def positionAnt():
    "Emplacement de la fourmie"
    global ant,t
    y = ((ant//t)*case) + case/2
    x = ((ant%t)*case) + case/2
    rayon=case/3
    can1.create_oval(x-rayon, y-rayon, x+rayon, y+rayon, fill='orange')


#_____Création de l'interface reunnissant le damier et les pions_______
def interface():
    "Dessine la GUI"
    global fenetre, can1,bt1, bt2, bt3, chaine, txt1, ant, selected, directant,t
    #----création de la fenetre----
    fenetre = Tk()
    fenetre.title("Fourmie de Langton")
    #----création de la surface graphique----
    can1 = Canvas(fenetre, width=case*t, height=case*t, bg='dark grey')
    can1.pack(side=TOP)
    #----creation de zone de texte----
    chaine = Label(fenetre)
    chaine.configure(text="", fg='red')
    chaine.pack()
    txt1 = Label(fenetre, text='')
    txt1.pack()
    #----creation des boutons----
    bt1 = Button(fenetre, text='Vitesse rapide', command=quickMooveAnt)
    bt1.pack(side=LEFT)

    bt2 = Button(fenetre, text='Next', command=MooveAnt)
    bt2.pack(side=RIGHT)

    bt3 = Button(fenetre, text='Pause', command=StopMooveAnt)
    bt3.pack()

    positionAnt()
    fenetre.mainloop()


#--- Programme principal ---
pause =False
#--taille--
t=10
#--direction initiale de la fourmis--
directant=0
#--position initiale de la fourmis--
ant = t*(t+1)/2
#--nb de pixel d'un carré--
case = 40
#--liste de cases noires--
case_n = []
#--nombre d'étape--
etapes=1
#--appel de l'interface graphique--
interface()

