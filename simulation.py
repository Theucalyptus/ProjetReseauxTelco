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

            self.rejChrono.append(nbRej)
            nbActif += len(u1.appelsIDs)           
            nbActif += len(u2.appelsIDs)
            nbActif += len(u3.appelsIDs)
            self.actifChrono.append(nbActif)

        # Manière pas belle de calculer le nombre total d'appels qui ont réussi
        #     for a1 in u1.appelsIDs:
        #         if not(a1 in appelsPasses):
        #             appelsPasses.append(a1)
        #     for a2 in u2.appelsIDs:
        #         if not(a2 in appelsPasses):
        #             appelsPasses.append(a2)
        #     for a3 in u3.appelsIDs:
        #         if not(a3 in appelsPasses):
        #             appelsPasses.append(a3)

        # print(len(appelsPasses))


        # links = [l1, l2, l3, l4, l5, l6, l7, l8, l9]
        # for l in links:
        #     print("Lien " + l.toString() + "{:10.4f}".format(l.getCharge() / l.getCapacite()))


    def getResultats(self):
        return (self.rejChrono, self.actifChrono)





