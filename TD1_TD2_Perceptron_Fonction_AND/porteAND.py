import numpy as np
import matplotlib.pyplot as plt

# inputs possibles
input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# sortie attendue
t = np.array([0, 0, 0, 1])

# tableau a deux dimension pour avoir l'erreur en fonction de w1 et w2
surfaceDerreur = np.zeros((11, 11))

# erreur totale sur le couple de poids
erreurTotale = 0
# la prédiction
y = 0

# pour chaque combinaison de poids
for w1 in range(-5, 6):
    for w2 in range(-5, 6):
        erreurTotale = 0
        # on calcule pour chaque couple d'entrée
        for compteur in range(4):
            y = input[compteur][0] * w1 + input[compteur][1] * w2
            if y <= 0:
                y = 0
            else:
                y = 1
            # la valeur d'érreur associées
            erreurTotale += 0.5 * ((y - t[compteur]) ** 2)
        # Après avoir passé les 4 inputs pour le couple w1t w2
        # on sauvegarde dans notre tab la valeur d'erreur totale pour cr couple
        surfaceDerreur[w1+5][w2+5] = erreurTotale

plt.imshow(surfaceDerreur)
plt.show()

