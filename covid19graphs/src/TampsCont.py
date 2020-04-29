import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import copy
days = 0  # 0 se vuoi vedere ogni giorno dal 24 febbraio

# Funzione che rimuove l'orario dalla data di prelievo dei dati


def removehourandyear(listdays):
    for index, elem in enumerate(listdays):
        newelem = elem.split("T")
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
            if i == 0 or i == 1 or e.isdigit() == False or elem[i].isdigit() == False or originalist[index-1][i].isdigit() == False:
                continue
            elem[i] = int(elem[i]) - int(originalist[index-1][i])
    return listelements

# Aggiungi valori sulle coordinate


def addtext(list1, list2, colore):
    i = 0
    for x, y in zip(list1, list2):
        plt.text(i, y, str(y), fontsize=12, color=colore)
        i += 1

# Funzione di salvataggio del grafico


def savegraph(title):
    plt.title(title, fontsize=20)
    plt.legend(fontsize=20)
    plt.savefig('../assets/tampscont.png', dpi=100, bbox_inches="tight")

# Funzione chiamante di addtext


def aggiungitesto(giorni, listascelte, listacolori):
    for s, c in zip(listascelte, listacolori):
        addtext(giorni, s, c)

# Salva le statistiche record in un file in assets


def main():

    # Apertura dei dati
    covid_file = open("dpc-covid19-ita-andamento-nazionale.csv", "r")
    covid_parser = csv.reader(covid_file, delimiter=",", quotechar='"')

    # Escludo la prima riga (cioè formato solo da descrizioni)
    alldays = list(covid_parser)[1:]

    # Salvo l'originale in caso possa servirmi dopo
    originaldays = copy.deepcopy(alldays)[-days:]
    # Elimino linee vuote eventuali
    originaldays = [h for h in originaldays if len(h) != 0]

    # Lista giorni
    listadati = dayperday(alldays)[-days:]  # Rimuovo la cumulazione dai dati
    # Elimino linee vuote eventuali
    listadati = [h for h in listadati if len(h) != 0]
    # Creo una lista da cui ricavare i giorni interessati
    giornocasi = [h[0] for h in listadati][-days:]
    # Rimuovo l'ora e l'anno dalle date
    removehourandyear(giornocasi)

    # Liste di dati
    # Lista nuovi contagiati per giorno, non uso cumulazione poichè il dato è già giornaliero nel csv
    contxday = [int(h[7])if h[7] else 0 for h in originaldays]
    # Lista tamponi per giorno
    tampxday = [int(h[12]) if h[12] else 0 for h in listadati]

    # Creazioni Serie

    contseries = pd.Series(data=contxday, index=giornocasi)
    tampseries = pd.Series(data=tampxday, index=giornocasi)
    # Inserisco stile
    plt.style.use('dark_background')
    plt.figure(figsize=(21, 10))
    # Lista delle serie che voglio vedere nel grafico
    listaseriescelte = [contseries, tampseries]
    # Lista dei colori per ogni serie, in ordine
    listacolori = ["orange", "brown"]

    # Grafico a linee
    tampseries.plot.bar(color="brown", label="Tamponi")
    contseries.plot.bar(color="orange", label="Contagi")
    # Aggiungo testo e mostro grafico
    aggiungitesto(giornocasi, listaseriescelte, listacolori)
    datatoday = listadati[-1][0].split("T")[0]
    oratoday = listadati[-1][0].split("T")[1]
    savegraph("Grafico variazione contagi/tamponi per giorno (aggiornato al {})".format(datatoday + " " + oratoday))
    return


main()
