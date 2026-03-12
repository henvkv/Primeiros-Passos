numero = int(input('Digite um número: '))
total = 1
numero1 = numero
print(f'\n{numero1}! = ', end='')

while numero > 0:
    print(f'{numero}', end=' ')
    print('x ' if numero > 1 else f'= {total}', end='')
    total = total*numero
    numero = numero - 1
