print("Classe army bien importee")


class Army:

    # constructeur
    def __init__(self, chef, valeurMoral):
        self.chef = chef
        self.valeurMoral = valeurMoral

    # getters
    def getChef(self):
        return self.chef

    def getValeurMoral(self):
        return self.valeurMoral

    # setters
    def setChef(self, nouveauChef):
        self.chef = nouveauChef

    def setValeurMoral(self, nouvelleValeurMoral):
        self.valeurMoral = nouvelleValeurMoral

    # surcharge de __repr__() -> déscription de l'objet
    def __repr__(self):
        return "Armée: chef= " + self.getChef().getPrenom() + ", valeur de moral de base= " + str(self.getValeurMoral())

    # méthode -> valeur de base de l'armée x le coef du chef
    def get_total_morale(self):
        temp = self.valeurMoral * self.getChef().getBoostDeMoral()
        return temp
