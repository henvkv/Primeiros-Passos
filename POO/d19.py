class Livro:
    pagina_inicial = 1
    
    def __init__(self, titulo, paginas=1):
        self.titulo = titulo
        self.paginas = paginas
        print(f'''O livro: {self.titulo} - tem {self.paginas} páginas. 
Você está na PÁGINA 1''')

    def avancar_pagina(self, qnt):
        Livro.pagina_inicial += qnt
        return Livro.pagina_inicial


l1 = Livro('10 coisas que aprendi', 20)    
avancar = int(input('\nQuantas páginas você gostaria de avançar? '))

print(f'\nAgora você está na página {l1.avancar_pagina(avancar)}.')