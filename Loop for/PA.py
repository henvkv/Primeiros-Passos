numero = int(input('Digite o seu número: '))
razao = int(input('Digite a razão: '))
decimo = numero+(10+1)*razao

for pa in range(numero, decimo, razao):
    print('{} '.format(pa),end='-> ')
print('ACABOU')

