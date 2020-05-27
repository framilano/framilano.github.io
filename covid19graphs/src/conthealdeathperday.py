import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def filter_date(dataframe): 
    fixeddate = []

    for h in dataframe.index:
        h = h.split('T')[0]
        (year, month, day) = h.split('-')
        h = month + "-" + day
        fixeddate.append(h)

    #Sostituisco l'indice con i nuovi dati
    dataframe.index = fixeddate
    return

def rotate_ticks(ax):
    for tick in ax.get_xticklabels():
        tick.set_rotation(90)

def remove_cumulation(series):
    copylist = list(series)
    for i, n in enumerate(copylist):
        if (i == 0): continue
        copylist[i] = n - series[i-1]
    return copylist

def add_labels(series, days, ax):
    maxes = []
    for m in series:
        maxes.append(max(m))
    offset = max(maxes)
    colors = ("orange", "green", "red")
    for color, ser in zip(colors,series):
        for day, value in zip(days, ser):
            ax.text(day, value + 1/70*offset, str(value), color = color, rotation=90)

def main():
    dataframe = pd.read_csv("dpc-covid19-ita-andamento-nazionale.csv", sep=",", index_col=0)

    # Rimuovo gli orari, tengo la data
    filter_date(dataframe)

    #Rimuovo cumulazione dati
    dataframe['deceduti'] = remove_cumulation(dataframe['deceduti'])
    dataframe['dimessi_guariti'] = remove_cumulation(dataframe['dimessi_guariti'])

    # tema nero
    plt.style.use('dark_background')
    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(19.2, 10.8)


    ax.plot(dataframe.index, dataframe['deceduti'], color="red", marker='o')
    ax.plot(dataframe.index, dataframe['dimessi_guariti'], color="green", marker='o')
    ax.plot(dataframe.index, dataframe['nuovi_positivi'], color="orange", marker='o')

    rotate_ticks(ax)
    ax.legend(("Deceduti", "Guariti", "Nuovi positivi"), fontsize=15)
    add_labels((dataframe['nuovi_positivi'], dataframe['dimessi_guariti'], dataframe['deceduti']), dataframe.index, ax)
    fig.tight_layout(pad=0.0)
    fig.savefig("../assets/deathconhealperdayline.png", dpi=100)

main()

