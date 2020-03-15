import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import copy
days = 0  # 0 se vuoi vedere ogni giorno dal 24 febbraio

# Funzione che rimuove l'orario dalla data di prelievo dei dati


def removehourandyear(listdays):
    for index, elem in enumerate(listdays):
        newelem = elem.split(" ")
        listdays[index] = newelem[0]
    
    for index, elem in enumerate(listdays):
        elemlist = elem.split("-")
        listdays[index] = elemlist[1]+"-"+elemlist[2]
    return


# Funzione che rimuove la cumulazione dei dati
def dayperday(listelements):
    # Copia in una nuova zona di memoria tutti gli elementi della lista, niente è lasciato in comune a listelements
    originalist = copy.deepcopy(listelements)
    for index, elem in enumerate(listelements):
        if index == 0:
            continue
        for i, e in enumerate(elem):
            if i == 0 or i == 1:
                continue
            elem[i] = int(elem[i]) - int(originalist[index-1][i])
    return listelements


def addtext(list1, list2, colore):
    i = 0
    for x, y in zip(list1, list2):
        plt.text(i, y, str(y), fontsize=12, color=colore)
        i += 1

def showgraph(title):
    plt.title(title, fontsize=20)
    plt.legend(fontsize = 20)
    plt.show()

def aggiungitesto(giorni, listascelte, listacolori):
    for s, c in zip(listascelte, listacolori):
        addtext(giorni, s, c)

def main():
    # Apertura dei dati
    covid_file = open("dpc-covid19-ita-andamento-nazionale.csv", "r")
    covid_parser = csv.reader(covid_file, delimiter=",", quotechar='"')
    alldays = list(covid_parser)[1:]

    # Lista giorni
    listadati = dayperday(alldays)[-days:]                  #Rimuovo la cumulazione dai dati
    giornocasi = [h[0] for h in listadati]          #Creo una lista da cui ricavare i giorni interessati
    removehourandyear(giornocasi)

    # Liste di dati
    decxday = [int(h[9]) if h[9] else 0 for h in listadati]         #Lista z per giorno
    guaxday = [int(h[8]) if h[8] else 0 for h in listadati]         #Lista guarigioni per giorno
    contxday = [int(h[10])if h[10] else 0 for h in listadati]       #Lista contagiati per giorno

    # Creazioni Serie
    deathseries = pd.Series(data=decxday, index=giornocasi)
    healseries = pd.Series(data=guaxday, index=giornocasi)
    contseries = pd.Series(data=contxday, index=giornocasi)

    #Inserisco stile
    plt.style.use('dark_background')

    listaseriescelte  = [deathseries, healseries, contseries]       #Lista delle serie che voglio vedere nel grafico
    listacolori = ["red", "green", "orange"]                        #Lista dei colori per ogni serie, in ordine

    # Grafico a linee
    deathseries.plot(alpha=1, color="red", label="Decessi", marker="o")
    contseries.plot(alpha=1, color="orange", label="Contagiati", marker='o')
    healseries.plot(alpha=1, color="green", label="Guarigioni", marker='o')

    #Aggiungo testo e mostro grafico
    aggiungitesto(giornocasi, listaseriescelte, listacolori)
    showgraph("Rapporto decessi/contagi/guarigioni per giorno (aggiornato al {})".format(listadati[-1][0]))
    return


main()
