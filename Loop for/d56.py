soma = 0
homemv = 0
nomehv = ''
mme = 0

for dados in range(1,5):  
    nome = str(input('\nDigite o nome da {}º pessoa: '.format(dados)))
    idade = int(input('Digite qual a idade da {}º pessoa: '.format(dados)))
    sexo = str(input('Digite o sexo(F/M) da {}º pessoa: '.format(dados)))

    soma += idade
    media = soma/4

    if dados == 1 and sexo in 'Mm':
        homemv = idade
        nomehv = nome
    else:
        if idade > homemv:
            homemv = idade
            nomehv = nome

    if sexo in 'Ff' and idade < 20:
        mme += 1

print('\nO homem mais velho é o {} com {} idade.'.format(nomehv, homemv))
print('A média de idade dessas pessoas é: {:.2f}'.format(media))
print('A quantidade de mulheres menores de 20 anos é: {}'.format(mme))

