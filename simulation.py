from shared import *

from comutateur import *
from client import Client
from lien import Lien

class Simulation:

    def __init__(self, strategie):
        self.cts = []
        self.ca = []
        self.client = {}
        self.strategie = strategie
        self.resultats = None

    def run(self):
        print("##### DEBUT SIMULATION #####")
        ca1 = Commutateur(self.strategie, "ca1")
        ca2 = Commutateur(self.strategie, "ca2")
        ca3 = Commutateur(self.strategie, "ca3")
        cts1 =  Commutateur(self.strategie, "cts1")
        cts2 =  Commutateur(self.strategie, "cts2")

        u1 = Client("u1", ca1)
        u2 = Client("u2", ca2)
        u3 = Client("u3", ca3)
        
        l1 = Lien(CA_CA, ca1, ca2)
        l2 = Lien(CA_CA, ca2, ca3)
        l3 = Lien(CA_CTS, ca1, cts1)
        l4 = Lien(CA_CTS, ca1, cts2)
        l5 = Lien(CA_CTS, ca2, cts1)
        l6 = Lien(CA_CTS, ca2, cts2)
        l7 = Lien(CA_CTS, ca3, cts1)
        l8 = Lien(CA_CTS, ca3, cts2)
        l9 = Lien(CTS_CTS, cts1, cts2)

        self.rejChrono = []
        self.actifChrono = []
        nbAppelParTick = NBAPPEL_PAR_SECONDES
        
        distrib = [nbAppelParTick for i in range(DUREE)] # peut être remplacer par une loi de Poisson
        appelsPasses = []

        for time in range(0, DUREE):
            nbRej = 0
            nbActif = 0
            n = [0, 0, 0]
            for i in range(distrib[time]):
                n[randint(0, 2)]+=1

            nbRej += u1.update([u2, u3], n[0])
            nbRej += u2.update([u1, u3], n[1])
            nbRej += u3.update([u1, u2], n[2])


            # permet d'avoir les appels totaux rejeté au temps t
            if len(self.rejChrono) == 0:
                val_rej_prec = 0
            else: 
                val_rej_prec = self.rejChrono[-1]

                
            self.rejChrono.append(nbRej + val_rej_prec)
            nbActif += len(u1.appelsIDs)           
            nbActif += len(u2.appelsIDs)
            nbActif += len(u3.appelsIDs)
            self.actifChrono.append(nbActif)




    def getResultats(self):
        return (self.rejChrono, self.actifChrono)





