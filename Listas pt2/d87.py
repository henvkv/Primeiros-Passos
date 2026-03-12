matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = 0
par = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        maior = matriz[1][0]
        
        for n in range(0,3):
            if maior < matriz[1][n]:
                maior = matriz[1][n]
        
        soma += matriz[l][2]
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]

print()
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'''\nSoma dos números pares: {par}
A soma dos valores da terceira coluna é: {soma}
O maior numero da segunda linha é: {maior}''')