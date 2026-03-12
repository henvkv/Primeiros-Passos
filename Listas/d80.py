valores = []

for v in range(0,5):
    valor = int(input('Digite um valor: '))
    
    if v == 0 or valor > valores[-1]:
        print('Valor adicionado ao final da lista!')
        valores.append(valor)

    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos, valor)
                print(f'Valor adiconado na posição: {pos}!')
                break
            pos += 1

print(f'\nVocê digitou os valores: {valores}')