import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import copy


def addtext(list2, colore):
    i = 0
    for y in list2:
        plt.text(i, y, str(y), fontsize=12, color=colore)
        i += 1


def showgraph(title, fileloc):
    plt.title(title, fontsize=20)
    plt.savefig(fileloc, dpi=100, bbox_inches="tight")


def aggiungitesto(listascelte, listacolori):
    for s, c in zip(listascelte, listacolori):
        addtext(s, c)


def main():
    # Apertura dei dati
    covid_file = open("dpc-covid19-ita-andamento-nazionale.csv", "r")
    covid_parser = csv.reader(covid_file, delimiter=",", quotechar='"')
    alldays = list(covid_parser)[-1:]

    tamponi = int(alldays[0][11])
    totalecasiposabs = int(alldays[0][10])
    totalecasinegabs = tamponi - totalecasiposabs

    # Frequenze relative positivi e negativi
    posrel = totalecasiposabs / tamponi
    negrel = totalecasinegabs / tamponi
    valori = [str(round(posrel * 100, 2))+"%",
              str(round(negrel * 100, 2)) + "%"]

    # Inserisco stile
    plt.style.use('dark_background')
    plt.figure(figsize=(21, 10))

    plt.pie(x=[posrel, negrel], labels=valori, colors=["#9b0000", "#0039cb"])
    plt.legend(labels=["Positivi", "Negativi"], fontsize=20)
    showgraph("Risultato tamponi totali (aggiornato al {})".format(alldays[0][0]), "../assets/posneglatestpie.png")

    plt.style.use('dark_background')
    plt.figure(figsize=(21, 10))
    barseries = pd.Series(data=[totalecasiposabs, totalecasinegabs], index=["Positivi", "Negativi"])
    barseries.plot.bar(color=["#9b0000", "#0039cb"])
    plt.text(0, barseries['Positivi']+2000, str(barseries['Positivi']), fontsize=12, color="#9b0000", ha="center")
    plt.text(1, barseries['Negativi']+2000, str(barseries['Negativi']), fontsize=12, color="#0039cb", ha="center")
    showgraph("Risultato tamponi totali (aggiornato al {})".format(alldays[0][0]), "../assets/posneglatestbar.png")
    return


main()
