from Animal import Animal
# Classe enfant Oiseau
class Oiseau(Animal):
    def __init__(self, nom: str, poids: float, taille: int, envergure: float):
        Animal.__init__(self, nom, poids, taille)
        self.envergure = envergure

    def se_deplacer(self):
        return f"L'oiseau {self.nom} vole."
        #pass