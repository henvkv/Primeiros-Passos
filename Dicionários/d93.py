# APROVEITAMENTO DE UM JOGADOR DE FUTEBOL
dados = dict()
gols = list()
soma = 0

dados['nome'] = str(input('Nome do jogador: '))

partidas = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
print('-'*40)

for g in range(1, partidas+1):
    num_gols = int(input(f'Números de gols na {g}º partida: '))
    soma += num_gols
    gols.append(num_gols)

dados['gols'] = gols
dados['total'] = num_gols

print('-'*40)
print(f'{dados["nome"]} jogou {partidas} partidas.')

for i, v in enumerate(gols):
    print(f'=> Na partida {i+1}, fez {v} gols!')
print('-'*40)

print(f'No total {dados['nome']} fez {soma} gols.')