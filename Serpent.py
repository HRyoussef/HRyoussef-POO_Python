from Animal import Animal
# Classe enfant Serpent
class Serpent(Animal):
    def __init__(self, nom: str, poids: float, taille: int, longueur: float):
        Animal.__init__(self, nom, poids, taille)  # appelle le constructeur de Animal
        self.longueur = longueur

    def se_deplacer(self):
        return f"Le serpent {self.nom} rampe."
        #pass
