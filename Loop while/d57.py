sexo = str(input('Digite o seu sexo [M/F]: ')).upper()

while sexo != 'M' or 'F':
    sexo = str(input('Digite o seu sexo novamente [M/F]: ')).upper()
    if sexo == 'M':
        print('\nO seu sexo é o MASCULINO!')
        break
    if sexo == 'F':
        print('\nO seu sexo é o FEMININO!')
        break

print('MUITO OBRIGADO(A)!')