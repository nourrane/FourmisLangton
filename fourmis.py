from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from unittest.mock import mock_open
#[h,g,b,d]  
#[1,2,3,4]

#case noir fourmis=pion_b
def MooveAnt():
    "Déplacement de la fourmis"
    global ant, case_n, directant
    print("-----")
    print("fourmis sur case noire: ",ant in case_n)
    print("direction fourmie: ",directant)
    if (ant in case_n):
        removecase_n()
        if directant==1:
            directant=2
            ant-=1
        elif directant==4:
            directant=1
            ant-=t
        elif directant==3:
            directant=4
            ant+=1
        else:
            directant=3
            ant+=t
    else:
        #[h,g,b,d]  
        #[1,2,3,4]
        case_n.append(ant)
        if directant==1:
            directant=4
            ant+=1
        elif directant==4:
            directant=3
            ant+=t
        elif directant==3:
            directant=2
            ant-=1
        else:
            directant=1
            ant-=t
    print("-->",directant)
    print(case_n)
    draw()
    positionAnt()

def removecase_n():
    global ant, case_n
    del case_n[case_n.index(ant)]
    x = ((ant%t))   
    y = (ant//t)
    can1.create_rectangle(x*case, y*case, (x*case)+case, (y*case)+case, fill='dark grey')

def draw():
    "On place les pions"
    global case_n, ant
    print("draw:", case_n)
    for rec in case_n:
        if rec != -1:
            x = ((rec%t))   #abscisse des pions rouges
            y = (rec//t)
            can1.create_rectangle(x*case, y*case, (x*case)+case, (y*case)+case, fill='black')




def positionAnt(): #emplacement de la fourmis
        global ant,t
        y = ((ant//t)*case) + case/2
        x = ((ant%t)*case) + case/2
        can1.create_oval(x-15, y-15, x+15, y+15, fill='orange')


#_____Création de l'interface reunnissant le damier et les pions_______
def interface():
    "Dessine la GUI"
    global fenetre, can1,bt2, chaine, txt1, ant, selected, directant,t

    #----création de la fenetre----
    fenetre = Tk()
    fenetre.title("Fourmis de Langton")
    #----création de la surface graphique----
    can1 = Canvas(fenetre, width=case*t, height=case*t, bg='dark grey')
    can1.pack(side=TOP)
    #----creation de zone de texte----
    chaine = Label(fenetre)
    chaine.configure(text="", fg='red')
    chaine.pack()
    txt1 = Label(fenetre, text='')
    txt1.pack()
    bt2 = Button(fenetre, text='Nouvelle Partie', command=MooveAnt)
    bt2.pack(side=RIGHT)
    positionAnt()
    fenetre.mainloop()


#--- Programme principal ---
t=10
selected=1
directant=1
ant = t*(t+1)/2
case = 40
case_n = []
interface()

