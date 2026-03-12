soma = 0
cont = 0

for impares in range (1, 501, 2):
    if impares % 3 == 0:
        soma += impares
        cont += 1

print('O valor da soma dos {} multiplicadores é: {}'.format(cont, soma))