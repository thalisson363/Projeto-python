from random import randint
from operator import itemgetter
import time
sort = {}


sort[f'jogador1'] = randint(1,6)
sort[f'jogador2'] = randint(1,6)
sort[f'jogador3'] = randint(1,6)
sort[f'jogador4'] = randint(1,6)
print('Jogadores sorteados:')
rankin = list()
for k,v in sort.items():
    print(f'{k}: {v}')
    time.sleep(0.98)
rankin = sorted(sort.items(), key=itemgetter(1),reverse=True)

print('Ranking dos sorteados:')
for i,v in enumerate(rankin):
 print(f'{i+1}º {v[0]} com {v[1]}')


 




 