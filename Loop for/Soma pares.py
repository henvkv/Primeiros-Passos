soma = 0
for numeros in range(1, 7):
    num = int(input('Digite um número:'))
    if num%2 == 0:
        soma += num
print('')
print('A soma dos valores pares é: {}!'.format(soma))