import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#modifica questa variabile per visualizzare gli ultimi n giorni
days = 0


def filter_date(dataframe): 
    fixeddate = []

    for h in dataframe.index:
        h = h.split('T')[0]
        (_, month, day) = h.split('-')
        h = month + "-" + day
        fixeddate.append(h)

    #Sostituisco l'indice con i nuovi dati
    dataframe.index = fixeddate
    return

def remove_cumulation(series):
    copylist = list(series)
    for i, n in enumerate(copylist):
        if (i == 0): continue
        copylist[i] = n - series[i-1]
    return copylist


def main():
    dataframe = pd.read_csv("dpc-covid19-ita-andamento-nazionale.csv", sep=",", index_col=0)
    # Rimuovo gli orari, tengo la data
    filter_date(dataframe)

    #Rimuovo cumulazione dati
    #dataframe['tamponi'] = remove_cumulation(dataframe['tamponi'])
    dataframe['deceduti'] = remove_cumulation(dataframe['deceduti'])
    dataframe['dimessi_guariti'] = remove_cumulation(dataframe['dimessi_guariti'])

    # tema nero
    plt.style.use('dark_background')
    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(19.2, 10.8)

    #ax.plot(dataframe['tamponi'], color="purple")
    ax.plot(dataframe['deceduti'], color="red")
    ax.plot(dataframe['dimessi_guariti'], color="green")
    ax.plot(dataframe['nuovi_positivi'], color="orange")

    ax.legend(("Deceduti", "Guariti", "Nuovi positivi"), fontsize=15)
    ax.set_title("Deceduti, guariti e nuovi positivi dal 24/02/2020", fontsize=20)
    ax.set_xticks([])
    fig.tight_layout(pad=3.0)
    fig.savefig("../assets/deathconhealfromstartline.png", dpi=100)

main()