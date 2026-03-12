import random
from time import sleep

print('')
print(20*'=','JOGO DO JOKENPÔ',20*'=')

print('''\n[1]COMEÇAR
[2]SAIR''')

r = int(input('ESCOLHA A SUA OPÇÃO: '))

if r == 1:
    
    lj = ['PEDRA', 'PAPEL', 'TESOURA']
    ec = random.choice(lj)

    print('')
    print(20*'=','''Escolha entre:''',20*'=')

    print('''\n[1]PEDRA
[2]PAPEL
[3]TESOURA''')

    e = input('DIGITE A SUA ESCOLHA: ')

    e1 = '1'
    e2 = '2'
    e3 = '3'

    pdr = e1.replace('1', 'PEDRA')
    pap = e2.replace('2', 'PAPEL')
    tes = e3.replace('3', 'TESOURA')

    print('')
    print('JO')
    sleep(0.75)
    print('KEN')
    sleep(0.75)
    print('PÔ!')

    if e == e1 and ec == 'PAPEL':
        print('')
        print(20*'=','VOCÊ PERDEU, JOGUE NOVAMENTE!',20*'=')
        print('')

    elif e == e1 and ec == 'TESOURA':
        print('')
        print(20*'=','VOCÊ GANHOU, PARABÉNS!',20*'=')
        print('')

    elif e == e2 and ec == 'TESOURA':
        print('')
        print(20*'=','VOCÊ PERDEU, JOGUE NOVAMENTE!',20*'=')
        print('')

    elif e == e2 and ec == 'PEDRA':
        print('')
        print(20*'=','VOCÊ GANHOU, PARABÉNS!',20*'=')
        print('')

    elif e == e3 and ec == 'PEDRA':
        print('')
        print(20*'=','VOCÊ PERDEU, JOGUE NOVAMENTE!',20*'=')
        print('')

    elif e == e3 and ec == 'PAPEL':
        print('')
        print(20*'=','VOCÊ GANHOU, PARABÉNS!',20*'=')
        print('')

    elif pdr or pap or tes == ec:
        print('')
        print(20*'=','EMPATE, JOGUE NOVAMENTE!',20*'=')
        print('')

elif r == 2:
    print('')
    print(20*'=','JOGUE QUANDO QUISER, ATÉ MAIS!',20*'=')
    print('')
