class Livro:
    def __init__(self, autor, titulo):
        self.autor = autor
        self.titulo = titulo
        
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

        
