numeros = []

while True:
    numero = int(input('\nDigite um valor: '))
    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor repetido! Valor não adicionado.')
    
    continuar = str(input('Quer continuar? [S/N]: ')).upper()

    if continuar == 'N':
        numeros.sort()
        print('='*30)
        print()
        print(f'Você digitou os valores: {numeros}')
        break

    else:
        numeros.sort()

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper()