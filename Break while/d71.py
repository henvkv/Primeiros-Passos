print('='*30)
print('BANCO DOURADO'.center(30))
print('='*30)

cont = 0
    
sacar = int(input('\nDigite o valor para sacar: '))
print('')

while True:
    cel50 = int(sacar/50)
    qnt50 = cel50*50
    total50 = sacar-qnt50
    if qnt50 == sacar:
        print('='*30)
        print(f'Total de {cel50} notas de R$50.')
        print('='*30)
        break
    else:
        pass

    cel20 = int(total50/20)
    qnt20 = cel20*20
    total20 = total50-qnt20
    if qnt20 == total50:
        print('='*30)
        print(f'Total de {cel50} notas de R$50.')
        print(f'Total de {cel20} notas de R$20.')
        print('='*30)
        break
    else:
        pass

    cel10 = int(total20/10)
    qnt10 = cel10*10
    total10 = total20-qnt10
    if qnt10 == total20:
        print('='*30)
        print(f'Total de {cel50} notas de R$50.')
        print(f'Total de {cel20} notas de R$20.')
        print(f'Total de {cel10} notas de R$10.')
        print('='*30)
        break
    else:
        pass

    cel1 = int(total10/1)
    qnt1 = cel1
    total1 = total10-qnt1
    print('='*30)
    print(f'Total de {cel50} notas de R$50.')
    print(f'Total de {cel20} notas de R$20.')
    print(f'Total de {cel10} notas de R$10.')
    print(f'Total de {cel1} notas de R$1.')
    print('='*30)
    break

print('')
print('='*60)
print('Volte sempre ao BANCO DOURADO!'.center(60))
print('='*60)