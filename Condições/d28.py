import random
l = [0, 1, 2, 3, 4, 5]
e = random.choice(l)
n = int(input('Qual foi o numero escolhido pelo computador?'))
if n == e:
    print('\nO número {} foi o escolhido! Você venceu!'.format(n))
else:
    print('\nO número {} não foi o escolhido! Você perdeu!'.format(n))
