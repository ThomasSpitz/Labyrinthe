from pileNonBornee import *

#Exercice 1

def dixentiernaturel():
    p=Pile(None)
    for i in range(10):
        p.empile(i)
    return p

#Exercice 2

def hauteur(p):
    c=0
    while not p.est_vide():
        p.depile()
        c+=1
    return c

##p=dixentiernaturel()
##print(hauteur(p))
##print(p)
#Il faudrait faire une copie de la pile !!!

#Exercice 3

def copie(p):
    p1=Pile(None)
    while not p.est_vide():
        e=p.sommet()
        p.depile()
        p1.empile(e)

    p2=Pile(None)
    while not p1.est_vide():
        e=p1.sommet()
        p1.depile()
        p2.empile(e)
        p.empile(e)
    return p2

#Exercice 4

def hauteur2(p):
    pcopie=copie(p)
    c=0
    while not pcopie.est_vide():
        pcopie.depile()
        c+=1
    return c

#Exercice 5

def inverse(p):
    pcopie=copie(p)
    p1=Pile(None)
    while not pcopie.est_vide():
        e=pcopie.sommet()
        pcopie.depile()
        p1.empile(e)
    return p1

#Exercice 6

def superpose(p1,p2):
    p1copie=copie(p1)
    p2copie=inverse(p2)
    while not p2copie.est_vide():
        e=p2copie.sommet()
        p2copie.depile()
        p1copie.empile(e)
    return p1copie

#Exercice 7

def insere(x,p):
    p1=copie(p)
    p2=Pile(None)
    pmax=p1.sommet()
    while x<pmax and not p1.est_vide():
        p2.empile(pmax)
        p1.depile()
        pmax=p1.sommet()
        
    p1.empile(x)
    p1=superpose(p1,inverse(p2))
    return p1

#Exercice 8

def triInsertionPile(p):
    pcopie=copie(p)
    ptri=Pile(None)
    ptri.empile(pcopie.sommet())
    pcopie.depile()
    while not pcopie.est_vide():
        ptri=insere(pcopie.sommet(),ptri)
        pcopie.depile()
    return ptri


#Exercice 9

def permute(p,n):
    pcopie=copie(p)
    p2=Pile(None)
    e=pcopie.sommet()
    pcopie.depile()
    for i in range(n-1):
        p2.empile(pcopie.sommet())
        pcopie.depile()
    pcopie.empile(e)
    return superpose(pcopie,inverse(p2))
        

#Exercice 10

def bonParenthesage(s):
    ouvrante=['(','[','{','<']
    fermante=[')',']','}','>']
    p=Pile(None)
    for i in range(len(s)):
        for j in range(len(ouvrante)):
            
            if s[i]==ouvrante[j]:
                p.empile(s[i])
            elif s[i]==fermante[j]:
                if p.sommet()!=ouvrante[j]:
                    return False
                else:
                    p.depile()
    return True

#Exercice 11

def calculatrice():
    p=Pile(None)
    while True:
        saisie=input('Saisir un entier, une opération ou une commande : ')
        if saisie=='+':
            a=p.sommet()
            p.depile()
            b=p.sommet()
            p.depile()
            p.empile(a+b)
            print(p)
        elif saisie=='-':
            a=p.sommet()
            p.depile()
            b=p.sommet()
            p.depile()
            p.empile(b-a)
            print(p)
        elif saisie=='x':
            a=p.sommet()
            p.depile()
            b=p.sommet()
            p.depile()
            p.empile(b*a)
            print(p)
        elif saisie=='/':
            a=p.sommet()
            p.depile()
            b=p.sommet()
            p.depile()
            p.empile(b/a)
            print(p)
        elif saisie=='q':
            break
        elif saisie=='p':
            print(p)
        else:
            p.empile(int(saisie))
            

