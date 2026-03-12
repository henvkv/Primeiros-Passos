from rich import inspect

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f'Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa Intel!'

f1 = Funcionario('Nicolas', 'TI', 'Júnior')

print(f1.apresentacao())