dados = dict()
lista_de_dados = list()
mulheres = dict()
acima_da_media = dict()
soma_idade = 0

while True:
    nome = str(input('\nNome: '))
    dados['nome'] = nome

    sexo = str(input('Sexo [M/F]: ')).upper()
    dados['sexo'] = sexo
    if sexo == 'F':
        mulheres['mulheres'] = nome

    idade = int(input('Idade: '))
    soma_idade += idade
    dados['idade'] = idade

    lista_de_dados.append(dados.copy())
    dados.clear()

    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Resposta inválida. Deseja continuar? [S/N]: ')).upper()

    if continuar == 'N':
        print(f'''\n- O grupo tem {len(lista_de_dados)} pessoas.
- A média de idade é de {soma_idade/len(lista_de_dados):.2f}
- As mulheres cadastradas foram: {mulheres["mulheres"] if len(mulheres) == 1 else 'Nenhuma mulher cadastrada'}''')
        
        print(f'''\nLista de pessoas acima da média:''')
        for d in range(0, len(lista_de_dados)):
            if lista_de_dados[d]['idade'] > soma_idade/len(lista_de_dados):
                acima_da_media['Acima da média'] = lista_de_dados[d]
                print(acima_da_media['Acima da média'])
        print('\nPROGRAMA ENCERRADO!')

        break