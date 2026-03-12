print(20*'-=')
print('EMPRESTIMO BANCÁRIO!!')
print(20*'-=')
vc = float(input('\nQual é o valor da casa? R$'))
sc = float(input('Qual seu salario? R$'))
qa = float(input('Por quantos anos você vai pagar? '))
p = vc/(qa*12)
ex = sc*0.30
if p > ex:
    print('\nInfelizmente você não pode financiar esta casa!')
    print('O valor da prestação seria de: R${:.2f}'.format(p))
elif p <= ex:
    print('\nPARABÉNS!!Você tem a possibilidade de financiar esta casa!')
    print('O valor da prestação será de: R${:.2f}'.format(p))
