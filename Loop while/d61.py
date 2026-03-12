numero = int(input('Digite o seu número: '))
razao = int(input('Digite a sua razão: '))
print('')

decimo = numero+(10+1)*razao

while numero < decimo:
    print(numero, end=' -> ')
    numero += razao
print('FIM!')