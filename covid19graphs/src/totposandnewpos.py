import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def removehour(element):
    templist = element.split('T')
    return templist[0]


def main():
    dataframe = pd.read_csv("dpc-covid19-ita-andamento-nazionale.csv", sep=",", index_col=0)

    # Rimuovo gli orari, tengo la data
    fixeddate = []
    for h in dataframe.index:
        h = h.split('T')[0]
        fixeddate.append(h)

    #Sostituisco l'indice con i nuovi dati
    dataframe.index = fixeddate

    #tema nero
    plt.style.use('dark_background')

    #genero la figura e l'array a due posizioni per i due plot
    figure, axes = plt.subplots(2, 1)
    #x è sempre i giorni
    x = dataframe.index
    y = dataframe['totale_positivi']
    axes[0].set_title('Totale positivi', fontsize=20)
    #axes[0] conterrà il primo grafico a barre
    axes[0].bar(x, y, color="blue")

    y = dataframe['variazione_totale_positivi']
    axes[1].set_title('Variazione positivi', fontsize=20)
    #axes[0] conterrà il secondo grafico a barre
    axes[1].bar(x, y, color="red")
    #Ruoto i label sull'asse delle x in verticale
    for tick in axes[0].get_xticklabels():
        tick.set_rotation(90)

    for tick in axes[1].get_xticklabels():
        tick.set_rotation(90)

    #Modifico le dimensioni della figura e salvo la figura
    figure.set_size_inches(19.2, 10.8)
    figure.tight_layout(pad=3.0)
    figure.savefig("../assets/totposandvariation.png", dpi=100)

    return


main()
