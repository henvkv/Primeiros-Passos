# DEFININDO AS FUNÇÕES
def area(largura, comprimento):
    print(f'{largura*comprimento}m²')

def exibir_texto(txt):
    print(txt)
    print('-'*30)

# DEFININDO AS VARIAVEIS
exibir_texto('Controle de terreno')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

# MOSTRANDO RESULTADO
exibir_texto('\nÁREA')
area(largura, comprimento)