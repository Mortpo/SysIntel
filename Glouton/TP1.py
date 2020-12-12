import random

LIBRE = 0
REINE = 1
MENACEE =2

class Cellule:

    # constructeur Cellule
    def __init__(self, x:int ,y:int):
        # définition des coordonées de la Cellule
        self.x = x
        self.y = y
        # état de base de la Cellule = LIBRE
        self.typeOccupation = LIBRE
        

    # getters
    def getX(self):
        return self.x




    def getY(self):
        return self.y
    
    def getTypeOccupation(self):
        return self.typeOccupation

    # setters
    def setTypeOccupation(self, occupation):
        self.typeOccupation = occupation
    
    


class Reine:

    # constructeur
    def __init__(self, x, y,menace):
        #attributs
        self.x = x
        self.y = y
        self.nbMenace = menace

    # getters
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getnbMenace(self):
        return self.nbMenace


    # setters
    def setnbMenace(self, menace):
        self.nbMenace = menace
    def setX(self, nouveauX):
        self.x = nouveauX
    def setY(self, nouveauY):
        self.y = nouveauY

    # surcharge de __repr__
    def __str__(self):
        return " x: "+str(self.x)+", y: "+str(self.y)


class Echiquier:

        # méthode -> instanciation d'une cellule dans chaque case
        def intialiserEchiquier(self):
            for x in range(self.taille):
                for y in range(self.taille):
                    self.echiquier[x][y] = Cellule(x,y)
    
        # constructeur Echiquier
        def __init__(self,taille):
            # définition de ses attributs -> sa taille et un tableau d'entier
            self.taille = taille
            self.echiquier = [[0 for x in range(taille)] for y in range(taille)]
            # attributs suplémentaires pour la suite
            self.nbrCellulelibre = self.taille**2
            # initialisation
            self.intialiserEchiquier()
        
        # méthode -> modifier type d'occupation d'une Cellule
        def modifierCellule(self, x, y, valeur):
            self.echiquier[x][y].setTypeOccupation(valeur)

        # méthode -> placer une Reine sur l'échiquier
        def placerReine(self,x,y):
            # si la case ciblée ok ? 
            if 0 <= x < self.taille and 0 <= y < self.taille and self.echiquier[x][y].typeOccupation == LIBRE :
                for X in range(self.taille):
                    # passe la ligne en menacée
                    self.modifierCellule(X,y,MENACEE)
                    self.modifierCellule(x,X,MENACEE)# passe la colonne en menacée
                    # passe la diagonale droite en menacée
                    diagDroite = (self.taille-X) + ((x+y)-self.taille)
                    if diagDroite < self.taille and diagDroite >= 0:
                        self.modifierCellule(X,diagDroite,MENACEE)
                    # passe la diagonale gauche en menacée
                    diagGauche =  X + (y-x)
                    if diagGauche < self.taille and diagGauche >= 0:
                        self.modifierCellule(X,diagGauche,MENACEE)
                
                    
                # place la reine pour finir
                self.modifierCellule(x,y,REINE)
            # sinon erreur
            else:
                print("Erreur de positionnement")

        # méthode -> affiche l'échiquier
        def toString(self):
            print("")
            symbole = " "
            for y in range(self.taille):
                # forme le "toît" de chaque ligne
                for x in range(self.taille):
                    print("____", end ='')
                print("")
                # affiche les cases d'une ligne
                for x in range(self.taille):
                    # si la case est libre -> " "
                    if self.echiquier[x][y].typeOccupation == 0:
                        symbole = "  "
                    # sinon si la case est occupée par une reine -> "R"
                    elif self.echiquier[x][y].typeOccupation == 1:
                        symbole = "R "
                    # sinon la case est menacée -> "x"
                    else:
                        symbole = "x "
                    print("|", symbole, end = '')
                print("|")
            # ferme l'échiquier par le bas
            for x in range(self.taille):
                print("____", end ='')
            print("")

        # méthode --> donne le nombre de cellule prises par le coup (menacée+reine)
        def estimeCoup(self, x, y):
            compteur = 1
            for X in range(self.taille):
                # compter sur la ligne
                if self.echiquier[X][y].getTypeOccupation() == LIBRE and X != x:
                    compteur += 1
                # compter sur la diagonale droite
                diagDroite = (self.taille-X) + ((x+y)-self.taille)
                if diagDroite < self.taille and X != x and diagDroite >= 0 and self.echiquier[X][diagDroite].getTypeOccupation() == LIBRE:
                    compteur += 1
                # compter sur la diagonale gauche
                diagGauche =  X + (y-x)
                if diagGauche < self.taille and diagGauche >= 0 and X != x and self.echiquier[X][diagGauche].getTypeOccupation() == LIBRE:
                    compteur += 1 
            # passe la colonne en menacée
                if self.echiquier[x][X].getTypeOccupation() == LIBRE and X != y:
                    compteur += 1                              

            return compteur

        # méthode -> jouer le meilleur coup
        def jouerAvecLeMeilleurCoup(self):
            while self.nbrCellulelibre > 0:
                estimation=0
                meilleurCoup = 1001
                for Y in range(self.taille):
                    for X in range(self.taille):
                        if self.echiquier[X][Y].getTypeOccupation() == LIBRE :
                            estimation = self.estimeCoup(X,Y)
                            if estimation < meilleurCoup:
                                meilleurCoup = estimation
                                meilleur_x = X
                                meilleur_y = Y
                            
                self.placerReine(meilleur_x, meilleur_y)
                self.nbrCellulelibre -= meilleurCoup               
                self.toString()
            self.toStringReine()

        def coupAvance(self):
            while self.nbrCellulelibre > 0:
                tableauCoup = []
                tableauCoup.clear()
                sommeMenace=0
                for Y in range(self.taille):
                    for X in range(self.taille):
                        if self.echiquier[X][Y].typeOccupation == LIBRE:
                            
                            estimation=self.estimeCoup(X,Y)
                            tableauCoup.append(Reine(X,Y,estimation))
                            sommeMenace+=estimation

                moyenneMenace = sommeMenace/len(tableauCoup)
    
                place=True
                while place:
                    estimation=tableauCoup[int(random.uniform(0, len(tableauCoup)))]
                    if estimation.getnbMenace()<=moyenneMenace :
                        self.nbrCellulelibre -= estimation.getnbMenace()
                        self.placerReine(estimation.getX(), estimation.getY())
                        place=False
            return self.getNormalPresentation()

        # méthode -> liste reine
        def toStringReine(self):
            listeReine = self.getNormalPresentation()
            print("\nNombre de reine : "+str(len(listeReine)))
            for i in range(len(listeReine)):
                print( "numero de reine  "+ str((i+1)) + str(listeReine[i]))

        def getNormalPresentation(self):
            presentation=[]
            
            for Y in range(self.taille):
                for X in range(self.taille):
                    if self.echiquier[X][Y].typeOccupation == REINE:
                            presentation.append(Reine(X,Y,0))
                            
            return presentation

        def getUniqueKey(self, tableaudereine): #générateur de clée "unique"
            somme=""
            for i in range(len(tableaudereine)):
                somme+= str(tableaudereine[i].getX())+str(tableaudereine[i].getY())
            return int(somme)

        def printResult(self):
            self.toString()
            self.toStringReine()
            


# fonction main
def mainnonglouton(sol:int):
    solution = 0
    solutionUnique=[]
    nonuniquecompteur=0 # sécurité
    
    while solution < 92 and nonuniquecompteur<300 and solution < sol :
        unique=True
        test = Echiquier(8)
        resultat=test.coupAvance()
        if len(resultat)==8 :
            i=0
            keyresult=test.getUniqueKey(resultat)
            while (i < len(solutionUnique) and unique == True ) :
                
                    if keyresult == solutionUnique[i] :
                        unique=False
                        nonuniquecompteur+=1
                        print("non unique") 
                    i+=1
            if unique==True:
                solutionUnique.append(keyresult)
                print("\n"+"\n"+ "Solution n°"+str(solution+1))
                test.printResult()
                solution+=1
                nonuniquecompteur=0
    print("\n\nSolution.s unique.s : " + str(len(solutionUnique)))

def mainglouton(): #algoglouton

    test = Echiquier(8)
    test.jouerAvecLeMeilleurCoup()
    test.printResult()


# début du code
mainnonglouton(1000)
#il faut choisir entre mainglouton et mainnonglouton
#Python nomprog.py > resultat.txt