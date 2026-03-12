import random
numeros = tuple(random.choices(range(1,10), k=5))
maior = menor = numeros[0]

print('='*30)
print('VALORES SORTIDOS'.center(30))
print('='*30)

print(f'\nO valores sorteados foram: ', end='')

for num in numeros:
    print(f'{num} ', end='')

for n in numeros[1:]:
    if n > maior:
        maior = n

    elif n < menor:
        menor = n

print(f'\n\nO maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')