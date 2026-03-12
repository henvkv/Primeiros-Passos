n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))

if n1 > n2:
    print('O PRIMEIRO é o número maior!'.format(n1))

elif n2 > n1:
    print('O SEGUNDO é o número maior!'.format(n2))

elif n1 == n2:
    print('Os dois números são iguais!')
