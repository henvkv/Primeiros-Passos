maior = 0
menor = 0

for pessoas in range(1, 6):
    pesos = float(input('Digite o {}º peso: '.format(pessoas)))
    if pessoas == 1:
        maior = pesos
        menor = pesos
    else:
        if pesos > maior:
            maior = pesos
        if pesos < menor:
            menor = pesos

print('\nO maior peso é {:.2f}Kg e o menor é {:.2f}Kg.'.format(maior, menor))
