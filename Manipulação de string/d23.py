n = int(input('Digite um numero de 0 a 9999:'))
u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(20*'=')
print('Unidade: {}\n'.format(u))
print('Dezena: {}\n'.format(d))
print('Centena: {}\n'.format(c))
print('Milhar: {}\n'.format(m))
print(20*'=')
