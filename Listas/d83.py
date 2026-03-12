calculo = str(input('Digite a expressão: ')).strip()
lista = list(calculo)

if calculo[-1] and calculo[-2] == ')' or calculo[0:3] == '(' or calculo[-1] not in ')':
    print('Sua expressão é Inválida!')
elif calculo[-1] == ')' or calculo.count('(') + calculo.count(')') % 2 > 0:
    print('Sua expressão é válida!')