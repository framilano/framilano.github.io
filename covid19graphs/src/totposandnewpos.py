import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#modifica questa variabile per visualizzare gli ultimi n giorni
days = 30

#Funzione che rimuove da un dataframe nel campo 'data' gli orari
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

def add_text_overbar(dataframe, title, color, offset, ax):
    for i, v in enumerate(dataframe[title]):
            ax.text(i-0.125, offset*max(dataframe[title]), str(v), rotation=90, color=color, fontsize=15)

def rotate_ticks(axes):
    for ax in axes:
        for tick in ax.get_xticklabels():
            tick.set_rotation(90)

def main():
    global days
    dataframe = pd.read_csv("dpc-covid19-ita-andamento-nazionale.csv", sep=",", index_col=0)

    # Rimuovo gli orari, tengo la data
    filter_date(dataframe)

    #tema nero
    plt.style.use('dark_background')

    #genero la figura e l'array a tre posizioni per i tre plot
    figure, axes = plt.subplots(3, 1)

    dataframe = dataframe[-days:]

    #x sono sempre i giorni
    x = dataframe.index

    #Sezione totale positivi
    axes[0].set_title('Totale positivi (ultimi 30 giorni)', fontsize=20)
    #Inserisco etichette per ogni barra
    add_text_overbar(dataframe, 'totale_positivi', "white", 1/20, axes[0])
    #axes[0] conterrà il primo grafico a barre
    axes[0].bar(x, dataframe['totale_positivi'], color="blue")

    #Sezione variazione positivi
    axes[1].set_title('Variazione positivi dal giorno precedente (ultimi 30 giorni)', fontsize=20)
    #Inserisco etichette per ogni barra
    add_text_overbar(dataframe, 'variazione_totale_positivi', "white", 4, axes[1])
    #axes[1] conterrà il secondo grafico a barre
    axes[1].bar(x, dataframe['variazione_totale_positivi'], color="red")

    #Sezione nuovi positivi per giorno
    axes[2].set_title('Nuovi positivi giornalieri (ultimi 30 giorni)', fontsize=20)
    #Inserisco etichette per ogni barra
    add_text_overbar(dataframe, 'nuovi_positivi', "white", 1/20, axes[2])
    #axes[2] conterrà il secondo grafico a barre
    axes[2].bar(x, dataframe['nuovi_positivi'], color="brown")

    #Ruoto le etichette sull'asse x in verticale
    rotate_ticks(axes)

    #Modifico le dimensioni della figura e salvo la figura
    figure.set_size_inches(19.2, 10.8)  #Imposto 1920x1080
    figure.tight_layout(pad=3.0)
    figure.savefig("../assets/totposandvariation.png", dpi=100)

    return


main()
