# IMPORT
from time import sleep

# FUNÇÃO
def contador(inicio, fim, passo):
    if passo <= 0:
        passo = 1
        while inicio <= fim:
            print(f'{inicio} ', end='')
            inicio += passo
            sleep(0.25)
    while inicio > fim:
        print(f'{inicio} ',end='')
        inicio -= passo
        sleep(0.25)
    while inicio <= fim:
        print(f'{inicio} ', end='')
        inicio += passo
        sleep(0.25)
    print()

def mensagem(txt):
    print()
    print('-='*30)
    print(f'{txt}'.center(30))

# EXECUTANDO CODIGO
mensagem('Contagem de 1 até 10 de 1 em 1:')
contador(1,10,1)

mensagem('Contagem de 10 até 0 de 2 em 2:')
contador(10,0,2)

mensagem('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo <= 0:
    passo = 1

mensagem(f'Contagem de {inicio} até {fim} de {passo} em {passo}!')
contador(inicio, fim, passo)