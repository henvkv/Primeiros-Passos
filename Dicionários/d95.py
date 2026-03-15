# DEFININDO AS LISTAS/DICIONARIOS/VARIAVEL 'SOMA'
dados = dict()
jogadores = list()
gols = list()
gols_feitos = list()
soma = 0

# ADICIONANDO AS VARIAVEIS AOS DADOS
while True:
    dados['nome'] = str(input('\nNome do jogador: '))

    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
    print('-'*40)

    for g in range(1, partidas+1):
        num_gols = int(input(f'Números de gols na {g}º partida: '))
        soma += num_gols
        gols.append(num_gols)
    
    dados['gols'] = gols
    dados['total'] = soma
    
    # APAGANDO OS DADOS E ADICIONANDO A LISTA DE DADOS
    gols_feitos.append(gols[:])
    jogadores.append(dados.copy())
    
    soma = 0
    dados.clear()
    gols.clear()
    
    # LOOP CONTINUAR
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()

    if continuar == 'N':
        print(f'{'\nNo.':<6}{'NOME':<30}{'GOLS':<20}{'TOTAL'}')
        print('-'*60)
        for n in range(0,len(jogadores)):
            print(f'{n+1:<6}{jogadores[n]['nome']:<30}{str(gols_feitos[n]):<20.20}{jogadores[n]['total']}')
        break

# EXIBINDO INFORMAÇÕES DETALHADAS DE CADA JOGADOR
while True:
    mostrar_dados = int(input(f'\nDigite o jogador de 1 a {len(jogadores)} (999 para parar): '))

    if mostrar_dados > len(jogadores) and mostrar_dados < 999:
        print('Jogador inexistente. Digite novamente!')

    elif mostrar_dados == 999:
        print(f'\nPROGRAMA ENCERRADO!')
        break
    
    else:
        print(f'\nLevantamento do jogador: {jogadores[mostrar_dados-1]['nome']}')
        for j, g in enumerate(gols_feitos[mostrar_dados-1]):
            print(f'No {j+1}º jogo {jogadores[mostrar_dados-1]['nome']} marcou: {g} gols')