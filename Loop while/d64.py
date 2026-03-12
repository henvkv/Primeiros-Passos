cont = soma = 0

while True:
    numero = int(input('Digite um número [999 PARA PARAR]: '))
    if numero == 999:
        print(f'\nVocê digitou {cont} números e a soma entre eles foi {soma}.')
        break
    soma += numero
    cont += 1
