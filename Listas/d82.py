numeros = []
pares = []
impares = []

while True:
    numero = numeros.append(int(input('\nDigite um número: ')))

    continuar = str(input('Você deseja continuar? [S/N]: ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Resposta inválida. Você deseja continuar? [S/N]: ')).upper()

    if continuar == 'N':
        for n in numeros:
            if n%2 == 0:
                pares.append(n)
            else:
                impares.append(n)
        print('='*30)
        print(f'''\nNúmeros: {numeros}
Números pares: {pares}
Números ímpares: {impares}''')
        break

    
