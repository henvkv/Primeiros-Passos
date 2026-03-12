maior = 0
menor = 0

for pessoa in range(1,8):
    ano = int(input('Dgite o {}º ano: '.format(pessoa)))
    idade = 2026-ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('')
print('Existem {} pessoas de maior. '.format(maior), end='')
print('Existem também {} pessoas de menor.'.format(menor))

