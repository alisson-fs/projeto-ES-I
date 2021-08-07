class Aluguel:
    def __init__(self, inicio, fim, filme):
        self.__inicio = inicio
        self.__fim = fim
        self.__filme = filme

    @property
    def inicio(self):
        return self.__inicio
    
    @property
    def fim(self):
        return self.__fim
    
    @property
    def filme(self):
        return self.__filme

    @inicio.setter
    def inicio(self, inicio):
        self.__inicio = inicio

    @fim.setter
    def fim(self, fim):
        self.__fim = fim

    @filme.setter
    def filme(self, filme):
        self.__filme = filme
