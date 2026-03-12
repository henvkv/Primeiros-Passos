numero = int(input('Digite o seu número: '))
razao = int(input('Digite a sua razão: '))
numero1 = numero
print('')

decimo = numero+(10-1)*razao

while numero <= decimo:
    print(numero, end=' -> ')
    numero += razao
print('FIM!')

while True:
    continuar = int(input('\nQuantos números a mais você quer mostrar? \n'))
    print('')

    resultado = numero+(continuar-1)*razao

    if continuar != 0:
        while numero <= resultado:
            print(numero, end=' -> ')
            numero += razao
        print('FIM!')

    if continuar == 0:
        print('FIM DO PROGRAMA! VOLTE SEMPRE!')
        break
