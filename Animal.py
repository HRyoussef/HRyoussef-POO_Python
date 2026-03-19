#class Animal:
#    def __init__(self, nom: str, poids: float, taille: int):
#        self.nom = nom
#        self.poids = poids
#        self.taille = taille
#    def se_deplacer(self):
#        pass

class Animal:
    def __init__(self, nom: str, poids: float, taille: int):
        self._nom = nom              # protected
        self.__poids = None          # private
        self._taille = taille        # protected

        self.set_poids(poids)        # validation via setter

    # Getter nom
    def get_nom(self):
        return self._nom

    # Setter nom
    def set_nom(self, nom):
        if not nom:
            raise ValueError("Le nom ne peut pas être vide")
        self._nom = nom

    # Getter poids (private)
    def get_poids(self):
        return self.__poids

    # Setter poids avec validation
    def set_poids(self, poids):
        if poids < 0:
            raise ValueError("Le poids ne peut pas être négatif")
        self.__poids = poids

    # Getter taille
    def get_taille(self):
        return self._taille

    # Setter taille
    def set_taille(self, taille):
        if taille <= 0:
            raise ValueError("La taille doit être positive")
        self._taille = taille

    def se_deplacer(self):
        pass
