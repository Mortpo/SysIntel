import numpy as np

boostDeMoralDesPersonnages = np.array([1, 2, 3, 4, 5])
moralDesArmees = np.random.uniform(20.0, 100.0, 5)
# on multiplit les valeurs de même indice avec *
# on obtient la somme des elements du tableau avec np.sum()
total = np.sum(boostDeMoralDesPersonnages * moralDesArmees)
print(total)

