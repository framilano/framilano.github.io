import os
import datetime as dt

def remove_emptylines(avvisi):
    new_avvisi = ""
    for line in avvisi.readlines():
        if (line == "\n"): continue
        else: new_avvisi += line
    return new_avvisi


#Moving avvisi.md knowing that the COVID-19 repo has already been pulled
os.system ("cp ~/Documents/GithubRepos/COVID-19/avvisi.md ~/Documents/GithubRepos/framilano.github.io/covid19graphs/src")
avvisi = open("avvisi.md", "r")
#Opening the previous saved message
avviso_odierno = open("../assets/avviso_odierno.txt", "r")
#Date saved on the previous alert
data_vecchio_avviso = avviso_odierno.readline().replace("\n", "")

messaggio = ""
data_ultimo_avviso = ""

avvisi_string = remove_emptylines(avvisi)

#Parsing the latest alert
for indice, linea in enumerate(avvisi_string.splitlines()):
        if ("## Avvisi" in linea):
            data_ultimo_avviso = avvisi_string.splitlines()[indice + 1].replace("<b>", "").replace("</b>", "").replace("<br>", "").replace("\n", "")
            messaggio = avvisi_string.splitlines()[indice + 2].replace("\n", "")
            break


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


# Logging (case of failure)
# Defining log dir
# os.path.expanduser(path)
# On Unix and Windows, return the argument with an initial component of ~ or ~user replaced by that user’s home directory.
# On Unix, an initial ~ is replaced by the environment variable HOME if it is set; otherwise the current user’s home 
# directory is looked up in the password directory through the built-in module pwd. An initial ~user is looked up directly in the password directory.
log_dir = os.path.expanduser("~/Documents/Logs/log_avvisicovid19.txt")
open(log_dir, "w").write(str(dt.datetime.today()) + "\nMessaggio: {}\nVecchio: {}\nNuovo: {}\n".format(messaggio, data_vecchio_avviso, data_ultimo_avviso))