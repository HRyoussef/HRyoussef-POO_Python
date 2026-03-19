class Animal:
    def __init__(self, nom: str, poids: float, taille: int):
        self.nom = nom
        self.poids = poids
        self.taille = taille
    def se_deplacer(self):
        pass


# Classe enfant Serpent
class Serpent(Animal):
    def __init__(self, nom: str, poids: float, taille: int, longueur: float):
        Animal.__init__(self, nom, poids, taille)  # appelle le constructeur de Animal
        self.longueur = longueur

    def se_deplacer(self):
        return f"Le serpent {self.nom} rampe."
        #pass

# Classe enfant Oiseau
class Oiseau(Animal):
    def __init__(self, nom: str, poids: float, taille: int, envergure: float):
        Animal.__init__(self, nom, poids, taille)
        self.envergure = envergure

    def se_deplacer(self):
        return f"L'oiseau {self.nom} vole."
        #pass

# Création des objets
souris_verte = Animal(nom='Stewart', poids=0.005, taille=10)
python_vert = Serpent(nom='Python', poids=15, taille=300, longueur=350)
perroquet = Oiseau(nom='Coco', poids=0.9, taille=25, envergure=40)


# Test
print(souris_verte.nom, souris_verte.poids, souris_verte.taille)
print(python_vert.nom, python_vert.se_deplacer(), python_vert.longueur)
print(perroquet.nom, perroquet.se_deplacer(), perroquet.envergure)