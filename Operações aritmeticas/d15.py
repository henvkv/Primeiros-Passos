d = int(input('Quantos dias alugado?'))
k = float(input('Quantos Kms percorridos?'))
dx = d*60
kx = k*0.15
print('Preço a ser pago: R${:.2f}!'.format(dx+kx))
