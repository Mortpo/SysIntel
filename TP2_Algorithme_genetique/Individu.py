from random import *


class Individu:

    # constructeur deux en un
    # --> donner un int pour le nombre de genes voulu et il seront generé aléatoiremnt
    # --> donner une liste pour donner à votre individu une liste de genes déjà définie
    def __init__(self, arg1):
        # si on nous donne un nombre de gene
        if type(arg1) == int:
            # nombre de genes de l'indivu
            self.nbrGenes = arg1
            # liste de ses genes
            self.listeGenes = []
            # on remplit cette liste avec du pseudo aléatoire
            for i in range(0, arg1):
                self.listeGenes.append(randint(0, 1))
            # score de fitness de l'individu
        # si on donne une liste de gene prédéfinie
        else:
            self.nbrGenes = len(arg1)
            self.listeGenes = arg1
        self.fitness = self.calculeFitness2()

    # getters
    def getNbrGenes(self):
        return self.nbrGenes

    def getGene(self, indexGene):
        return self.listeGenes[indexGene]

    def getListeGenes(self):
        return self.listeGenes

    def getFitness(self):
        return self.fitness

    # méthode qui calcule la valeur de fitness d'un individu
    # /!\ jai voulu concerver la lecture de droite a gauche comme en vrai
    # cad que le bit de poids faible est a la fin de la liste et le poids fort à l'indice 0
    def calculeFitness(self):
        fit = 0
        for i in range(0, self.nbrGenes):
            fit += (2 ** (self.nbrGenes - i - 1)) * self.listeGenes[i]
        return fit

    # deuxième version de la méthode du calcul de la valeur de fitness d'un individu
    def calculeFitness2(self):
        nbrDeUn = 0
        for i in range(0, self.nbrGenes):
            if self.listeGenes[i] == 1:
                nbrDeUn += 1
        return nbrDeUn

    # mutation, passer un bit de 0 à 1 ou l'inverse selon une certaine probabilité
    def mutation(self, chanceMutation):
        # on tire un nombre au hasard pour voir si la mutation aura lieu ou non
        aleatoire = randint(0, 99)
        # si c'est bon on mute
        if aleatoire < chanceMutation*100:
            # index du genes qui va muter
            index = randint(0, self.nbrGenes - 1)
            # si le gene est à 1 on le passe à 0
            if self.listeGenes[index] == 1:
                self.listeGenes[index] = 0
            # inversement
            else:
                self.listeGenes[index] = 1
            # attention si on mute alors la valeur de fitness change
            self.fitness = self.calculeFitness2()

    # to String
    def __str__(self):
        return "\t Fitness = " + str(self.fitness) + "\tGenes de l'individu: " + self.listeGenes.__str__() + "\n"
