from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, nome, pessoas=0):
        self.nome = nome
        self.pessoas = pessoas

    def analisar(self):
        kg = (self.pessoas*400)/1000
        custo = kg*82.4
        cpp = custo/self.pessoas
        
        conteudo = f'''Analisando o {self.nome} com {self.pessoas} pessoas
\nRecomendável: comprar {kg}Kg de carne
Custo: R${custo:.2f}
Custo por pessoa: R${cpp:.2f}'''
        analise = Panel(conteudo, title=self.nome)
        print(analise)

churrasco = Churrasco('Churrasquin', 17)
churrasco.analisar()

churrasco2 = Churrasco('Churrascão', 25)
churrasco2.analisar()