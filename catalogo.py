from filme import Filme
from registro import Registro


class Catalogo(Registro):
    def __init__(self):
        super().__init__()

    def adicionar(self, filme):
        if isinstance(filme, Filme):
            self.DB.append(filme)

    def remover(self, titulo):
        for filme in self.__DB:
            if filme.titulo == titulo:
                self.DB.remove(filme)

    def consultar(self, titulo):
        for filme in self.DB:
            if filme.titulo == titulo:
                return filme

    def gerar_lista(self):
        lista = []
        for filme in self.DB:
            lista.append(filme.titulo)
        return lista