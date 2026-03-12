import random
print(20*'-=')
print('JOGO DA FORCA!!')
print(20*'-=')

j = str(input('\nJogar jogo da forca? (sim ou não)'))
if j == 'sim':
    e = str(input('\nEscolha uma categoria: Animal ou Comida?'))
    e = e.upper()

else:
    print('\nQue pena! Até mais!')

if e == 'ANIMAL':
    a1 = 'Jacaré'
    a2 = 'Cobra'
    l = [a1, a2]
    al = random.choice(l)
    pal = al.replace(al, '_'*len(al))
    print(pal)
