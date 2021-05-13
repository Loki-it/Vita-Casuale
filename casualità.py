import random
from datetime import datetime

adesso = datetime.now()
ora = adesso.strftime("%H:%M:%S")
s = open("scelte.txt","r").read().splitlines()

input("- Premi invio per generare -\n")
while True:
    print(ora,">",random.choice(s))
    input("")