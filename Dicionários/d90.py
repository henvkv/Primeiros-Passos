ficha = dict()

ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input('Média: '))

print(f'\nO {ficha['nome']} tem média {ficha['media']}.')

if ficha['media'] < 7:
    print('Aluno reprovado!')
else:
    print('Aluno Aprovado!')