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


def savegraph(title, fileloc):
    plt.title(title, fontsize=20)
    plt.savefig(fileloc, dpi=100, bbox_inches="tight")


def aggiungitesto(listascelte, listacolori):
    for s, c in zip(listascelte, listacolori):
        addtext(s, c)


def main():
    # Apertura dei dati
    covid_file = open("dpc-covid19-ita-andamento-nazionale.csv", "r")
    covid_parser = csv.reader(covid_file, delimiter=",", quotechar='"')
    lasttwodays = list(covid_parser)[-2:]
    today, yesterday = lasttwodays[1], lasttwodays[0]

    tamponi = int(today[12])
    totalecasiposabs = int(today[11])
    totalecasinegabs = tamponi - totalecasiposabs

    #Creo aerogramma non cumulativo
    tamponitoday = tamponi - int(yesterday[12])
    casipositivitoday = int(today[7])
    casinegativitoday = tamponitoday - casipositivitoday

    # Frequenze relative positivi e negativi cumulativi
    posrel = totalecasiposabs / tamponi
    negrel = totalecasinegabs / tamponi
    valori = [str(round(posrel * 100, 2))+"%", str(round(negrel * 100, 2)) + "%"]

    # Frequenze relative positivi e negativi non cumulativi
    posreltoday = casipositivitoday / tamponitoday
    negreltoday = casinegativitoday / tamponitoday
    valoritoday = [str(round(posreltoday * 100, 2))+"% (" + str(casipositivitoday) +")", str(round(negreltoday * 100, 2)) + "% (" + str(casinegativitoday) + ")"]

    # Parsing nella data e dell'ora di oggi
    datatoday = today[0].split("T")[0]
    oratoday = today[0].split("T")[1]

    # Inserisco stile
    plt.style.use('dark_background')
    plt.figure(figsize=(21, 10))

    # Sezione dedicata al grafico a torta (aerogramma)
    plt.pie(x=[posrel, negrel], labels=valori, colors=["#9b0000", "#0039cb"])
    plt.legend(labels=["Positivi", "Negativi"], fontsize=20)
    savegraph("Risultato tamponi totali (aggiornato al {})".format(datatoday + " " + oratoday), "../assets/posnegcumpie.png")
    plt.clf()
    
    # Sezione dedicata al grafico a barre
    plt.style.use('dark_background')
    plt.figure(figsize=(21, 10))
    barseries = pd.Series(data=[totalecasiposabs, totalecasinegabs], index=["Positivi", "Negativi"])
    barseries.plot.bar(color=["#9b0000", "#0039cb"])
    plt.text(0, barseries['Positivi']+2000, str(barseries['Positivi']),fontsize=12, color="#9b0000", ha="center")
    plt.text(1, barseries['Negativi']+2000, str(barseries['Negativi']),fontsize=12, color="#0039cb", ha="center")
    savegraph("Tamponi e contagi (aggiornato al {})".format(datatoday + " " + oratoday), "../assets/posnegcumbar.png")
    plt.clf()

    # Sezione dedicata al grafico a torta (aerogramma) del non cumulativo
    plt.style.use('dark_background')
    plt.figure(figsize=(21, 10))
    plt.pie(x=[posreltoday, negreltoday], labels=valoritoday, colors=["#9b0000", "#0039cb"])
    plt.legend(labels=["Positivi", "Negativi"], fontsize=20)
    savegraph("Tamponi e variazione contagi del {})".format(datatoday + " " + oratoday), "../assets/posnegtodaypie.png")
    plt.clf()
    return

main()
