ficha = list()

while True:
    nome = str(input('\nNome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2

    ficha.append([nome, media, [nota1, nota2]])

    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Resposta incorreta. Deseja continuar? [S/N]: '))

    if continuar == 'N':
        print(f'\n{'No.':<4}{'NOME':<30}{'MÉDIA':<5}')
        print('-'*45)
        for d in range(0,len(ficha)):
                print(f'{d+1:<4}{ficha[d][0]:<30.30}{ficha[d][1]:<5}')
        break
    
while True:
    nota = int(input(f'\nSelecione um aluno de 1 a {len(ficha)} para mostrar a nota (999 interrompe): '))

    if nota == 999:
            print('<'*3, 'VOLTE SEMPRE', '>'*3)
            break

    while nota > len(ficha) or nota < len(ficha) and nota < 999:
        print('Aluno não encontrado.')
        nota = int(input(f'\nSelecione um aluno de 1 a {len(ficha)} para mostrar a nota (999 interrompe): '))

    else:
        print(f'As Notas de {ficha[nota-1][0]} foi: {ficha[nota-1][2]}')
