print(20*'=','LOJAS DO FULANO',20*'=')

v = float(input('\nTotal das compras: R$'))
print('')
print(20*'=','''Escolha uma forma de pagamento''',20*'=')
print('''\n[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão (Juros de 20%)''')

e = int(input('\nDigite a sua escolha: '))

e1 = 1
e2 = 2
e3 = 3
e4 = 4

if e == e1:
    d = v*0.10
    r = v-d
    print('\nSua compra de R${:.2f} vai custar R${:.2f} agora!'.format(v, r))

elif e == e2:
    d = v*0.05
    r = v-d
    print('\nSua compra de R${:.2f} vai custar R${:.2f} agora!'.format(v, r))

elif e == e3:
    d = v/2
    print('\nSeu parcelamento de R${:.2f} fica em 2x de R${:.2f}!'.format(v, d))

elif e == e4:
    p = int(input('Quantidade de parcelas: ')) 
    j = v*0.2
    rj = v+j
    vp = rj/p 
    print('\nO valor do produto com juros do parcelamento é R${:.2f}!'.format(rj))
    print('O valor da parcela em {}x será de R${:.2f}!'.format(p, vp))
