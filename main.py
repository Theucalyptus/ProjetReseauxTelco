from simulation import Simulation
from comutateur import StrategieRoutage
from shared import *

import matplotlib.pyplot as plt

if __name__=="__main__":
    sim1 = Simulation(StrategieRoutage.Hierarchique)
    sim1.run()
    (rej1, actif1) = sim1.getResultats()
    print(rej1[-1]/(NBAPPEL_PAR_SECONDES*DUREE)) # ratio d'appels ratés

    sim2 = Simulation(StrategieRoutage.PartageCharge)
    sim2.run()
    (rej2, actif2) = sim2.getResultats()
    print(rej2[-1]/(NBAPPEL_PAR_SECONDES*DUREE)) # ratio d'appels ratés

    sim3 = Simulation(StrategieRoutage.Dynamique)
    sim3.run()
    (rej3, actif3) = sim3.getResultats()
    print(rej3[-1]/(NBAPPEL_PAR_SECONDES*DUREE)) # ratio d'appels ratés

    temps = [i for i in range(0, DUREE)]


    # Affichage du nombre d'appels en cours au temps t
    fig, ax = plt.subplots()
    ax.plot(temps, actif1)
    ax.plot(temps, actif2)
    ax.plot(temps, actif3)
    ax.legend(['Hierarchique Actifs', 'Partage Charge Actifs', 'Dynamique Actifs'])

    ax.set(xlabel='Temps (s)', ylabel='Nombre d\' appels', title='Nombre d\'appels en cours au temps t')
    ax.grid()

    # fig.savefig("acc_" + str(NBAPPEL_PAR_SECONDES) + "_" + str(DUREE) + ".png")



    # Affichage du nombre d'appels total rejetés au cours du temps
    fig, ax = plt.subplots()
    ax.plot(temps, rej1)
    ax.plot(temps, rej2)
    ax.plot(temps, rej3)

    ax.legend(['Hierarchique Rejets', 'Partage Charge Rejets', 'Dynamique Rejets'])
    ax.set(xlabel='Temps (s)', ylabel='Nombre d\' appels', title='Nombre d\'appels rejetés au cours du temps')
    # fig.savefig("rej_" + str(NBAPPEL_PAR_SECONDES) + "_" + str(DUREE) + ".png")
    plt.show()

