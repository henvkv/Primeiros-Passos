s = float(input('Digite o seu salário atual:'))
if s > 1250:
    sn = s*0.10+s
    print('\nO seu novo salário vai ser de: R${:.2f}!'.format(sn))
else:
    sn = s*0.15+s
    print('\nSeu novo salário vaiser de: R${:.2f}!'.format(sn))
