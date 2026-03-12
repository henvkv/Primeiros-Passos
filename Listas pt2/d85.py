numeros = [[], []]

for v in range(0,7):
    numero = int(input(f'Digite o {v+1}º número: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
        numeros[0].sort()
    else:
        numeros[1].append(numero)
        numeros[1].sort()

print(f'''\nNúmeros pares: {numeros[0]}
Números ìmpares: {numeros[1]}''')