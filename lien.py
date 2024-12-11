from comutateur import *

class Lien:

    def __init__(self, capacite, coma, comb):
        self.capacity = capacite
        self.coma = coma
        self.comb = comb
        self.charge = 0

        self.coma.addVoisin(self.comb, self)
        self.comb.addVoisin(self.coma, self)

    def getCharge(self):
        return self.charge
    
    def getCapacite(self):
        return self.capacity

    def ajoutAppel(self):
        if self.charge == self.capacity:
            return False
        else:
            self.charge +=1
            return True
    
    def libererAppel(self):
        self.charge-=1
        
    def dessert(self, id):
        return (id.getNom() == self.coma.getNom() or id.getNom() == self.comb.getNom())
    
    def toString(self):
        return self.coma.getNom() + "-" + self.comb.getNom()
