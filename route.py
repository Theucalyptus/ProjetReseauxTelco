class Route:

    def __init__(self):
        self.liens = []

    def ajouterLien(self, lien):
        # on prend le lien "lien" dans la route
        ret = lien.ajoutAppel()
        if ret:
            self.liens.append(lien)
        return ret

    def liberer(self):
        # L'appel est terminé, on libère les ressources
        for l in self.liens:
            l.libererAppel()

    def checkCycle(self, noeud):
        # On vérifie si le noeud qu'on ajoute a la route crée un cycle
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
