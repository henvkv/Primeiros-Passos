import random
from time import sleep

valores = dict()

for j in range(1, 5):
    valores[f'jogador{j}'] = random.randint(1, 6)

valores_ordenado = dict(sorted(valores.items(), key=lambda item: item[1], reverse=True))

print('Valores sorteados:')
for k, v in valores.items():
    print(f'O {k} tirou o número {v}!')
    sleep(1)

print('\nRanking dos jogadores:')

for l in range(1,5):
    print(f'{l}º Lugar:', end='')

for k, v in valores_ordenado.items():
    print(f'{k} com {v}')