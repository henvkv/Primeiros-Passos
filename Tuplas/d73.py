classificacao = ('Palmeiras', 'São Paulo', 'Corinthians', 'Bahia', 'Fluminense',
                 'Athletico-PR', 'Bragantino', 'Grêmio', 'Chapecoense', 'Mirassol')

print('='*30)
print('BRASILEIRÃO SERIE A'.center(30))
print('='*30)

while True:
    print('''Escolha entre: 
\n[1] 5 Primeiros colocados
[2] 4 Últimos colocados
[3] Em ordem alfabética
[4] Chapecoense''')
    
    escolha = int(input('Digite a sua escolha: '))
    if escolha < 1 or escolha > 5:
        escolha = int(input('Tente novamente. Digite a sua escolha: '))

    elif escolha == 1:
        print(f'\nOs 5 primeiros times são {classificacao[0:5]}')
        break

    elif escolha == 2:
        print(f'\nOs 4 últimos times são {classificacao[-4:10]}')
        break

    elif escolha == 3:
        print(f'\nTimes em ordem alfabética: {sorted(classificacao)}')
        break

    elif escolha == 4:
        print(f'\nA Chapecoense está em {classificacao.index('Chapecoense')+1}º na tabela!')
        break