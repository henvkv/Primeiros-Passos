import math
n = int(input('Digite um número qualquer:'))
print('\nEscolha uma das bases de conversão:\n'
      '[1] para Binário\n'
      '[2] para Octal\n'
      '[3] para hexadecimal')
ne = int(input('\nDigite sua opção:'))

if ne == 1:
    n1 = bin(n)
    print('\nO número {} com base binária é: {}'.format(n, n1))

if ne == 2:
    print('\nO número {} com base Octal é: {}'.format(n, oct(n)))

elif ne == 3:
    print('\nO número {} com base Hexadecimal é: {}'.format(n, hex(n)))
