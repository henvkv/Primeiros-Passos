listagem = ('Lápis',1.75, 'Borracha',2, 'Caderno',15, 'Estojo',25,
            'Transferidor',4.20)

print('-'*33)
print('NOTA FISCAL'.center(30))
print('-'*33)

for p in range(0, 10):
    if p % 2 == 0:
        print(f'{listagem[p]:.<25}', end='')
    
    else:
        print('R$',float(listagem[p]))

print('-'*33)