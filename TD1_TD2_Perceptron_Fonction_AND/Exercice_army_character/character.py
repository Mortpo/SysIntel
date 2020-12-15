print("Classe character bien importee")


class Character:

    # constructeur
    def __init__(self, nom, prenom, age, profession, boostDeMoral):
        self.nom = nom
        self.prenom = prenom
        self.age = int(age)
        self.profession = profession
        self.boostDeMoral = float(boostDeMoral)

    # getters
    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

    def getAge(self):
        return self.age

    def getProfession(self):
        return self.profession

    def getBoostDeMoral(self):
        return self.boostDeMoral

    # setters
    def setNom(self, nouveauNom):
        self.nom = nouveauNom

    def setPrenom(self, nouveauPrenom):
        self.prenom = nouveauPrenom

    def setAge(self, nouvelAge):
        self.age = nouvelAge

    def setProfession(self, nouvelleProfession):
        self.profession = nouvelleProfession

    def setBoostDeMoral(self, nouveauBoostDeMoral):
        self.boostDeMoral = nouveauBoostDeMoral

    # surcharge de __repr__() -> déscription de l'objet
    def __repr__(self):
        return self.getPrenom() + " " + self.getNom() + ", age: " + str(
            self.getAge()) + ", profession: " + self.getProfession() + ", boost de moral: " + str(
            self.getBoostDeMoral())
