import random
from datetime import datetime

s = open("scelte.txt","r").read().splitlines()
input("- Premi invio per generare -\n")

while True:
    adesso = datetime.now()
    oggi = adesso.strftime("%Y-%m-%d")
    ora = adesso.strftime("%H:%M:%S")
    x = random.choice(s)
    print(ora,">",x)
    with open("log/" + oggi + ".txt","a") as log:
        log.writelines("\n" + ora + " > " + x)
        log.close()
    input("")
