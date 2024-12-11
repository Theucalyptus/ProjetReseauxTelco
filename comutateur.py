from enum import Enum
from random import randint
from shared import *
import numpy as np

class TypeCommutateur(Enum):
    CA = 1
    CTS = 2

class StrategieRoutage(Enum):
    Hierarchique = 1
    PartageCharge = 2
    Dynmaique = 3
    
class Commutateur:


    def __init__(self, strategie, nom):
        self.voisins = {}
        self.clients =  []
        self.strategie = strategie
        self.appelsCourants = [] # listes des ID d'appels passant par le commutateur
        self.nom = nom

    def addVoisin(self, noeud, link):
        self.voisins[noeud.getNom()] = (link, noeud)

    def addClient(self, client):
        self.clients.append(client)

    def getNom(self):
        return self.nom

    def getLocalIDs(self):
        return [f.getID() for f in self.clients]
    
    # Routage statique hiérarchique
    def __hierarchique(self, destination):
        if self.nom == "ca1":
            return "cts1"
        elif self.nom == "ca2":
            return "cts1"
        elif self.nom == "ca3":
            return "cts2"
        elif self.nom == "cts1" or self.nom == "cts2":
            return destination.getCA().getNom()

    # Effectue un partage équitable entre tout les prochains commutateur possible en fonction de la capacité des liens
    # Ne prend pas en compte la longueur des chemins
    def __partagecharge(self, destination, route):
        dn = destination.getID()
        candidats = [] 
        cap = []
        zipped = [(l, c) for l, c in self.voisins.values() if (dn in c.getLocalIDs()) or ("cts" in c.getNom())]
        for l, c in zipped:
            if not route.checkCycle(c):
                candidats.append(c)
                cap.append(l.getCapacite())
        probs = np.divide(cap, sum(cap)).tolist()
        choice = np.random.choice(candidats, 1, probs)
        return choice[0].getNom()
    
    # Effectue un routage privilégiant les chemins courts lorsque que la charge le permet
    def __dynamique(self, destination, route):
        dn = destination.getID()
        ca = [(l, c) for l, c in self.voisins.values() if dn in c.getLocalIDs()]
        cts = [(l, c) for l, c in self.voisins.values() if "cts" in c.getNom()]
        
        # Si le CA de la destination est dans nos voisins, alors on cherche à le joindre par un lien direct en priorité
        for l, c in ca:
            # Si il reste de la place sur le lien
            if l.getCharge() < l.getCapacite():
                return c.getNom()
            
        # Sinon, alors on cherche à passer par un autre CTS
        for l, c in cts:
            if not route.checkCycle(c) and l.getCharge() < l.getCapacite():
                return c.getNom()
        
        # Aucune route possible, on rejette l'appel
        return None

    
    def getRoute(self, destination, route):
        # si le commutateur n'est pas raccordé au client final
        if not (destination.getID() in self.getLocalIDs()):
            # on construit la route
            nextHop=None
            if self.strategie == StrategieRoutage.Hierarchique:
                nextHop = self.__hierarchique(destination)
            elif self.strategie == StrategieRoutage.PartageCharge:
                nextHop = self.__partagecharge(destination, route)
            elif self.strategie == StrategieRoutage.Dynmaique:
                nextHop = self.__dynamique(destination, route)
                if nextHop == None:
                    route.liberer()
                    return None
            (lien, noeud) = self.voisins[nextHop]
            res = route.ajouterLien(lien)
            if res:
                return noeud.getRoute(destination, route)
            else:
                route.liberer()
                return None
            
        # sinon alors la route se limite au commutateur lui-même
        else:
            return route