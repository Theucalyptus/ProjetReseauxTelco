from simulation import Simulation
from comutateur import StrategieRoutage
from shared import *

import matplotlib.pyplot as plt

if __name__=="__main__":
    sim1 = Simulation(StrategieRoutage.Hierarchique)
    sim1.run()
    (rej1, actif1) = sim1.getResultats()

    sim2 = Simulation(StrategieRoutage.PartageCharge)
    sim2.run()
    (rej2, actif2) = sim2.getResultats()

    sim3 = Simulation(StrategieRoutage.Dynmaique)
    sim3.run()
    (rej3, actif3) = sim3.getResultats()

    temps = [i for i in range(0, DUREE)]

    fig, ax = plt.subplots()
    ax.plot(temps, rej1)
    ax.plot(temps, actif1)
    ax.plot(temps, rej2)
    ax.plot(temps, actif2)
    ax.plot(temps, rej3)
    ax.plot(temps, actif3)
    ax.legend(['Hierarchique Rejets', 'Hierarchique Actifs', 'Partage Charge Rejets', 'Partage Charge Actifs', 'Dynamique Rejets', 'Dynamique Actifs'])

    ax.set(xlabel='Temps (m)', ylabel='Nombre d\' appels',
        title='Mon super titre')
    ax.grid()

    #fig.savefig("out_" + str(NBAPPEL) + "_" + STRATEGIE.name + "_" + str(DUREE) + ".png")
    plt.show()

