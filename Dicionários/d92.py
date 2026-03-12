from datetime import date

dados = dict()

dados['nome'] = str(input('Nome: '))

ano_de_nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - ano_de_nascimento

ctps = int(input('Carteira de trabalho (0 não tem): '))

if ctps != 0:
    dados['CTPS'] = ctps
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    idade_contratado = dados['Ano de contratação'] - ano_de_nascimento
    dados['Salário'] = float(input('Salário: R$'))
    print('='*30)
    print()
    
    print(f'''O(A) {dados["nome"]} tem {dados["Idade"]} anos.
CTPS: {dados["CTPS"]}. 
Com o ano de contratação em {dados["Ano de contratação"]}.
Recebe: R${dados["Salário"]} por mês.
O(A) {dados["nome"]} se aposenta com {idade_contratado + 35} anos.''')

else:
    print(f'\nO(A) {dados["nome"]} tem {dados["Idade"]} anos e não tem CTPS.')