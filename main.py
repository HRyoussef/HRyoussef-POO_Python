from models.Animal import Animal
from models.Serpent import Serpent
from models.Oiseau import Oiseau
from models.Zoo import Zoo


## Création des objets
#souris_verte = Animal(nom='Stewart', poids=0.005, taille=10)
#python_vert = Serpent(nom='Python', poids=15, taille=300, longueur=350)
#perroquet = Oiseau(nom='Coco', poids=0.9, taille=25, envergure=40)


## Test
#print(souris_verte.nom, souris_verte.poids, souris_verte.taille)
#print(python_vert.nom, python_vert.se_deplacer(), python_vert.longueur)
#print(perroquet.nom, perroquet.se_deplacer(), perroquet.envergure)
#from models.Animal import Animal

animal = Animal("Chat", 4.5, 30)

print(animal.get_nom())
print(animal.get_poids())

## Test 
#animal.set_poids(-5)



# Création d'animaux
chat = Animal("Chat", 4.5, 30)
python = Serpent("Python", 15, 300, 350)
perroquet = Oiseau("Coco", 0.9, 25, 40)

# Création du zoo
zoo = Zoo([chat, python])


# Ajouter un animal
zoo.ajouter_animal(perroquet)

# Afficher les animaux
zoo.afficher_animaux()