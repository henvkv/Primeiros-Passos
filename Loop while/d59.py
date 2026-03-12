numero1 = float(input('Digite o 1º número: '))
numero2 = float(input('Digite o 2º número: '))

while True:
    print('')
    print(20*'-=')
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair''')
    print(20*'-=')

    escolha = int(input('\nEscolha a sua opção: '))

    if escolha == 1:
        print(f'A soma entre {numero1} + {numero2} = {numero1 + numero2}!')

    elif escolha == 2:
        print(f'A multiplicação entre {numero1} x {numero2} = {numero1*numero2}')

    elif escolha == 3:
        if numero1 < numero2:
            print(f'O maior número é o {numero2}!')
        elif numero1 > numero2:
            print(f'O maior número é o {numero1}!')

    elif escolha == 4:
        numero1 = float(input('Digite o 1º número: '))
        numero2 = float(input('Digite o 2º número: '))

    elif escolha == 5:
        print('OBRIGADO POR TESTAR! VOLTE SEMPRE!')
        break

    else:
        print('Opcção inválida. Tente novamente!')


