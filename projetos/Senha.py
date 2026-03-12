print(20*'-=')
print('CRIE SUA CONTA!!')
print(20*'-=')

s = str(input('Digite a sua senha:'))
sn = str(input('Digite a sua senha novamente:'))
ln1 = ('0') and ('1') and ('2') and ('3') and ('4') and (
    '5') and ('6') and ('7') and ('8') and ('9')

while s != sn:
    tt1 = input('\nAs senhas devem ser iguais.\nDigite sua senha:')
    tt2 = input('Digite a senha novamente:')
    if tt1 == tt2:
        break

while len(sn) < 8 or sn.count(ln1) == 0:
    ln = ('0') and ('1') and ('2') and ('3') and ('4') and (
        '5') and ('6') and ('7') and ('8') and ('9')
    tentativa = input(
        '\nSua senha deve ter no minimo 8 caracteres e um número ou mais.\nDigite sua senha:')
    tentativa1 = input('Digite sua senha novamente:')

    while tentativa != tentativa1:
        tnt = input('As senhas devem ser iguais.\nDigite sua senha:')

        if len(tnt) >= 8 and tnt.count(tnt) == 0:
            tnt3 = input(
                '\nSua senha deve ter um número ou mais.\nDigite sua senha:')

        elif len(tnt) < 8 and tnt.count(tnt) > 0:
            tnt4 = input(
                '\nSua senha deve ter 8 caracteres.\nDigite sua senha:')
            tnn2 = input('Digite novamente:')

    else:
        print('\nParabéns. Senha criada com sucesso!')
        break

        # if cs != s:
        # print(20*'-=')
        # print('\n A senha digitada não condiz com a anterior. Digite novamente!')
