print('-'*45)
print(' '*10, 'LOJA SUPER BARATÃO', ' '*10)
print('-'*45)
total = contmil = menorp = cont = 0
barato = ' '

while True:
    
    print('')
    nome = str(input('Nome do produto: ')).upper()
    preco = int(input('Preço: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        contmil += 1
      
    if cont == 1 or preco < menorp:
        menorp = preco
        barato = nome

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper()

    if continuar == 'N':
        print('')
        print('-'*15, 'FIM DO PROGRAMA', '-'*15)
        print('')
        print(f'''Total da compra: R${total}
Produtos mais de R$1000: {contmil}
Produto mais barato foi {barato} que custou R${menorp}''')
        break