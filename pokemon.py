class Pokemon:
    def __init__(self, nom):
        self.__nom = nom
        self.__pv = 100
        self.puissance_attaque = 0
        self.defense = 0
        
    def attaquer(self, adversaire):
        degats = self.puissance_attaque - adversaire.defense
        if degats < 0:
            degats = 0
        
        adversaire.__pv -= degats
        
        print(f"{self.__nom} attaque {adversaire.__nom} et inflige {degats} dégâts.")
        
    def est_ko(self):
        return self.__pv <= 0
    
    def get_nom(self):
        return self.__nom
    
    def set_nom(self, nom):
        self.__nom = nom
        
    def get_pv(self):
        return self.__pv
    
    def set_pv(self, pv):
        self.__pv = pv
