import random
from time import sleep

valores = dict()

for j in range(1, 5):
    valores[f'jogador{j}'] = random.randint(1, 6)

ranking = sorted(valores.items(), key=lambda item: item[1], reverse=True)

print('Valores sorteados:')
for k, v in valores.items():
    print(f'O {k} tirou o número {v}!')
    sleep(1)

print('\nRanking dos jogadores:')

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com o número {v[1]}')