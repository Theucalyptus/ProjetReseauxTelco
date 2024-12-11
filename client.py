from enum import Enum
from random import randint

from route import Route

class EtatClient(Enum):
    LIBRE = 1
    APPEL = 2

class Client:

    def __init__(self, id, ca):
        self.appelCounter = 0

        self.dureesAppels = {}
        self.dureesAppelTotals = {}
        self.appelsIDs = []
        self.routes = {}

        self.id = id
        self.ca = ca
        self.ca.addClient(self)

    def __finAppel(self, appelID):
        assert(appelID in self.appelsIDs)
        self.dureesAppelTotals.pop(appelID)
        self.dureesAppels.pop(appelID)
        r = self.routes.pop(appelID)
        self.appelsIDs.remove(appelID)
        r.liberer()

    def __lancerAppel(self, destination):
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
        self.appelCounter += 1
        return self.id + "_" + str(self.appelCounter)

    def update(self, clients, nb):
        for callID in self.appelsIDs:
            duree = self.dureesAppels[callID]
            target = self.dureesAppelTotals[callID]
            if duree >= target:
                self.__finAppel(callID)
            else:
                self.dureesAppels[callID]+=1

        nbRejets = 0
        for i in range(nb):
            dest = clients[randint(0, len(clients)-1)]
            res = self.__lancerAppel(dest)
            if not res:
                nbRejets += 1
        return nbRejets