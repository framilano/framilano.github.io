import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#modifica questa variabile per visualizzare gli ultimi n giorni
days = 30

def filter_date(dataframe):
    fixeddate = []

    for h in dataframe.index:
        h = h.split('T')[0]
        (year, month, day) = h.split('-')
        h = month + "-" + day
        fixeddate.append(h)

    # Sostituisco l'indice con i nuovi dati
    dataframe.index = fixeddate
    return

def add_text_overbar(dataframe, title, color, offset, ax):
    for i, v in enumerate(dataframe[title]):
        ax.text(i, offset * max(dataframe[title]), str(v), rotation=90, color=color, fontsize=15, ha='center')

def rotate_ticks(axes):
    for ax in axes:
        for tick in ax.get_xticklabels():
            tick.set_rotation(90)

def remove_cumulation(series):
    copylist = list(series)
    for i, n in enumerate(copylist):
        if (i == 0): continue
        copylist[i] = n - series[i-1]
    return copylist


def main():
    global days
    dataframe = pd.read_csv("dpc-covid19-ita-andamento-nazionale.csv", sep=",", index_col=0)
    #Passa una serie del dataframe, ne rimuoverà la cumulazione dei dati, non è in loco
    dataframe['tamponi'] = remove_cumulation(dataframe['tamponi'])
    dataframe['deceduti'] = remove_cumulation(dataframe['deceduti'])
    dataframe['dimessi_guariti'] = remove_cumulation(dataframe['dimessi_guariti'])
    dataframe = dataframe[-days:]

    # Rimuovo gli orari, tengo la data
    filter_date(dataframe)


    # tema nero
    plt.style.use('dark_background')

    # genero la figura e l'array a tre posizioni per i tre plot
    figure, axes = plt.subplots(4, 1)
    # x sono sempre i giorni
    x = dataframe.index

    # Sezione tamponi totali
    axes[0].set_title('Tamponi ogni giorno (ultimi 30 giorni)', fontsize=20)
    # Inserisco etichette per ogni barra
    add_text_overbar(dataframe, 'tamponi', "white", 1/7, axes[0])
    # axes[0] conterrà il primo grafico a barre
    axes[0].bar(x, dataframe['tamponi'], color="brown")

    # Sezione guariti
    axes[1].set_title('Dimessi guariti ogni giorno (ultimi 30 giorni)', fontsize=20)
    # Inserisco etichette per ogni barra
    add_text_overbar(dataframe, 'dimessi_guariti', "white", 1/7, axes[1])
    # axes[0] conterrà il primo grafico a barre
    axes[1].bar(x, dataframe['dimessi_guariti'], color="green")

    # Sezione deceduti
    axes[2].set_title('Decessi ogni giorno (ultimi 30 giorni)', fontsize=20)
    # Inserisco etichette per ogni barra
    add_text_overbar(dataframe, 'deceduti', "white", 1/7, axes[2])
    # axes[0] conterrà il primo grafico a barre
    axes[2].bar(x, dataframe['deceduti'], color="red")

    # Sezione deceduti
    axes[3].set_title('In terapia intensiva attualmente (ultimi 30 giorni)', fontsize=20)
    # Inserisco etichette per ogni barra
    add_text_overbar(dataframe, 'terapia_intensiva', "white", 1/7, axes[3])
    # axes[0] conterrà il primo grafico a barre
    axes[3].bar(x, dataframe['terapia_intensiva'], color="purple")

    #Ruoto le etichette sull'asse x in verticale
    rotate_ticks(axes)

    figure.set_size_inches(19.2, 10.8)  #Imposto 1920x1080
    figure.tight_layout(pad=3.0)
    figure.savefig("../assets/tampscontdeath.png", dpi=100)

main()
