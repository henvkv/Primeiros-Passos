dados = dict()
lista_de_dados = list()
mulheres = list()
acima_da_media = list()
soma_idade = 0

while True:
    nome = str(input('\nNome: '))
    dados['nome'] = nome

    sexo = str(input('Sexo [M/F]: ')).upper()
    if sexo == 'F':
        mulheres.append(nome)
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper()
    dados['sexo'] = sexo

    idade = int(input('Idade: '))
    soma_idade += idade
    media = soma_idade/len(lista_de_dados)
    dados['idade'] = idade

    lista_de_dados.append(dados.copy())
    dados.clear()

    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Resposta inválida. Deseja continuar? [S/N]: ')).upper()

    if continuar == 'N':
        print(f'''\n- O grupo tem {len(lista_de_dados)} pessoas.
- A média de idade é de {media:.2f}
- As mulheres cadastradas foram:''', end=' ')
        if len(mulheres) >= 1:
            for m in mulheres:
                print(m, end=' ')
        else:
            print('Nenhuma mulher cadastrada!', end='')
        
        print(f'''\n\nLista de pessoas acima da média:''')
        for d in range(0, len(lista_de_dados)):
            if lista_de_dados[d]['idade'] > media:
                acima_da_media.append(lista_de_dados[d])
                for p in acima_da_media:
                    print(p['nome'])
            else:
                print('Não existem pessoas acima da média!')
        print('\nPROGRAMA ENCERRADO!')
        break