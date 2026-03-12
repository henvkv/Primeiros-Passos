v = int(input('Qual a velocidade do carro?'))
m = (v-80)*7
if v > 80:
    print('\nVocê foi multado por alta velocidade!\n\nSua velocidade: {}Km/h\nValor a pagar: R${}'.format(v, m))
else:
    print('\nPARABÉNS! Você não foi multado! Sua velocidade: {}Km/h'.format(v))
