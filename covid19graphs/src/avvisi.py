import os
import datetime as dt


#Moving avvisi.md knowing that the COVID-19 repo has already been pulled
os.system ("cp ~/Documents/GithubRepos/COVID-19/avvisi.md ~/Documents/GithubRepos/framilano.github.io/covid19graphs/src")
avvisi = open("avvisi.md", "r")
#Opening the previous saved message
avviso_odierno = open("../assets/avviso_odierno.txt", "r")
#Date saved on the previous alert
data_vecchio_avviso = avviso_odierno.readline().replace("\n", "")

messaggio = ""
data_ultimo_avviso = ""

#Parsing the latest alert
for indice, linea in enumerate(avvisi.readlines()):
        if ("## Avvisi" in linea):
            avvisi.seek(0)
            data_ultimo_avviso = avvisi.readlines()[indice + 1].replace("<b>", "").replace("</b>", "").replace("<br>", "").replace("\n", "")
            avvisi.seek(0)
            messaggio = avvisi.readlines()[indice + 2].replace("\n", "")
            break
#Closing avvisi.md after parsing the latest alert
avvisi.close()

#If the the previous alert date and the new one are different, send a telegram message to the Telegram channel
if (data_vecchio_avviso != data_ultimo_avviso): 
    avviso_odierno.close()
    avviso_odierno = open("../assets/avviso_odierno.txt", "w")
    avviso_odierno.write(data_ultimo_avviso + "\n" + messaggio)
    msg_formattato = "*Avviso del " + data_ultimo_avviso + "*" + "\n" + messaggio
    os.system("telegram-send --format markdown " + "\"" + msg_formattato + "\"")
else :
    os.system("telegram-send \"Buona serata 🌙\"")

#Closing current alert after updating it
avviso_odierno.close()


#Logging (case of failure)
open("~/Documents/Logs/log_avvisicovid19.txt", "w").write(str(dt.datetime.today()) + "\n" + data_vecchio_avviso + "\n" + data_ultimo_avviso)