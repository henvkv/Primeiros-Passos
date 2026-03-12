a = int(input('Insira um ano qualquer:'))
b = a % 4
if b == 0:
    print('O ano {} é um ano BISSEXTO!'.format(a))
else:
    print('O ano {} não é um ano BISSEXTO!'.format(a))
