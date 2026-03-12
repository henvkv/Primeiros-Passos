print('-'*30)
print('SEQUÊNCIA DE FIBONNACI')
print('-'*30)

numero = int(input('Digite um número: '))
termo1 = 0
termo2 = 1
termo3 = termo1 + termo2
cont = 3
print('')

print(f'{termo1} -> {termo2} -> ', end='')

while cont <= numero:
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    cont += 1
    print(f'{termo3}', end=' -> ')
print('FIM!', end= '')