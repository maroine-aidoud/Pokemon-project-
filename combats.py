from pokemon import Pokemon
from type import Normal, Feu, Eau, Terre

class Combat:
    def __init__(self, joueur1, joueur2):
        self.__joueur1 = joueur1
        self.__joueur2 = joueur2
        self.__adversaire = None
        self.__tour = 1

    def __prochain_adversaire(self):
        if self.__adversaire is None:
            self.__adversaire = self.__joueur2
        else:
            self.__adversaire = self.__joueur1 if self.__adversaire == self.__joueur2 else self.__joueur2

    def __attaque(self, attaquant, defenseur):
        type_attaquant = type(attaquant).__name__
        type_defenseur = type(defenseur).__name__

        multiplicateur = 1.0

        if type_attaquant == "Feu":
            if type_defenseur == "Terre":
                multiplicateur = 0.5
            elif type_defenseur == "Eau":
                multiplicateur = 2.0
        elif type_attaquant == "Eau":
            if type_defenseur == "Feu":
                multiplicateur = 0.5
            elif type_defenseur == "Terre":
                multiplicateur = 2.0
        elif type_attaquant == "Terre":
            if type_defenseur == "Eau":
                multiplicateur = 0.5
            elif type_defenseur == "Feu":
                multiplicateur = 2.0

        degats = int(attaquant.puissance_attaque * multiplicateur) - defenseur.defense

        if degats < 0:
            degats = 0

        defenseur.set_pv(defenseur.get_pv() - degats)

        print(f"{attaquant.get_nom()} attaque {defenseur.get_nom()} et inflige {degats} dégâts.")

    def jouer(self):
        print("Le combat commence !")

        while True:
            print(f"Tour {self.__tour}:")
            print(f"{self.__joueur1.get_nom()} vs {self.__joueur2.get_nom()}")

# le projet n'est pas terminé 