somahomem = somamaior = somamulher = 0

while True:
    print('')
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    
    idade = int(input('Idade: '))
    if idade > 18:
        somamaior += 1
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper()
    if sexo == 'M':
        somahomem += 1
    elif idade < 20 and sexo == 'F':
        somamulher += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper()

    if continuar == 'S' or 'N':
        if continuar == 'N':
            print('')
            print('='*15,'FIM DO PROGRAMA','='*15)
            print('')

            print(f'''Total de pessoas +18: {somamaior}
Total de homens cadastrados: {somahomem}
Total de mulheres com -20 anos: {somamulher}''')
            break
        
        elif continuar == 'S':
            pass