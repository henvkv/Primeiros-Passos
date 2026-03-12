import random
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
a = [a1, a2, a3, a4]
e = random.choice(a)
print('Os alunos escolhidos foram: {}!'.format(e))
