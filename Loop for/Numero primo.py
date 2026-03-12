numero = int(input('Digite o numero: '))
print('')
total = 0

for primo in range(1, numero+1):
    if numero % primo == 0:
        total += 1

if total == 2:
    print('O número {} é um número primo!'.format(numero))
else:
    print('O número {} não é um número primo!'.format(numero))