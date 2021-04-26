import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def filter_date(dataframe):
    fixeddate = []

    for h in dataframe.index:
        h = h.split('T')[0]
        (year, month, day) = h.split('-')
        h = year + "-" + month + "-" + day
        fixeddate.append(h)

    # Sostituisco l'indice con i nuovi dati
    dataframe.index = fixeddate
    return


dataframe = pd.read_csv(
    "dpc-covid19-ita-andamento-nazionale.csv", sep=",", index_col=0)[-1:]
filter_date(dataframe)

plt.style.use("dark_background")

fig, axes = plt.subplots(1, 2)
fig.set_size_inches(19.2, 10.8)

#Riempio le variabili che mi interessano
totale_tamponi = int(dataframe.tamponi)
totale_casi = int(dataframe.totale_casi)
totale_noncasi = totale_tamponi - totale_casi
totale_deceduti = int(dataframe.deceduti)
totale_nondeceduti = totale_casi - totale_deceduti


# Creo primo grafico
axes[0].set_title("Rapporto decessi e numero totale di casi registrati " +
                  str(dataframe.index.values), fontsize=15)
axes[0].pie([totale_deceduti, totale_nondeceduti], labels=["Deceduti\n" + "[" + str(totale_deceduti) + "]", "Guariti\n" + "[" +
                                                   str(totale_nondeceduti) + "]"], colors=["#280680", "#00b248"], textprops={'fontsize': 20})

# Creo secondo grafico
axes[1].set_title("Rapporto casi totali registrati su numero di tamponi effettuati " +
                  str(dataframe.index.values), fontsize=15)
axes[1].pie([totale_casi, totale_noncasi], labels=["Positivi\n" + "[" + str(totale_casi) + "]", "Negativi\n" + "[" +
                                                   str(totale_noncasi) + "]"], colors=["#8e0000", "#002984"], textprops={'fontsize': 20})

fig.savefig("../assets/pieratio.png", dpi=100)

