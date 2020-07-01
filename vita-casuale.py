import random
import pandas as pd

l = []
for line in pd.read_csv('./scelte.csv', encoding='utf-8', header=None, chunksize=1):
    l.append(line.iloc[0,0])

s = pd.read_csv('scelte.csv')
righe = len(s)

# Numero di elementi
r = random.randrange(righe)
print('Devi', l[r])
# -- Se vuoi inserire anche il tempo --
# print('Devi', l[r], 'per', random.randrange(30), 'minuti')
input("Premi invio per iniziare questa attività")
