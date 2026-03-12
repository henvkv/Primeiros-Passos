import random
from time import sleep

print('='*15, f'JOGO DA MEGA SENA', '='*15)

quantidade = int(input('\nQuantos jogos você quer sortear? '))
print()

print('='*15, f'SORTEANDO {quantidade} JOGOS', '='*15)

for n in range(0,quantidade):
    jogos = [random.randint(1,60) for _ in range(6)]
    sleep(1)
    print(f'Jogo {n+1}: {jogos}')
    jogos.clear()
    