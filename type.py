from pokemon import Pokemon

class Type(Pokemon):
    def __init__(self, nom, pv, puissance_attaque, defense):
        super().__init__(nom)
        self.__pv = pv
        self.puissance_attaque = puissance_attaque
        self.defense = defense
    
    def donner_informations(self):
        print(f"Nom: {self._Pokemon__nom}")
        print(f"Points de vie: {self.__pv}")
        print(f"Puissance d'attaque: {self.puissance_attaque}")
        print(f"Défense: {self.defense}")
        
class Normal(Type):
    def __init__(self, nom):
        super().__init__(nom, pv=100, puissance_attaque=10, defense=5)
        
class Feu(Type):
    def __init__(self, nom):
        super().__init__(nom, pv=120, puissance_attaque=7, defense=6)
        
class Eau(Type):
    def __init__(self, nom):
        super().__init__(nom, pv=80, puissance_attaque=12, defense=4)
        
class Terre(Type):
    def __init__(self, nom):
        super().__init__(nom, pv=150, puissance_attaque=5, defense=10) 



p1 = Normal("Pikachu")
p2 = Feu("Charmander")
p3 = Eau("Squirtle")
p4 = Terre("Onix")

# p1.donner_informations()
