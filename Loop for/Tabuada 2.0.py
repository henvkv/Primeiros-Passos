numero = int(input('Digite um número: '))

print('')
print('A tabuada do {} é:'.format(numero))
print('')

for tabuada in  range(1,11):
    resultado = numero*tabuada
    print('{} x {} = {}'.format(numero, tabuada, resultado))