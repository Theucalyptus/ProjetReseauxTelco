from enum import Enum
from random import randint

from route import Route

class EtatClient(Enum):
    LIBRE = 1
    APPEL = 2

class Client:

    def __init__(self, id, ca):
        # Nombre d'appels lancé 
        self.appelCounter = 0

        # Dictionnnaire contenant l'id d'un appel et sa durée en cours
        self.dureesAppels = {}
        # Dictionnnaire contenant l'id d'un appel et sa durée totale
        self.dureesAppelTotals = {}
        # ID des appels en cours
        self.appelsIDs = []
        # Dictionnnaire contenant l'id d'un appel et sa route sur le réseau
        self.routes = {}

        self.id = id # id de l'appel
        self.ca = ca # Commutateur d'abonné associé au client

        self.ca.addClient(self) # On associe le client au commutateur d'aboné

    def __finAppel(self, appelID):
        assert(appelID in self.appelsIDs)
        # Fin d'un appel
        self.dureesAppelTotals.pop(appelID)
        self.dureesAppels.pop(appelID)
        r = self.routes.pop(appelID)
        self.appelsIDs.remove(appelID)
        r.liberer()

    def __lancerAppel(self, destination):
        # Début d'un appel
        callID = self.__getNewCallID()
        route = self.ca.getRoute(destination, Route())
        if route != None:
            self.appelsIDs.append(callID)
            self.routes[callID] = route
            self.dureesAppelTotals[callID] = randint(60, 300)
            self.dureesAppels[callID] = 0
        
        return (route != None)
        
    def getID(self):
        return self.id
    
    def getCA(self):
        return self.ca

    def __getNewCallID(self):
        # On renvoie un id unique
        self.appelCounter += 1
        return self.id + "_" + str(self.appelCounter)

    def update(self, clients, nb):
        # On met à jour la durée des appels en cours
        for callID in self.appelsIDs:
            duree = self.dureesAppels[callID]
            target = self.dureesAppelTotals[callID]
            if duree >= target:
                self.__finAppel(callID)
            else:
                self.dureesAppels[callID]+=1

        # On lance nb appels
        nbRejets = 0
        for i in range(nb):
            # On choisit au hasard un client parmit les autres
            dest = clients[randint(0, len(clients)-1)]
            res = self.__lancerAppel(dest)
            if not res:
                nbRejets += 1
        return nbRejets