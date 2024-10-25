import random as rd
from pileNonBornee import *
from tpPiles import *
import matplotlib.pyplot as plt

class Case:
    def __init__(self):
        self.N=False
        self.S=False
        self.E=False
        self.W=False
        self.etat=False

class Labyrinthe:
    def __init__(self,minit,ninit):
        self.n=ninit
        self.m=minit
        self.tab=[[Case() for i in range(self.n)]for j in range(self.m)]

    def show(self):
        X=[]
        Y=[]
        for m in range (len(self.tab)):
            X.append(None)
            Y.append(None)
            for n in range(len(self.tab[m])):
                X.append(None)
                Y.append(None)
                
                if self.tab[m][n].S==False and (m!=len(self.tab)-1 or n!=0):
                    X.append(m)
                    X.append(m+1)
                    Y.append(n)
                    Y.append(n)
                else:
                    X.append(None)
                    Y.append(None)

                if self.tab[m][n].E==False and (m!=len(self.tab)-1 or n!=0):
                    X.append(m+1)
                    X.append(m+1)
                    Y.append(n)
                    Y.append(n+1)
                else:
                    X.append(None)
                    Y.append(None)

                if self.tab[m][n].N==False and (m!=0 or n!=len(self.tab)-1):
                    X.append(m+1)
                    X.append(m)
                    Y.append(n+1)
                    Y.append(n+1)
                else:
                    X.append(None)
                    Y.append(None)

                if self.tab[m][n].W==False and (m!=0 or n!=len(self.tab)-1):
                    X.append(m)
                    X.append(m)
                    Y.append(n+1)
                    Y.append(n)
                else:
                    X.append(None)
                    Y.append(None)

        plt.plot(X,Y)
        plt.title('Labyrtinthe')
        plt.show()

    def solution(self):
        soluce=explorer(self)
        X2=[]
        Y2=[]
        for i in range(len(soluce)):
            X2.append(soluce[i][0]+0.5)
            Y2.append(soluce[i][1]+0.5)
        X=[]
        Y=[]
        for m in range (len(self.tab)):
            X.append(None)
            Y.append(None)
            for n in range(len(self.tab[m])):
                X.append(None)
                Y.append(None)
                if self.tab[m][n].S==False and (m!=len(self.tab)-1 or n!=0):
                    X.append(m)
                    X.append(m+1)
                    Y.append(n)
                    Y.append(n)
                else:
                    X.append(None)
                    Y.append(None)

                if self.tab[m][n].E==False and (m!=len(self.tab)-1 or n!=0):
                    X.append(m+1)
                    X.append(m+1)
                    Y.append(n)
                    Y.append(n+1)
                else:
                    X.append(None)
                    Y.append(None)

                if self.tab[m][n].N==False and (m!=0 or n!=len(self.tab)-1):
                    X.append(m+1)
                    X.append(m)
                    Y.append(n+1)
                    Y.append(n+1)
                else:
                    X.append(None)
                    Y.append(None)

                if self.tab[m][n].W==False and (m!=0 or n!=len(self.tab)-1):
                    X.append(m)
                    X.append(m)
                    Y.append(n+1)
                    Y.append(n)
                else:
                    X.append(None)
                    Y.append(None)

        plt.plot(X,Y)
        plt.plot(X2,Y2,color='red')
        plt.title('Labyrtinthe')
        plt.show()


def creation(m,n):
    L=Labyrinthe(m,n)
    i=rd.randint(0,m-1)
    j=rd.randint(0,n-1)
    P=Pile(None)
    L.tab[i][j].etat=True
    P.empile((i,j))
    T=[]
    while not P.est_vide():

        x=P.sommet()[0]
        y=P.sommet()[1]
        if y<(n-1):

            if L.tab[x][y+1].etat==False:
                T.append('N')
        if y>0:

            if L.tab[x][y-1].etat==False:
                T.append('S')
        if x<(m-1):

            if L.tab[x+1][y].etat==False:
                T.append('E')
        if x>0:

            if L.tab[x-1][y].etat==False:
                T.append('W')

        if len(T)==1:
            P.depile()
        if len(T)>=1:
            drct=T[rd.randint(0,len(T)-1)]
            if drct=='N':
                L.tab[x][y+1].etat=True
                L.tab[x][y+1].S=True
                L.tab[x][y].N=True
                P.empile((x,y+1))
            elif drct=='S':
                L.tab[x][y-1].etat=True
                L.tab[x][y-1].N=True
                L.tab[x][y].S=True
                P.empile((x,y-1))
            elif drct=='E':
                L.tab[x+1][y].etat=True
                L.tab[x+1][y].W=True
                L.tab[x][y].E=True
                P.empile((x+1,y))
            elif drct=='W':
                L.tab[x-1][y].etat=True
                L.tab[x-1][y].E=True
                L.tab[x][y].W=True
                P.empile((x-1,y))

        else:
            P.depile()

        T=[]
    return L

def explorer(laby):
    P=Pile(None)
    n=laby.n
    m=laby.m
    laby.tab[0][n-1].etat=False
    P.empile((0,laby.n-1))
    while True:
        x=P.sommet()[0]
        y=P.sommet()[1]
        T=[]
        if (x,y)==(laby.m-1,0):
            Soluce=[]
            for i in range(hauteur2(P)):
                Soluce.append(P.sommet())
                P.depile()
            return Soluce

        if y>0:

            if laby.tab[x][y-1].etat==True and laby.tab[x][y].S==True:
                T.append('S')
        if x<(m-1):

            if laby.tab[x+1][y].etat==True and laby.tab[x][y].E==True:
                T.append('E')

        if y<(n-1):

            if laby.tab[x][y+1].etat==True and laby.tab[x][y].N==True:
                T.append('N')
        if x>0:

            if laby.tab[x-1][y].etat==True and laby.tab[x][y].W==True:
                T.append('W')

        if len(T)==0:
            P.depile()

        elif len(T)>=1:
            drct=T[0]
            if drct=='N':
                laby.tab[x][y+1].etat=False
                P.empile((x,y+1))
            elif drct=='S':
                laby.tab[x][y-1].etat=False
                P.empile((x,y-1))
            elif drct=='E':
                laby.tab[x+1][y].etat=False
                P.empile((x+1,y))
            elif drct=='W':
                laby.tab[x-1][y].etat=False
                P.empile((x-1,y))

        else:
            P.depile()
        T=[]

m = int(input("Entrer la largeur du labyrinthe : "))
n = int(input("Entrer la hauteur du labyrinthe : "))
l= creation(m,n)
while 1 :
    rep = input("Que voulez-vous faire ? (afficher:a,solution:s)")
    if rep == 'a' :
        l.show()
    elif rep == 's':
        l.solution()
