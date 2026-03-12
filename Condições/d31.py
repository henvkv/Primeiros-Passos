d = int(input('Qual é a distancia da sua viagem?'))
if d <= 200:
    p = 0.50*d
    print('\nO preço da sua passagem irá custar: R${}'.format(p))
else:
    p = 0.45*d
    print('\nO preço da sua passagem irá custar: R${}'.format(p))
