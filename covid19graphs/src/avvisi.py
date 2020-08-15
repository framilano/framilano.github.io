import os

#Moving avvisi.md knowing that the COVID-19 repo has already been pulled
os.system ("cp /home/francesco/Documents/GithubRepos/COVID-19/avvisi.md /home/francesco/Documents/GithubRepos/framilano.github.io/covid19graphs/src")
avvisi = open("avvisi.md", "r")
#Opening the previous saved message
avviso_odierno = open("../assets/avviso_odierno.txt", "r")
#Date saved on the previous alert
data_vecchio_avviso = avviso_odierno.readline().replace("\n", "")
messaggio = ""
data_ultimo_avviso = ""

for indice, linea in enumerate(avvisi.readlines()):
        if ("## Avvisi" in linea):
            avvisi.seek(0)
            data_ultimo_avviso = avvisi.readlines()[indice + 1].replace("<b>", "").replace("</b>", "").replace("<br>", "").replace("\n", "")
            avvisi.seek(0)
            messaggio = avvisi.readlines()[indice + 2].replace("\n", "")
            break

if (data_vecchio_avviso != data_ultimo_avviso): 
    avviso_odierno = open("../assets/avviso_odierno.txt", "w")
    avviso_odierno.write(data_ultimo_avviso+"\n"+messaggio)
    msg_formattato = "*"+ data_ultimo_avviso + "*" + "\n" + messaggio
    os.system("telegram-send --format markdown " + "\"" + msg_formattato + "\"")
    
avviso_odierno.close()
avvisi.close()
