if __name__ == '__main__':
    from Perceptron import *

    # inputs possibles
    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]

    # sortie attendue
    sortiesAttendues = [0, 0, 0, 1]

    # instance de notre perceptron
    perceptron = Perceptron(4, 50, 0.1)

    # entrainement de notre perceptron
    perceptron.train(inputs, sortiesAttendues)