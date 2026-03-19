from models.Animal import Animal

class Zoo:
    def __init__(self, animaux: list):
        # Vérification que la liste contient bien des Animal
        for animal in animaux:
            if not isinstance(animal, Animal):
                raise ValueError("Tous les éléments doivent être des objets de type Animal")

        self._animaux = animaux  # protected

    # Méthode pour ajouter un animal
    def ajouter_animal(self, animal: Animal):
        if not isinstance(animal, Animal):
            raise ValueError("Seuls les objets de type Animal peuvent être ajoutés")
        
        self._animaux.append(animal)

    # Méthode pour afficher les animaux
    def afficher_animaux(self):
        for animal in self._animaux:
            print(animal.get_nom(), "-", animal.get_poids())