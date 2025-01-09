class Route:

    def __init__(self):
        self.liens = []

    def ajouterLien(self, lien):
        ret = lien.ajoutAppel()
        if ret:
            self.liens.append(lien)
        return ret

    def liberer(self):
        for l in self.liens:
            l.libererAppel()

    def checkCycle(self, noeud):
        cycle = False
        for l in self.liens:
            cycle = cycle or l.dessert(noeud)
        return cycle
    
    def printR(self):
        for l in self.liens:
            print(l.coma.getNom(),"-",l.comb.getNom(), "->", end="")
        print("\n")