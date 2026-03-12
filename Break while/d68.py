import random

print('=-'*30)
print('JOGO PAR OU ÍMPAR')
print('=-'*30)
vencidas = 0

while True:
    valor_pensado = random.randint(1,10)
    valor = int(input('\nDigite um valor de 1 a 10: '))
    soma = valor+valor_pensado
    if valor > 10:
        print('')
        print('Tipo inválido. Inicie o programa novamente!')
        break
    escolha = str(input('Par ou ímpar? [P/I]: ')).upper()
    
    print('')
    print('-'*60)
    print(f'Você jogou {valor} e o computador {valor_pensado}. Total de {soma}',end=' ')
    
    if soma%2 == 0:
        soma = 'P'
        print('DEU PAR')
    else:
        soma = 'I'
        print('DEU ÍMPAR')
    
    print('-'*60)
    
    if soma == 'P' and escolha == 'I' or soma == 'I' and escolha == 'P':
        print('')
        print('=-'*30)
        print('Você PERDEU!')
        print(f'GAME OVER! Você ganhou {vencidas} vezes.')
        print('=-'*30)
        break

    elif soma == 'P' and escolha == 'P' or soma == 'I' and escolha == 'I':
        vencidas += 1
        print('')
        print('=-'*30)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-'*30)

    