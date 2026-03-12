print(20*'-=')
print('CALCULADORA DE MÉDIA!!')
print(20*'-=')
n1 = float(input('Digite a nota do aluno:'))
n2 = float(input('Digite a outra nota do aluno:'))

m = (n1+n2)/2

if m < 5:
    print('\nO aluno está REPROVADO! Sua média foi: {}!'.format(m))

elif m >= 5 and m < 7:
    print('\nO aluno está de RECUPERAÇÃO! Sua média foi: {}!'.format(m))

elif m >= 7:
    print('\nO aluno foi APROVADO! Sua média foi: {}'.format(m))
