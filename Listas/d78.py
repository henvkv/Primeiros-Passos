valores = []

for v in range(0,5):
    valores.append(int(input('Digite um valor: ')))

menor = maior = valores[0]

for var in valores:
    if var > maior:
        maior = var

    elif var < menor:
        menor = var

print('='*30)

print(f'\nVocê digitou os valores: {valores}')
print(f'O maior valor digitado foi o número {maior} na(s) posições:', end=' ')
for i, v in enumerate(valores, start=1):
    if v == maior:
        print(f'{i} ', end='')
print()

print(f'O menor valor digitado foi o número {menor} na(s) posições:', end=' ')
for i, v in enumerate(valores, start=1):
    if v == menor:
        print(f'{i} ', end='')
print()