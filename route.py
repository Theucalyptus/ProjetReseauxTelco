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

    def afficher(self):
        str = ""
        for l in self.liens:
            str += l.toString() + " -> "
        str += "FIN"
        print(str)
