from comutateur import *

class Lien:

    def __init__(self, capacite, coma, comb):
        self.capacity = capacite # capacité totale
        self.coma = coma # Côté gauche du lien
        self.comb = comb # Côté droit du lien
        self.charge = 0 # capacité éffective

        # On notifie le commutateur de son voisin
        self.coma.addVoisin(self.comb, self) 
        self.comb.addVoisin(self.coma, self) 

    def getCharge(self):
        return self.charge
    
    def getCapacite(self):
        return self.capacity

    def ajoutAppel(self):
        # Ajout d'un appel sur le lien
        if self.charge == self.capacity:
            return False
        else:
            self.charge +=1
            return True
    
    def libererAppel(self):
        # Un appel est terminé, on libère le lien
        self.charge-=1
        
    def dessert(self, id):
        # on verifie si le lien dessert le commutateur d'ID id
        return (id.getNom() == self.coma.getNom() or id.getNom() == self.comb.getNom())
    
    def toString(self):
        return self.coma.getNom() + "-" + self.comb.getNom()
