dados = list()
pessoas = list()
maior = menor = 0
pesadas = list()
leves = list()

while True:
    dados.append(str(input('\nNome: ')))
    dados.append(float(input('Peso: ')))
    
    if len(pessoas) == 0:
        maior = menor = dados[1]
        pesadas.append(dados[0])
        leves.append(dados[0])
    else:
        if dados[1] > maior:
            maior = dados[1]
            pesadas.clear()
            pesadas.append(dados[0])
        elif dados[1] < menor:
            menor = dados[1]
            leves.clear()
            leves.append(dados[0])
        elif dados[1] == maior:
            pesadas.append(dados[0])
        elif dados[1] == menor:
            leves.append(dados[0])
    
    pessoas.append(dados[:])
    dados.clear()

    continuar = str(input('Você que continuar? [S/N]: ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Resposta inválida. Você que continuar? [S/N]: ')).upper()
    
    if continuar == 'N':
        print('='*30)
        print(f'''\nVocê cadastrou {len(pessoas)} pessoas.
O maior peso foi de {maior} Kg. Peso de {pesadas}
O menor peso foi de {menor} Kg. Peso de {leves}''')
        break