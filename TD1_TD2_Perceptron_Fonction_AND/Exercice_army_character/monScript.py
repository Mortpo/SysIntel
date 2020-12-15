if __name__ == "__main__":

    from army import *
    from character import *
    import csv
    from random import *


    # création des listes de personnage et armée
    characters_list = []
    armee_list = []

    # lecture du fichier et instanciation des personnages
    with open('characters.csv', newline='') as fichierCSV:
        # instanciation du reader
        reader = csv.reader(fichierCSV)
        # pour chaque ligne du csv on instancie un personnage et une armée associée (sauf la première ligne)
        compteur = 0
        for ligne in reader:
            if compteur > 0:
                characters_list.append(Character(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4]))
                armee_list.append(Army(characters_list[compteur-1], uniform(20.0, 100.0)))
            compteur += 1

    # afficher le contenu tous les personnages
    for i in characters_list:
        print(i)

    # afficher les amrées
    for i in armee_list:
        print(i)

    # calcul de la valeur totale de moral de toutes les armées
    total = 0
    for armee in armee_list:
        total += armee.get_total_morale()
    print("Valeur totale de moral de toutes les armées: ", total)
