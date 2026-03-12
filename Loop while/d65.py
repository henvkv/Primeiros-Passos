loop = cont = maior = menor = 0
soma = float(0)

while loop >= 0:
    numero = int(input('Digite um número: '))
    continuar = str(input('Você quer continuar? [S/N]: ')).upper()
    print('')

    cont += 1
    soma += numero

    if cont == 1:
        maior = menor = numero 
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    
    if continuar == 'N':
        print(f'Você digitou {cont} números e a media {soma/cont:.2f}')
        print(f'O maior valor foi {maior} e o menor foi {menor}')
        break