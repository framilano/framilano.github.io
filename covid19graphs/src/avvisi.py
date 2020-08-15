import os

avvisi = open("avvisi.md", "r")
avviso_odierno = open("../assets/avviso_odierno.txt", "r")

messaggio = ""
data_vecchio_avviso = avviso_odierno.readline().replace("\n", "")
data_ultimo_avviso = ""

for indice, linea in enumerate(avvisi.readlines()):
        if ("## Avvisi" in linea):
            avvisi.seek(0)
            data_ultimo_avviso = avvisi.readlines()[indice+1].replace("<b>", "").replace("</b>", "").replace("<br>", "").replace("\n", "")
            avvisi.seek(0)
            messaggio = avvisi.readlines()[indice+2].replace("\n", "")

if (data_vecchio_avviso == data_ultimo_avviso): 
    avviso_odierno.close()
    avvisi.close()
    exit()
else :
    avviso_odierno = open("../assets/avviso_odierno.txt", "w")
    avviso_odierno.write(data_ultimo_avviso+"\n"+messaggio)
    avviso_odierno.close()
    avvisi.close()
    msg_formattato = "*"+ data_ultimo_avviso + "*" + "\n" + messaggio
    os.system("telegram-send --format markdown " + "\"" + msg_formattato + "\"")
    
