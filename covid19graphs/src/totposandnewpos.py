import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def removehour(element):
    templist = element.split('T')
    return templist[0]


def main():
    dataframe = pd.read_csv(
        "dpc-covid19-ita-andamento-nazionale.csv", sep=",", index_col=0)
    # Rimuovo gli orari, tengo la data
    fixeddate = []
    for h in dataframe.index:
        h = h.split('T')[0]
        fixeddate.append(h)

    dataframe.index = fixeddate

    plt.style.use('dark_background')

    figure, axes = plt.subplots(2, 1)
    x = dataframe.index
    y = dataframe['totale_positivi']
    axes[0].set_title('Totale positivi', fontsize=20)
    axes[0].bar(x, y, color="blue")

    y = dataframe['variazione_totale_positivi']
    axes[1].set_title('Variazione positivi', fontsize=20)
    axes[1].bar(x, y, color="red")
    for tick in axes[0].get_xticklabels():
        tick.set_rotation(90)

    for tick in axes[1].get_xticklabels():
        tick.set_rotation(90)

    figure.set_size_inches(21, 10)
    figure.tight_layout(pad=3.0)
    figure.savefig("../assets/totposandvariation.png", dpi=100)

    return


main()
