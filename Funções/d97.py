# DEFININDO AS FUNÇÕES
def escreva(txt):
    tam = len(txt) + 4
    print('~'*tam)
    print(f'{txt}'.center(tam))
    print('~'*tam)

escreva('TESTE')
escreva('DE')
escreva('FUNÇÕES')