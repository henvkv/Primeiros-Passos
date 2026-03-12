n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))
n3 = float(input('Digite o terceiro número:'))
m = n2
mm = n1
if n2 < n1 and n2 < n3:
    mm = n2
if n3 < n1 and n3 < n2:
    mm = n3
if n1 > n2 and n1 > n3:
    m = n1
if n3 > n1 and n3 > n2:
    m = n3
print('\nO menor valor digitado foi: {}'.format(mm))
print('O maior número digitado foi: {}'.format(m))
