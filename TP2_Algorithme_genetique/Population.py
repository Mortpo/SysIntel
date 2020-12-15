from Individu import *


class Population:

    # generer une population avec du pseudo-aléatoire
    def __init__(self, taillePop, nbrG, cross, chanceMut):
        # taille de la population
        self.taillePopulation = taillePop
        # nbr de gene pour chaque individu de la population
        self.nbrGenes = nbrG
        # crosstype a utiliser
        self.crossType = cross
        # chance pour un individu de muter à la naissance
        self.chanceMutation = chanceMut
        # tableau contenant nos individus
        self.listeIndividus = []
        # on le remplit
        for i in range(0, taillePop):
            self.listeIndividus.append(Individu(nbrG))

    # retourne un individu avec une selection par roulette biaisée
    def roulette(self):
        # on calcule la somme totale des valeurs de fitness des individus de la population
        somme = 0
        for individu in self.listeIndividus:
            somme += individu.getFitness()
        # on tire un nombre au hasard entre 0 et la somme (somme comprise)
        nbrAleatoire = randint(0, somme)
        # on regarde au fur et a mesure qu'on ajoute entre elles les valeur de fitness des individus
        # de la population (cumul), sur quel individu on s'arrête (index) quand on aura atteind le nbr
        # tiré au hasard plus haut
        cumul = 0
        index = 0
        while cumul+self.listeIndividus[index].getFitness() < nbrAleatoire:
            cumul += self.listeIndividus[index].getFitness()
            index += 1
        # on retourne l'individu concerné
        return self.listeIndividus[index]

    # selection par tournoi
    def tournoi(self):
        # liste des concurents
        concurents = []
        # on tire N concurents au hasard parmis notre population
        for i in range(0, int(self.taillePopulation/4)):
            concurents.append(self.listeIndividus[randint(0, self.taillePopulation-1)])
        # on trie le tableau par ordre croissant de valeur de fitness
        concurents = sorted(concurents, key=lambda concurents: concurents.fitness)
        # on renvoit le dernier individu des concurents, le meilleur
        return concurents[len(concurents)-1]

    # faire un croisement 1 point entre deux individus au point indiqué
    def croisement2parents(self, parent1, parent2, indexCoupure):
        # liste des genes des enfant
        genesEnfant1 = []
        genesEnfant2 = []
        # jusqu'au point de coupure on recopie les genes de P1 dans E1 et P2 dans E2
        for index in range(0, indexCoupure):
            genesEnfant1.append(parent1.getGene(index))
            genesEnfant2.append(parent2.getGene(index))
        # et ensuite switch et jusqu'a la fin on ajoute P1 dans E2 et P2 dans E1
        for index in range(indexCoupure, parent1.getNbrGenes()):
            genesEnfant1.append(parent2.getGene(index))
            genesEnfant2.append(parent1.getGene(index))
        # on instancit les enfants
        enfant1 = Individu(genesEnfant1)
        enfant2 = Individu(genesEnfant2)
        # on les faits muter selon une certaine probabilité
        enfant1.mutation(self.chanceMutation)
        enfant2.mutation(self.chanceMutation)
        # on retourne un tableau d'enfants
        return [enfant1, enfant2]

    # generer une nouvelle population
    def genererNouvelleGeneration(self):
        # les individus de notre nouvelle population
        nouveauxIndividus = []
        # les parents selectionés pour le croisement
        parent1 = None
        parent2 = None
        # on remplie la liste
        for i in range(0, int(self.taillePopulation/2)):
            # on en selectionne deux selon le type de selection voulue
            if self.crossType == "roulette":
                parent1 = self.roulette()
                parent2 = self.roulette()
            else:
                parent1 = self.tournoi()
                parent2 = self.tournoi()
            # on croise les deux parents pour obtenir nos enfants
            enfants = self.croisement2parents(parent1, parent2, randint(0, parent1.getNbrGenes()-1))
            # on ajoute les enfants à la nouvelle population
            nouveauxIndividus.append(enfants[0])
            nouveauxIndividus.append(enfants[1])
        # si le nombre d'individu est impaire il faut en rajouter un dernier enfant
        if self.taillePopulation%2 != 0:
            if self.crossType == "roulette":
                parent1 = self.roulette()
                parent2 = self.roulette()
            else:
                parent1 = self.tournoi()
                parent2 = self.tournoi()
            enfants = self.croisement2parents(parent1, parent2, parent1.getNbrGenes()-1)
            nouveauxIndividus.append(enfants[0])
        # on remplace les individus
        self.listeIndividus = nouveauxIndividus

    # retourne la valeur de fitness du meilleur individu de la population
    def getLeMeilleur(self):
        # meilleur fitness trouvé
        best = 0
        # on parcours tous les individus
        for individu in self.listeIndividus:
            # si la valeur de fitness de l'individu est meilleure que celle qu'on avait déjà
            if individu.getFitness() > best:
                best = individu.getFitness()
        # on retourne la meilleure valeur trouvé
        return best

    # toString
    def __str__(self):
        retour = "Taille: " + str(self.taillePopulation) + ", Nbr genes: " + str(
            self.nbrGenes) + ", CrossType: " + self.crossType + ", Chance Mutation: " + str(self.chanceMutation)+"\n"
        for individu in self.listeIndividus:
            retour += individu.__str__()
        return retour
