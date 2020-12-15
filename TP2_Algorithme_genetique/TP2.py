from Population import *

# taille de la population voulue
taillePopulation = 50
# nombre de genes voulu par individu
nbrGenes = 20
# crosstype à utiliser "roulette" et "tournoi"
crossType = "tournoi"
# % de chance pour un individu de muter à la naissance
chanceMutation = 0.05

# notre population
population = Population(taillePopulation, nbrGenes, crossType, chanceMutation)

# on affiche notre population
print("Population initiale:\n", population)

# compteur pour stopper notre boucle while
compteur = 0
# meilleure de fitness trouvée
meilleurFitness = 0
# variable temporaire pour eviter de retrouver le meilleur de la population plusieurs fois
temp = 0
# nombre d'epoch (nombre de generation qu'on genere)
epoch = 0
# on fait tourner notre programme tant que on se stabilise sur une valeure max 20 fois
while compteur < 20:
    # on genère une nouvelle population
    population.genererNouvelleGeneration()
    # on recupère la meilleure valeur de fitness de la population
    temp = population.getLeMeilleur()
    # si la meilleure valeur de fitness est la même que la dernière fois
    if temp == meilleurFitness:
        # on ajoute 1 a notre compteur pour arreter la boucle while
        compteur += 1
    # sinon cest qu'on a trouver une autre valeur (meilleure en théorie mais peut être aussi moins bonne)
    else:
        # notre meilleure fitness change
        meilleurFitness = temp
        # on recommence à 0
        compteur = 0
    epoch += 1

# on affiche notre population finale
print("Population finale :", population)

# conclusion
print("\n\n\nAprès ", epoch, " epochs, le plus grand nombre qu'on trouve possède ", meilleurFitness, "x1 (Max possible = ", nbrGenes, " )")
