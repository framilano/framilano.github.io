import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import copy


def addtext(list1, list2, colore):
    i = 0
    for x, y in zip(list1, list2):
        plt.text(i, y, str(y), fontsize=12, color=colore)
        i += 1


def showgraph(title):
    plt.title(title, fontsize=15)
    plt.legend(labels=["Positivi", "Negativi"])
    plt.show()


def aggiungitesto(giorni, listascelte, listacolori):
    for s, c in zip(listascelte, listacolori):
        addtext(giorni, s, c)


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
    print(posrel, negrel)
    valori = [str(round(posrel * 100, 2))+"%",
              str(round(negrel * 100, 2)) + "%"]

    # Inserisco stile
    plt.style.use('dark_background')

    plt.pie(x=[posrel, negrel], labels=valori, colors=["#9b0000", "#0039cb"])
    showgraph("Grafico tamponi totali (aggiornato al {})".format(alldays[0][0]))


main()
