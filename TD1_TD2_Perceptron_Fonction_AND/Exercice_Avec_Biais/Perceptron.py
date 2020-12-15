import csv
import os

class Perceptron:

    # constructeur
    def __init__(self, nbrInputs, nbrEpochs, learningRate):
        # attributs
        self.nbrInputs = nbrInputs
        self.nbrEpochs = nbrEpochs
        self.learningRate = learningRate
        # valeur du biais
        self.biais = 1
        # poids du biais
        self.w0 = 0
        # poids
        self.w1 = 0
        self.w2 = 0

    def predict(self, input1, input2):
        # notre prédiction
        y = self.w1 * input1 + self.w2 * input2 + self.w0 * self.biais
        # règle du perceptron
        if y <= 0:
            y = 0
        else:
            y = 1
        return y

    def train(self, listeInputs, listeSortiesAttendues):
        # pour stocker nos poids dans un fichier csv
        # with open("Valeures_des_poids.csv", "w") as fichierCSV:
        # preciser newline='' permet de ne pas sauter de ligne entre nos écritures
        with open("Valeures_des_poids.csv", mode="w", newline='') as fichierCSV:
            # attention le delimiter est bien un ; si on veut des colonnes séparées sous excel 2016
            writer = csv.writer(fichierCSV, delimiter=";")
            writer.writerow(("W0", "W1", "W2"))
            # prédiction
            y = 0
            # autant de fois que d'époch
            for epoch in range(0, self.nbrEpochs):
                # pour chaque paire d'input
                for i in range(0, self.nbrInputs):
                    # faire une prédiction
                    y = self.predict(listeInputs[i][0], listeInputs[i][1])
                    # correction des poids avec la loi de Widrow-Hoff
                    self.w0 = self.w0 + self.learningRate * (listeSortiesAttendues[i] - y) * self.biais
                    self.w1 = self.w1 + self.learningRate * (listeSortiesAttendues[i] - y) * listeInputs[i][0]
                    self.w2 = self.w2 + self.learningRate * (listeSortiesAttendues[i] - y) * listeInputs[i][1]
                    writer.writerow((self.w0, self.w1, self.w2))
